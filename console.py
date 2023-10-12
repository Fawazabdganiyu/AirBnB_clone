#!/usr/bin/python3
"""
Module Name: console.py
Description: This is a program and it contains the entry point of the
command interpreter.

"""
from models import storage
from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """A definition of `HBNBCommand` class inherited from `Cmd`
    for command interpreter

    Args:
        line (string): A space separated argument for the program.

    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit the interpreter on receiving `quit` command"""
        return True

    def help_quit(self):
        """displays custom quide for command `quit`"""
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """Exit the program on receiving EOF signal"""
        return True

    def emptyline(self):
        """Overide the base class method not to print anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id

        Example:
            `(hbnb) create BaseModel`

        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            # Create the expected instance
            obj = BaseModel()
            obj.save()
            print(f"{obj.id}")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and `id`.

        Example:
            `(hbnb) show BaseModel 1234-1234-1234`

        """
        args = line.split()

        # Get objects dictionary in the form { <BaseModel.id>=<obj>,... }
        all_objs = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"BaseModel.{args[1]}" not in all_objs.keys():
            print("** no instance found **")
        else:
            print(all_objs[f"BaseModel.{args[1]}"])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and
        `id`. Then save the change into the JSON file

        Example:
            `(hbnb) destroy BaseModel 1234-1234-1234`

        """
        args = line.split()

        # Get objects dictionary in the form { <BaseModel.id>=<obj>,... }
        all_objs = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"BaseModel.{args[1]}" not in all_objs.keys():
            print("** no instance found **")
        else:
            del all_objs[f"BaseModel.{args[1]}"]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances,
        based or not on the class name

        Example:
           `(hbnb) all BaseModel` or
           `(hbnb) all`

        """
        args = line.split()
        # Get objects dictionary in the form { <BaseModel.id>=<obj>,... }
        all_objs = storage.all()

        if len(args) == 0 or (len(args) == 1 and args[0] == "BaseModel"):
            # Represent all instances in a list
            all_objs_list = [str(v) for v in all_objs.values()]
            print(all_objs_list)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()