# top.py
import time

class Top:
    def __init__(self):
        self._start = None
        self._lap_count = 0

    def start(self):
        """Démarre le chrono."""
        self._start = time.perf_counter()
        self._lap_count = 0

    def lap(self):
        """Affiche un temps intermédiaire sans arrêter le chrono."""
        if self._start is None:
            print("Chrono non démarré")
            return

        now = time.perf_counter()
        elapsed = now - self._start
        self._lap_count += 1

        self._print_time(elapsed, prefix=f"Lap {self._lap_count}")

    def stop(self):
        """Arrête le chrono et affiche le temps total."""
        if self._start is None:
            print("Chrono non démarré")
            return

        now = time.perf_counter()
        elapsed = now - self._start
        self._start = None

        self._print_time(elapsed, prefix="Total")

    @staticmethod
    def _print_time(seconds, prefix=""):
        """Formatage HH:MM:SS.ss"""
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = seconds % 60
        print(f"{prefix} : {h:02d}:{m:02d}:{s:05.2f}")
