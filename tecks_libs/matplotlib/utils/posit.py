import ctypes
from typing import Any, cast

def place_figure_on_monitor(fig, monitor_index=1, window_width=900, window_height=700):
    manager = fig.canvas.manager
    if manager is None or not hasattr(manager, "window"):
        return

    window = cast(Any, manager).window

    # Tk geometry uses virtual desktop coordinates.
    left = 0
    top = 0
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    if monitor_index > 0:
        try:
            monitors = []

            class RECT(ctypes.Structure):
                _fields_ = [
                    ("left", ctypes.c_long),
                    ("top", ctypes.c_long),
                    ("right", ctypes.c_long),
                    ("bottom", ctypes.c_long),
                ]

            def callback(_monitor, _hdc, rect_ptr, _lparam):
                r = rect_ptr.contents
                monitors.append((r.left, r.top, r.right, r.bottom))
                return 1

            monitor_enum_proc = ctypes.WINFUNCTYPE(
                ctypes.c_int,
                ctypes.c_ulong,
                ctypes.c_ulong,
                ctypes.POINTER(RECT),
                ctypes.c_double,
            )

            ctypes.windll.user32.EnumDisplayMonitors(
                0, 0, monitor_enum_proc(callback), 0
            )

            monitors.sort(key=lambda m: (m[0], m[1]))
            if len(monitors) > monitor_index:
                m_left, m_top, m_right, m_bottom = monitors[monitor_index]
                left = m_left
                top = m_top
                screen_width = m_right - m_left
                screen_height = m_bottom - m_top
        except Exception:
            pass

    # x_pos = left + max(0, screen_width - window_width)
    x_pos = left
    y_pos = top + max(0, (screen_height - window_height) // 2)
    window.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
