def examples():

    print("Value in built variable name is:  ", __name__)
    
    print("{} and {}".format("a", "b"))
    print("{0} and {1}".format("a", "b"))
    print("{one} and {two}\n".format(one="a", two="b"))

    print("{0} en binaire: {0:b}".format(7))
    print("The scientific value of {0} is : {0:e}\n".format(4000))

    print("The float value of {0} is {0:.2f}".format(40.789))

    print("The hexa value of {0} is : {0:x}\n".format(255))

    print("The value is : {:%}".format(0.8123))
    print("The value is : {:.2f}%\n".format(0.8123 * 100))
    print("The value is : {:.2%}\n".format(0.8123))

    print(
        "The value is : {:_.2f}\n".format(10000.789000)
        .replace("_", " ")
        .replace(".", ",")
    )

    print("The value is: {:9.2f}".format(1))
    print("The value is: {:9.2f}".format(40))

    print("The value is: {:-}".format(40))
    print("The value is: {:+}".format(40))

    print("The value {:^10} is a positive value".format(40))
    print("The value {:>10} is positive value".format(40))
    print("The value {:>10} is positive value\n".format(4))

    class MyClass:
        msg1 = "Guru"
        msg2 = "Tutorials"

    print("Welcome to {c.msg1}99 {c.msg2}!\n".format(c=MyClass()))

    my_dict = {"msg1": "Welcome", "msg2": "Guru99"}
    print("{m[msg1]} to {m[msg2]} Tutorials!\n".format(m=my_dict))

    print("I have {:5} dogs and {:5} cat".format(2, 1))
    print("I have {1:5} dogs and {0:5} cat".format(1, 2))


if __name__ == "__main__":
    examples()
