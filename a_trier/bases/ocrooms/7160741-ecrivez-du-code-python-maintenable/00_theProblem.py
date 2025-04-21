def main():
    """Main script"""
    print("Hello World")
    print(is_leap_year(1996))


def is_leap_year(year):
    """Return true (bool) if year is leap else false"""
    # Les années bissextiles sont toutes des multiples de 4
    if year % 4 != 0:
        return False

    # Les années séculaires ne sont pas bissextiles, hormis 1600, 2000, 2400, etc.
    if year % 100 == 0:
        return year % 400 == 0

    # Tous les autres résultats sont vrais.
    return True


def adjustment(value):
    """Return true (bool) if year is leap else false"""
    return (value % 4 == 0) and (value % 100 != 0 or value % 400 == 0)


if __name__ == "__main__":
    main()
