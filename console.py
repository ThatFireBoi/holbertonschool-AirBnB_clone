#!/usr/bin/python3
"""This program defines a command interpreter for the HBnB console"""


import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines attributes and methods for the HBnB console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_help(self, arg):
        """Help command to show available commands"""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
