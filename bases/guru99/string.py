string = "python at guru99"
print(string.title())

x = "Guru99"
x.replace("Guru99", "Python")
print(x)
x = x.replace("Guru99", "Python")
print(x)

str1 = " Welcome to Guru99!  "
after_strip = str1.strip()
print(len(str1), len(after_strip), str1, after_strip)

str1 = "****Welcome to Guru99!****"
after_strip = str1.strip("*")
print(after_strip)

print(" " * 55 + "\n")

arr = [1, 2, 3]
print(arr, len(arr), arr.count(2))

mystring = "Meet Guru99 Tutorials Site.Best site for Python Tutorials!"
print(mystring[5:40])
print("The position of Best site is at:", mystring.find("Best site", 5, 40))
print("The position of Guru99 is at:", mystring.find("Guru99", 20))

my_string = "test string test, test string testing, test string test string"
print(my_string.count('test'))
