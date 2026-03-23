"""
    Fonction de tri que nous allons utiliser pour trier nos chats. Les variables utilisant un typage implicite, nous pouvons trier n'importe quoi à partir du moment 
    où les opérateurs existent 
"""


def sort_insertion(l):
    for i in range(len(l)):
        j = i
        while j > 0 and l[j] < l[j - 1]:
            l[j - 1], l[j] = l[j], l[j - 1]
            j -= 1


"""
    Classe qui nous permet de définir ce qu'est un chat et de définir les opérateurs qui vont servir au tri
"""


class chat:
    color_priority = {"noir": 4, "blanc": 3, "gris": 2, "brun": 1}
    neutered_priority = {"Oui": 2, "Non": 1}
    sex_priority = {"femelle": 2, "male": 1}

    def __init__(self, name, color, neutered, sex, size):
        self.name = name
        self.color = color
        self.neutered = neutered
        self.sex = sex
        self.size = size

    # ==
    def __eq__(self, other):
        if (
            self.color == other.color
            and self.neutered == other.neutered
            and self.sex == other.sex
            and self.size == other.size
        ):
            return True
        return False

    # !=
    def __ne__(self, other):
        return self != other

    # <
    def __lt__(self, other):
        if self.color_priority[self.color] != self.color_priority[other.color]:
            return self.color_priority[self.color] < self.color_priority[other.color]
        elif (
            self.neutered_priority[self.neutered]
            != self.neutered_priority[other.neutered]
        ):
            return (
                self.neutered_priority[self.neutered]
                < self.neutered_priority[other.neutered]
            )
        elif self.sex_priority[self.sex] != self.sex_priority[other.sex]:
            return self.sex_priority[self.sex] < self.sex_priority[other.sex]
        else:
            return self.size > other.size

    # >
    def __gt__(self, other):
        return (self >= other) and (self != other)

    # <=
    def __le__(self, other):
        return self < other or self == other

    # >=
    def __ge__(self, other):
        return self > other or self == other


if __name__ == "__main__":
    # name, color, neutered, sex, size
    list_chats = []
    list_chats.append(chat("Felix     ", "noir", "Non", "male", "45"))
    list_chats.append(chat("Felicia   ", "brun", "Non", "femelle", "40"))
    list_chats.append(chat("Garfield  ", "noir", "Oui", "male", "35"))
    list_chats.append(chat("Figaro    ", "blanc", "Non", "femelle", "47"))
    list_chats.append(chat("Azrael    ", "blanc", "Non", "male", "37"))
    list_chats.append(chat("Grumpycat ", "noir", "Oui", "femelle", "42"))
    list_chats.append(chat("Tom       ", "brun", "Non", "male", "38"))
    list_chats.append(chat("HelloKitty", "brun", "Oui", "femelle", "41"))
    list_chats.append(chat("Isidor    ", "gris", "Non", "male", "40"))

for n in range(2):
    for i in list_chats:
        print(f"{i.name}\t{i.color}\t{i.neutered}\t{i.sex}\t{i.size}")
    if not n:
        nbs = 12
        print("\n" + "=" * nbs, "Trions les chats", "=" * nbs, "\n")
        sort_insertion(list_chats)
