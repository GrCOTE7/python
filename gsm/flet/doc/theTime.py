from datetime import datetime as dt
import locale

locale.setlocale(locale.LC_ALL, "fr_FR")

def theTime(page=None):
    now = dt.now()
    theTime = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"
    # print(theTime, page.route)
    return theTime


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
