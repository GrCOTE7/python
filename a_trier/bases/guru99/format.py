def examples():

    print("01 - Value in built variable name is:  ", __name__)

    print("{} and {}".format("a", "b"))
    print("{0} and {1}".format("a", "b"))
    print("{one} and {two}\n".format(one="a", two="b"))

    print("02 - {0} en binaire: {0:b}".format(7))

    print("03 - The scientific value of {0} is : {0:e}\n".format(4000))

    print("04 - The float value of {0} is {0:.2f}".format(40.789))

    print("05 - The hexa value of {0} is : {0:x}\n".format(255))

    print("06 - The value is : {:%}".format(0.8123))
    print("07 - The value is : {:.2f}%\n".format(0.8123 * 100))
    print("08 - The value is : {:.2%}\n".format(0.8123))

    print(
        "09 - The value is : {:_.2f}\n".format(10000.789000)
        .replace("_", " ")
        .replace(".", ",")
    )

    print("10 - The value is: {:9.2f}".format(1))
    print("11 - The value is: {:9.2f}".format(40))

    print("12 - The value is: {:-}".format(40))
    print("13 - The value is: {:+}".format(40))

    print("14 - The value {:^10} is a positive value".format(40))
    print("15 - The value {:>10} is a positive value".format(40))
    n = 4
    cas_n = "positive" if n >= 0 else "negative"
    print(f"16 - The value {n:>10} is a {cas_n} value\n")

    class MyClass:
        msg1 = "Guru"
        msg2 = "Tutorials"

    print("17 - Welcome to {c.msg1}99 {c.msg2}! (class)\n".format(c=MyClass()))

    my_dict = {"msg1": "Welcome", "msg2": "Guru99"}
    print("17 - {m[msg1]} to {m[msg2]} Tutorials (dict)!\n".format(m=my_dict))

    print("18 - I have {:5} dogs and {:5} cat".format(2, 1))
    print("19 - I have {1:5} dogs and {0:5} cat".format(1, 2))


if __name__ == "__main__":
    examples()
