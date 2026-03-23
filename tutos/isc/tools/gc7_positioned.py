import flet as ft

def position(page):
    screen_width = 1920
    window_width = 500

    page.window.left = screen_width - window_width
    page.window.top = 0
    page.window.width = window_width
    page.window.height = 940 # 1040"
    page.window.resizable = False
    
    t = '123 abcd From tools/gc7_positioned.py (Bref, un sous-dossier)'
    page.add(ft.Text(t, size=24, color=ft.Colors.ORANGE_500))

import locale

def nf(f, dec=2):
    "Number Format 123456789 → 123 456,79"
    try:
        f = float(f)
        return locale.format_string(f"%.{dec}f", f, grouping=True)
    except ValueError:
        src = caller_info()
        # print(src)
        print(
            f"⚠️ Errorfor nf() in main_tools:\n\033[1;31mBad data type ({type(f).__name__}) -> {f} (Line {src[2]} in {src[0]}){EB}"
        )
        return str(f)
