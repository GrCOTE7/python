class User:
    """Un utilisateur."""

    def __init__(self, username, password):
        """Initialise le nom et le mot de passe."""
        if len(username) < 3:
            raise UsernameTooShortException()
        if len(password) < 5:
            raise PasswordTooShortException()

        self.username = username
        self.password = password


class UsernameTooShortException(Exception):
    """Erreur sur le nom d'utilisateur."""

    def __init__(self, msg="", *args, **kwargs):
        """Init le message."""
        msg = msg or "Le nom d'utilisateur est trop court !"
        super().__init__(msg, *args, **kwargs)


class PasswordTooShortException(Exception):
    """Erreur sur le mot de passe."""

    def __init__(self, msg="", *args, **kwargs):
        """Init le message."""
        msg = msg or "Le mot de passe est trop court !"
        super().__init__(msg, *args, **kwargs)


if __name__ == "__main__":
    try:
        user = User("John", "pwd")
    except UsernameTooShortException:
        print("L'exception sur le nom d'utilisateur a été levée.")

    except PasswordTooShortException:
        print("L'exception sur le mot de passe a été levée.")
print("Fini")
