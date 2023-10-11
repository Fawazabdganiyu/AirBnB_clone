#!/usr/bin/python3
"""
Module Name: console.py
Description: This is a program and it contains the entry point of the
command interpreter.

"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """A definition of `HBNBCommand` class inherited from `Cmd`
    for command interpreter

    Args:
        line (string): A space separated argument for the program.

    """
    prompt = "(hbnb) "

    def precmd(self, line):
        """Overrides to separate the `line` argument based on it spaces

        Return (list):
            A list of arguments passed to the program

        """
        args = line.split(' ')

        return cmd.Cmd.precmd(self, args)

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

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id

        """
        if len(line) == 0:
            print("** class name missing **")
        if line[0] != "BaseModel":
            print("** class doesn't exist **")

            # Create the expected instance
            obj = BaseModel()
            obj.save()
            print(f"{obj.id}")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and `id`.

        """
        if len(line) == 0:
            print("** class name missing **")
        if line[0] != "BaseModel":
            print("** class doesn't exist **")
        if line[1] == None:
            print("** instance id missing **")

        search = f"BaseMode.{line[1]}"
        found = 0
        try:
            with open("file.json", mode='r', encoding='utf-8') as f:
                objs_dict = json.load(f)

            # Search the dict generated from file.json
            for k in objs_dict.keys():
                if k == search:
                    found = 1
                    obj_attr = objs_dict[k]
                    obj = BaseModel(**objs_attr)
                    print(obj)
                else:
                    found = 0

            if found = 0:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
