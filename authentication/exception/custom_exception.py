class DoesNotExists(Exception):
    def __init__(self):
        self.message = "User with provided creds doesn't exists."

    def __str__(self):
        return self.message


class IncorrectCreds(Exception):
    def __init__(self):
        self.message = "Username or Password is not correct. Please check and try again"

    def __str__(self):
        return self.message