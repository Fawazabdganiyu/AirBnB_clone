#!/usr/bin/python3
"""
Module Name: console.py
Description: This is a program and it contains the entry point of the
command interpreter.

"""
import cmd
import re
import shlex
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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

        SYNOPSIS:
            create <class name>

        Example:
            `(hbnb) create BaseModel`
            <id>
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

        SYNOPSIS:
            show <class name> <id>
            <class name>.show(<id>)

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
        if args_num >= 2:
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

        SYNOPSIS:
            destroy <class name> <id>
            <class name>.destroy(<id>)

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
        if args_num >= 2:
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
        based or not on the class name.

        SYNOPSIS:
            all
            all <class name>
            <class name>.all()

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
        <class name>.update(<id>, <attribute name>, <attribute value>)
        <class name>.update(<id>, <dictionary representation>)

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
            if not attr_value.isdigit():
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

    def do_count(self, line):
        """
        Counts the number of objects that is present in storage
        from a particular class.

        SYNOPSIS:
            count <class name>
            <class name>.count()

        Example:
            (hbhb) count User
            3
            (hbnb) User.count()
            3
        """
        class_name = line
        if class_name == "":
            return

        all_objs = storage.all()

        count = 0
        for obj in all_objs.values():
            if class_name == obj.__class__.__name__:
                count += 1

        print(count)

    def default(self, line):
        """
        Define custom methods with no command prefix

        The custom commands are:
            - <class name>.count()
            - <class name>.show(<id>)
            - <class name>.destroy(<id>)
            - <class name>.update(<id>, <attribute name>, <attribute value>)
            - <class name>.update(<id>, <dictionary representation>)
        """

        # --------------Initialisations------------------
        # Initialise the needed variables
        class_name = ""
        obj_id = ""
        attr_key = ""
        attr_value = ""
        args = ""

        # ----------Parsing-------------
        # Get the class name, the method and the passed argument(s) if any
        if "." in line:
            class_name, method_args = line.split('.')
        else:
            return super().default(line)

        method = re.findall(r'(^.+?)\(', method_args)
        # Get method as string
        if method:
            method = method[0]
        else:
            return super().default(line)

        args_in_list = re.findall(r'\((.+?)\)', method_args)
        # Get the arguments in the return list as a set of strings
        arg_len = len(args_in_list)
        if arg_len != 0:
            args = args_in_list[0]
            # Split them
            args = args.split(", ")
            args_num = len(args)

            if args_num >= 1:
                obj_id = args[0].replace('"', "")

        # ------------Execution---------------
        # Execute on the given class the given method
        if method == "count":
            self.do_count(class_name)
        elif method in ("show", "destroy"):

            args = f'{class_name} {obj_id}'

            if method == "show":
                self.do_show(args)
            else:
                self.do_destroy(args)
        elif method == "update":
            update_dict_list = re.findall(r'\{(.+?)\}', method_args)
            if update_dict_list:
                update_dict = update_dict_list[0]
                # Split the content of the dictionary by key/value
                update_dict = update_dict.split(",")
                # Get the number of attributes in the dict
                dict_len = len(update_dict)

                turn = dict_len
                index = 0
                while (turn > 0 and index < dict_len):
                    # Get the key-value pair
                    key_value = update_dict[index]
                    # Split them
                    key_value = key_value.split(": ")

                    key = ""
                    value = ""

                    # Confirm if valid key-value pair is input
                    if key_value:
                        if key_value[0]:
                            key = key_value[0]
                        if len(key_value) > 1:
                            value = key_value[1]

                    attr_key = key.replace("'", "")
                    attr_value = value.replace("'", "")

                    args = f'{class_name} {obj_id} {attr_key} {attr_value}'
                    self.do_update(args)

                    turn -= 1
                    index += 1
            else:
                if len(args) >= 2:
                    attr_key = args[1].replace("'", "")
                if len(args) >= 3:
                    attr_value = args[2].replace("'", "")

                args = f'{class_name} {obj_id} {attr_key} {attr_value}'
                self.do_update(args)
        else:
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
