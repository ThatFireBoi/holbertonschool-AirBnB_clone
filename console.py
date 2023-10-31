#!/usr/bin/python3
"""This program defines a command interpreter for the HBnB console"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
