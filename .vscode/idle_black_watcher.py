from __future__ import annotations

import argparse
import subprocess
import threading
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

# ❌ Rendre le terminal caché (watcher silencieux)
# ❌ transformer le watcher en service Windows (il tourne même sans VS Code)

IGNORED_DIR_PARTS = {
    ".git",
    "__pycache__",
    "node_modules",
    ".venv",
    ".venv313",
    ".venv315",
    ".idea",
    ".vscode",
}


def log(msg: str) -> None:
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[idle-black {now}] {msg}", flush=True)


class IdleBlackHandler(FileSystemEventHandler):

    def __init__(
        self,
        delay: float,
        default_python_exe: str,
        workspace: Path,
        routes: List[Tuple[str, str]],
    ) -> None:
        self.delay = delay
        self.default_python_exe = default_python_exe
        self.workspace = workspace
        self.routes = sorted(routes, key=lambda item: len(item[0]), reverse=True)

        self._timers: Dict[Path, threading.Timer] = {}
        self._last_formatted: Dict[Path, float] = {}
        self._lock = threading.Lock()

        log(f"handler init: delay={delay}, default_python={default_python_exe}")
        if self.routes:
            log("routes:")
            for prefix, py in self.routes:
                shown = prefix or "<root>"
                log(f"  - {shown} -> {py}")

    def on_modified(self, event: FileSystemEvent) -> None:
        self._schedule(event)

    def on_created(self, event: FileSystemEvent) -> None:
        self._schedule(event)

    def _should_ignore(self, path: Path) -> bool:
        # ignore non .py
        if path.suffix != ".py":
            return True

        # ignore certains dossiers
        for part in path.parts:
            if part in IGNORED_DIR_PARTS or part.startswith(".venv"):
                return True

        return False

    def _schedule(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return

        path = Path(event.src_path)

        if self._should_ignore(path):
            return

        now = time.time()
        last = self._last_formatted.get(path, 0.0)
        # anti-spam : ne pas reformater le même fichier trop vite
        if now - last < 1.5:
            return

        with self._lock:
            timer = self._timers.get(path)
            if timer is not None:
                timer.cancel()

            timer = threading.Timer(self.delay, self._format_file, args=(path,))
            timer.daemon = True
            self._timers[path] = timer
            timer.start()

    def _format_file(self, path: Path) -> None:
        if not path.exists():
            return

        python_exe = self._select_python(path)
        cmd = [python_exe, "-m", "black", str(path)]

        rel = None
        try:
            rel = path.relative_to(self.workspace)
        except Exception:
            rel = path

        log(f"formatting: {rel} with {python_exe}")

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
            )
        except Exception as exc:
            with self._lock:
                self._timers.pop(path, None)
            log(f"ERROR running black on {rel}: {exc!r}")
            return

        with self._lock:
            self._timers.pop(path, None)

        if result.returncode == 0:
            self._last_formatted[path] = time.time()
            log(f"OK: {rel}")
        else:
            stderr = (result.stderr or "").strip() or "unknown black error"
            stdout = (result.stdout or "").strip()
            log(f"FAIL: {rel} -> {stderr}")
            if stdout:
                log(f"black stdout: {stdout}")

    def _select_python(self, path: Path) -> str:
        try:
            rel = (
                path.resolve().relative_to(self.workspace.resolve()).as_posix().lower()
            )
        except Exception:
            return self.default_python_exe

        for prefix, python_exe in self.routes:
            if rel.startswith(prefix):
                return python_exe
        return self.default_python_exe


def parse_routes(raw_routes: List[str]) -> List[Tuple[str, str]]:
    routes: List[Tuple[str, str]] = []
    for raw in raw_routes:
        if "=" not in raw:
            raise ValueError(
                f"Invalid --route value: {raw}. Expected <prefix>=<python>"
            )
        prefix, python_exe = raw.split("=", 1)
        clean_prefix = prefix.strip().replace("\\", "/").strip("/").lower()
        if clean_prefix:
            clean_prefix += "/"
        routes.append((clean_prefix, python_exe.strip()))
    return routes


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Format Python files with Black after inactivity."
    )
    parser.add_argument("--workspace", required=True, help="Workspace folder to watch")
    parser.add_argument(
        "--delay", type=float, default=2.5, help="Debounce delay in seconds"
    )
    parser.add_argument(
        "--python", required=True, help="Python executable used to run Black"
    )
    parser.add_argument(
        "--route",
        action="append",
        default=[],
        help="Optional path route: <folder/prefix>=<python_executable>",
    )
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    routes = parse_routes(args.route)

    log(f"watching: {workspace}")
    log(f"delay: {args.delay:.1f}s")
    handler = IdleBlackHandler(
        delay=args.delay,
        default_python_exe=args.python,
        workspace=workspace,
        routes=routes,
    )

    observer = Observer()
    observer.schedule(handler, str(workspace), recursive=True)

    while True:
        try:
            observer.start()
            log("observer started")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            log("KeyboardInterrupt, stopping observer…")
            observer.stop()
            break
        except Exception as exc:
            log(f"observer crashed: {exc!r}, restarting in 3s…")
            observer.stop()
            time.sleep(3)
            observer = Observer()
            observer.schedule(handler, str(workspace), recursive=True)
        finally:
            observer.join()


if __name__ == "__main__":
    main()
