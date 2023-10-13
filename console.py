#!/usr/bin/python3
"""
Module Name: console.py
Description: This is a program and it contains the entry point of the
command interpreter.

"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """A definition of `HBNBCommand` class inherited from `Cmd`
    for command interpreter

    Args:
        line (string): A space separated argument for the program.

    """
    prompt = "(hbnb) "

    # List of classes
    __class_list = ["BaseModel", "User", "State", "City", "Place",
                    "Amenity", "Review"]

    def do_quit(self, line):
        """Quit the interpreter on receiving `quit` command"""
        return True

    def help_quit(self):
        """displays custom guide for command `quit`"""
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """Exit the program on receiving EOF signal"""
        print()
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
        class_list = HBNBCommand.__class_list
        class_name = line

        if class_name == "":
            print("** class name missing **")
        elif class_name not in class_list:
            print("** class doesn't exist **")
        else:
            # Create the expected instance
            obj = globals()[class_name]()
            obj.save()
            print(f"{obj.id}")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and `id`.

        Example:
            `(hbnb) show BaseModel 1234-1234-1234`

        """
        # Get objects dictionary in the form { <BaseModel.id>=<obj>,... }
        all_objs = storage.all()
        # List of available object classes
        class_list = HBNBCommand.__class_list

        obj_class_name = ""
        obj_id = ""

        args = line.split()
        args_num = len(args)

        if args_num >= 1:
            obj_class_name = args[0]
        if args_num == 2:
            obj_id = args[1]

        if obj_class_name == "":
            print("** class name missing **")
        elif obj_class_name not in class_list:
            print("** class doesn't exist **")

        elif obj_id == "":
            print("** instance id missing **")
        elif f"{obj_class_name}.{obj_id}" not in all_objs.keys():
            print("** no instance found **")
        else:
            print(all_objs[f"{obj_class_name}.{obj_id}"])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and
        `id`. Then save the change into the JSON file

        Example:
            `(hbnb) destroy BaseModel 1234-1234-1234`

        """
        # Get objects dictionary in the form { <BaseModel.id>=<obj>,... }
        all_objs = storage.all()

        # List of object classes
        class_list = HBNBCommand.__class_list

        args = line.split()
        args_num = len(args)

        obj_class_name = ""
        obj_id = ""

        if args_num >= 1:
            obj_class_name = args[0]
        if args_num == 2:
            obj_id = args[1]

        if obj_class_name == "":
            print("** class name missing **")
        elif obj_class_name not in class_list:
            print("** class doesn't exist **")
        elif obj_id == "":
            print("** instance id missing **")
        elif f"{obj_class_name}.{obj_id}" not in all_objs.keys():
            print("** no instance found **")
        else:
            del all_objs[f"{obj_class_name}.{obj_id}"]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances,
        based or not on the class name

        Example:
           `(hbnb) all BaseModel` or all User
           `(hbnb) all`

        """
        # Get objects dictionary in the form { <BaseModel.id>=<obj>,... }
        all_objs = storage.all()

        # List of available object classes
        class_list = HBNBCommand.__class_list

        class_name = ""

        args = line.split()
        args_num = len(args)

        if args_num == 1:
            class_name = args[0]

        # If the class name is missing, prints all objects of all classes
        if class_name == "":
            all_objs_list = [str(obj) for obj in all_objs.values()]
            print(all_objs_list)

        # If the class name exist, prints all objects that belong to class name
        elif class_name in class_list:
            class_objs_list = [str(obj) for obj in all_objs.values()
                               if obj.__class__.__name__ == class_name]
            print(class_objs_list)

        # Otherwise, it is an invalid class
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update the value of an Instance attribute

    SYPNOSIS:
        update <class_name> <obj_id> <attr_name> <attr_value>

    Example:
        `(hbnb) update BaseModel 1234-1234 email "airbnb@mail"`
        """
        # Default values to track validity
        class_name = ""
        obj_id = ""
        attr_name = ""
        attr_value = ""
        obj = ""

        # List of available objects classes
        class_list = HBNBCommand.__class_list

        # Dictionary containing all objects of all classes
        all_objs = storage.all()

        # Get list of arguments passed
        args = shlex.split(line)
        args_num = len(args)

        # Assignment
        if args_num >= 1:
            class_name = args[0]
        if args_num >= 2:
            obj_id = args[1]
        if args_num >= 3:
            attr_name = args[2]
        if args_num >= 4:
            attr_value = args[3]

        obj_key = f"{class_name}.{obj_id}"  # object key

        # Validation
        if class_name == "":
            print("** class name missing **")
        elif class_name not in class_list:
            print("** class doesn't exist **")

        elif obj_id == "":
            print("** instance id missing **")
        elif obj_key not in all_objs.keys():
            print("** no instance found **")

        elif attr_name == "":
            print("** attribute name missing **")
        elif attr_value == "":
            print("** value missing **")

        # Updation
        else:
            # object information
            obj = all_objs[obj_key]

            # Test for string
            if attr_value.isalpha():
                pass
            # Test for integers
            elif attr_value.isdecimal():
                attr_value = int(attr_value)
            # Test for floats
            else:
                attr_value = float(attr_value)

            # Update/set the attribute with the new value
            setattr(obj, attr_name, attr_value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
