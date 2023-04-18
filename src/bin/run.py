"""
Import dependencies
"""
from program.menu import Menu

"""
Main is the entry running dependencies from singleton 
"""


class Main(Menu):
    def run(self):
        self.run_program()


m = Main()
m.run()
