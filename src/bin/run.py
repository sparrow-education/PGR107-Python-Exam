"""
Import dependencies
"""
from program.menu import run_program as init
from program.authenticate import verify
"""
Main is the entry running dependencies from singleton 
"""


class Main:
    def run(self):
        token, user = verify()
        if token:
            init()
        else:
            print('Main')


m = Main()
m.run()
