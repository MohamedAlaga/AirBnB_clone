#!/bin/usr/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        exit the program
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        if arg == "":
            print("** class name missing **")
        elif arg != "BaseModel" and arg != "User" and arg != "State" and arg != "City" and arg != "Amenity" and arg != "Place" and arg != "Review":
            print("** class doesn't exist **")
        else:
            if arg == "BaseModel":
                new = BaseModel()
            elif arg == "User":
                new = User()
            elif arg == "State":
                new = State()
            elif arg == "City":
                new = City()
            elif arg == "Amenity":
                new = Amenity()
            elif arg == "Place":
                new = Place()
            elif arg == "Review":
                new = Review()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] != "BaseModel" and args[0] != "User" and args[0] != "State" and args[0] != "City" and args[0] != "Amenity" and args[0] != "Place" and args[0] != "Review":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] != "BaseModel" and args[0] != "User" and args[0] != "State" and args[0] != "City" and args[0] != "Amenity" and args[0] != "Place" and args[0] != "Review":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        if arg == "":
            print([str(value) for key, value in storage.all().items()])
        else:
            args = arg.split()
            if args[0] != "BaseModel" and args[0] != "User" and args[0] != "State" and args[0] != "City" and args[0] != "Amenity" and args[0] != "Place" and args[0] != "Review":
                print("** class doesn't exist **")
            else:
                print([str(value) for key, value in storage.all().items()])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into
        the JSON file).
        """
        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] != "BaseModel" and args[0] != "User" and args[0] != "State" and args[0] != "City" and args[0] != "Amenity" and args[0] != "Place" and args[0] != "Review":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    obj = storage.all()[key]
                    attr_name = args[2]
                    attr_value = args[3]
                    try:
                        attr_value = eval(attr_value)
                    except:
                        pass
                    setattr(obj, attr_name, attr_value)
                    obj.save()
                else:
                    print("** no instance found **")
if __name__ == '__main__':
    HBNBCommand().cmdloop()