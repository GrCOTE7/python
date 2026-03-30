from __future__ import annotations

import argparse
import subprocess
import threading
import time
from pathlib import Path

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer


class IdleBlackHandler(FileSystemEventHandler):
    def __init__(
        self,
        delay: float,
        default_python_exe: str,
        workspace: Path,
        routes: list[tuple[str, str]],
    ) -> None:
        self.delay = delay
        self.default_python_exe = default_python_exe
        self.workspace = workspace
        self.routes = sorted(routes, key=lambda item: len(item[0]), reverse=True)
        self._timers: dict[Path, threading.Timer] = {}
        self._last_formatted: dict[Path, float] = {}
        self._lock = threading.Lock()

    def on_modified(self, event: FileSystemEvent) -> None:
        self._schedule(event)

    def on_created(self, event: FileSystemEvent) -> None:
        self._schedule(event)

    def _schedule(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return

        path = Path(event.src_path)
        if path.suffix != ".py":
            return

        if any(
            part in {".git", "__pycache__", "node_modules"} or part.startswith(".venv")
            for part in path.parts
        ):
            return

        now = time.time()
        last = self._last_formatted.get(path, 0.0)
        if now - last < 1.0:
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
        result = subprocess.run(cmd, capture_output=True, text=True)

        with self._lock:
            self._timers.pop(path, None)

        if result.returncode == 0:
            self._last_formatted[path] = time.time()
            rel = path.relative_to(self.workspace)
            print(
                f"[idle-black] formatted: {rel} ({Path(python_exe).name})", flush=True
            )
        else:
            stderr = result.stderr.strip() or "unknown black error"
            print(f"[idle-black] failed: {path} -> {stderr}", flush=True)

    def _select_python(self, path: Path) -> str:
        rel = path.resolve().relative_to(self.workspace.resolve()).as_posix().lower()
        for prefix, python_exe in self.routes:
            if rel.startswith(prefix):
                return python_exe
        return self.default_python_exe


def parse_routes(raw_routes: list[str]) -> list[tuple[str, str]]:
    routes: list[tuple[str, str]] = []
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
    handler = IdleBlackHandler(
        delay=args.delay,
        default_python_exe=args.python,
        workspace=workspace,
        routes=routes,
    )

    observer = Observer()
    observer.schedule(handler, str(workspace), recursive=True)
    observer.start()

    print(f"[idle-black] watching: {workspace}", flush=True)
    print(f"[idle-black] delay: {args.delay:.1f}s", flush=True)
    if routes:
        print("[idle-black] routes:", flush=True)
        for prefix, python_exe in routes:
            shown = prefix or "<root>"
            print(f"  - {shown} -> {python_exe}", flush=True)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    finally:
        observer.join()


if __name__ == "__main__":
    main()
