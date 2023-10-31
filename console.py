#!/usr/bin/python3
"""This program defines a command interpreter for the HBnB console"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it (to the JSON file)
        and print the id."""
        if arg == "":
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            from models.base_model import BaseModel
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id."""
        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                from models import storage
                objects = storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the
        change into the JSON file)."""
        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                from models import storage
                objects = storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key in objects:
                    del objects[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not
        on the class name."""
        from models import storage
        objects = storage.all()
        if arg == "":
            print([str(v) for v in objects.values()])
        elif arg == "BaseModel":
            print([str(v) for k, v in objects.items() if "BaseModel" in k])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)."""
        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                from models import storage
                objects = storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key in objects:
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objects[key], args[2], args[3])
                        storage.save()
                else:
                    print("** no instance found **")

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
