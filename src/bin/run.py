"""
Import dependencies
"""
from program.authenticate import verify
from program.menu import *

"""
Main is the entry running dependencies from singleton 
"""


class Main:
    def login(self):
        token = boarding()
        if token:
            self.run()

    def run(self):
        token, user = verify()
        if token and user is not None:
            run_program(user)
        else:
            print('Main')


m = Main()
m.login()
