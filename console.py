#!/usr/bin/python3
"""This program defines a command interpreter for the HBnB console"""


import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines attributes and methods for the HBnB console"""
    prompt = "(hbnb) "
    classes = {
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel"""
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
        """Show command to print string representation of an instance"""
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
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy command to delete an instance"""
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
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """All command to print string representation of all instances"""
        from models import storage
        if arg == "":
            print([str(obj) for obj in storage.all().values()])
        elif arg == "BaseModel":
            print([str(obj) for obj in storage.all().values()])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update command to update an instance"""
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
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all():
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(storage.all()[key], args[2], args[3])
                        storage.all()[key].save()
                else:
                    print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def do_help(self, arg):
        """Help command to show available commands"""
        cmd.Cmd.do_help(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
