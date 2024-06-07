""" Héritage Multiple """


class Cat:
    """Un chat."""

    def meow(self):
        """Miaule."""
        print("Meow!")


class Talker:
    """Interface qui définit la méthode "say" (dire)."""

    def say(self, to_say):
        """Affiche "to_say" (à dire)."""
        print(to_say)


class TalkingCat(Cat, Talker):
    """Un chat qui parle ??"""

    pass


salem = TalkingCat()
salem.meow()
salem.say("Hello!")
