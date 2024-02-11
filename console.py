#!/usr/bin/python3


import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """hbnb console """
    prompt = "(hbnb) "
    object = {
        'BaseModel': BaseModel, "User": User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State
        }
    def do_quit(self, args):
        """ This command ends the program """
        return True
    
    def do_EOF(self, args):
        """ End of file (exits the program) """
        print()
        return True
    
    def do_emptyline(self, args):
        """ This print a new line after the promth """
        pass
    
    def do_create(self, args):
        """ This creates a new instance of the BaseModel """
        if args == "":
            print("** class name missing **")
        elif args in HBNBCommand.object.keys():
            myModel = HBNBCommand.object[args]()
            myModel.save()
            print(myModel.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ prints the string representation of an instance based on the class name and id. """

        tok = args.split()
        if args == "":
            print("** class name missing **")
        elif tok[0] in HBNBCommand.object.keys():
            if len(tok) < 2:
                print("** instance id missing **")
                return False
            all_objects = storage.all()
            object_id = '{} {}'.format(tok[0], tok[1])
            if object_id not in all_objects.keys():
                print("** no instance found **")
            else:
                print(f"{all_objects[object_id]}")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """ Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        tok = args.split()
        if args == '':
            print("** class name missing **")
        elif tok[0] in HBNBCommand.object.keys():
            if len(tok) < 2:
                print("** instance id missing **")
                return False
            all_objects = storage.all()
            object_id = '{} {}'.format(tok[0], tok[1])
            if object_id not in all_objects.keys():
                print("** no instance found **")
            else:
                del all_objects[object_id]
                storage.save()
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """ Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        tok = args.split()
        if args == "" or tok[0] in HBNBCommand.object.keys():
            all_objs = storage.all()
            str_rep = [(str(all_objs[obj_id])) for obj_id in all_objs.keys()]
            print(str_rep)
        else:
            print("** class doesn't exist **")
    
    def do_update(self, args):
         """ Method to update JSON file"""
        args = args.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                if len(args) > 2:
                    if len(args) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            args[2],
                            arg[s3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')
    
    def default(self, args):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
