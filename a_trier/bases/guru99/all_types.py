age = [59, 2]
print(isinstance(age, list))
print("-" * 72)


class MyClass:
    """Exemple class"""

    x = "Hello World"
    y = 50


t1 = type("NewClass", (MyClass,), dict(x="Hello World", y=50))
print(type(t1), end=": ")
print(vars(t1))
print("-" * 72)

str_list = "Welcome to Guru99"
age = 50
pi = 3.14
c_num = 3j + 10
my_list = ["A", "B", "C", "D"]
my_tuple = ("A", "B", "C", "D")
my_dict = {"A": "a", "B": "b", "C": "c", "D": "d"}
my_set = {"A", "B", "C", "D"}

print("The type is : ", type(str_list))
print("The type is : ", type(age))
print("The type is : ", type(pi))
print("The type is : ", type(c_num))
print("The type is : ", type(my_list))
print("The type is : ", type(my_tuple))
print("The type is : ", type(my_dict))
print("The type is : ", type(my_set))
