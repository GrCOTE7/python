from dataclasses import dataclass


def example01():
    @dataclass
    class Adresse:
        rue: str
        ville: str
        code_postal: str

    @dataclass
    class Personne:
        nom: str
        age: int
        adresse: Adresse

    a = Adresse("2 rue Machin", "Dijon", "21000")
    p = Personne("Lionel", 60, a)

    print(p.adresse.rue)


def example02():
    @dataclass
    # @dataclass(frozen=True)
    class User:
        name: str = "Who ?"
        email: str = "unknown"

    def modif_user(user):
        user.name = "Toto"

    # u = User(name="Lionel", email="lionel@gmail.com")
    # u = User(email="lionel@gmail.com", name="Lionel")
    # u = User(email="lionel@gmail.com")
    u = User(name="Lionel")
    modif_user(u)

    print(u)


if __name__ == "__main__":
    # example01()
    example02()
