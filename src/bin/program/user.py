class User:
    def __init__(self, usr, pw):
        self.username = usr
        self.password = pw

    def get_user(self):
        return list(self.username)[0]

    def get_pass(self):
        return list(self.password)[0]

    def __str__(self):
        return list(self.username)[0]
