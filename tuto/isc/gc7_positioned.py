def position(page):
    screen_width = 1920
    window_width = 500

    page.window.left = screen_width - window_width
    page.window.top = 0
    page.window.width = window_width
    page.window.height = 1040
    page.window.resizable = False
