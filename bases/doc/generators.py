r = range(3)
print(list(r))
print(sum(i**2 for i in r))  # sum of squares

xvec = [1, 2, 3]
yvec = [7, 5, 3]
lvec = list(zip(xvec, yvec))
print(lvec)
print(sum(x * y for x, y in zip(xvec, yvec)))  # dot product

graduates = [{"name": "Pier", "gpa": 5}, {"name": "Pol", "gpa": 7}]
print("Victorian: ", max(graduates, key=lambda student: student["gpa"]))


class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa


graduates = [Student("Pier", 5), Student("Pol", 7)]
print("Victorian: ", max((student.gpa, student.name) for student in graduates))


# Mots uniques d'un page
with open("data.txt") as page:
    unique_words = set(word for line in page for word in line.split())
print(unique_words)
