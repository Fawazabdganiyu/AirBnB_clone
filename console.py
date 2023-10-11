#!/usr/bin/python3
"""
Module Name: console.py
Description: This is a program and it contains the entry point of the
command interpreter.

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """A definition of `HBNBCommand` class inherited from `Cmd`
    for command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """quits the interpreter on receiving `quit` command"""
        return True

    def help_quit(self):
        """displays custom quide for command `quit`"""
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """quits the interpreter on EOF signal"""
        return True

    def emptyline(self):
        """Overide the base class method not to print anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
