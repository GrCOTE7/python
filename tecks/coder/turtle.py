def triangle():
    for i in range(1, 8):
        str = ""
        for j in range(1, i + 1):
            str += " *"
        print(str.center(26))

triangle()
