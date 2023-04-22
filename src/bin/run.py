"""
Import dependencies
"""
from program.authenticate import verify
from program.menu import *

"""
Main class is the entry to the program
"""


class Main:
    """
    Main class will have one welcome message and initialize the program
    if the user decide to do so.
    """
    def login(self):
        token = boarding()
        if token:
            self.run()

    def run(self):
        """
        :return: A boolean and current logged-in user object
        """
        token, user = verify()
        if token and user is not None:
            run_program(user)
        else:
            print('Main')


m = Main()
m.login()
