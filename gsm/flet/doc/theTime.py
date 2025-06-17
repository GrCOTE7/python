from datetime import datetime as dt

def theTime(page=None):
    now = dt.now()
    theTime = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"
    # print(theTime, page.route)
    return theTime
