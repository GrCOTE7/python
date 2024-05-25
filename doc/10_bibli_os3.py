# dates are easily constructed and formatted
from datetime import date
import locale

now = date.today()
print(now)
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
print(now.strftime('%A %d %B %Y'))

print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))


# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)


from urllib.request import urlopen

with urlopen("http://worldtimeapi.org/api/timezone/etc/UTC.txt") as response:
    for line in response:
        line = line.decode()  # Convert bytes to a str
        if line.startswith("datetime"):
            print(line.rstrip())  # Remove trailing newline


import smtplib

server = smtplib.SMTP("localhost", 1025)
server.sendmail(
    "soothsayer@example.org",
    "jcaesar@example.org",
    """To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""",
)
server.quit()
