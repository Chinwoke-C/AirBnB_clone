#!/usr/bin/python3


import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """hbnb console """
    prompt = "(hbnb) "
    object = {
        'BaseModel': BaseModel
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
        """ """
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
        """ """
        tok = args.split()
        if args == "" or tok[0] in HBNBCommand.object.keys():
            all_objs = storage.all()
            str_rep = [(str(all_objs[obj_id])) for obj_id in all_objs.keys()]
            print(str_rep)
        else:
            print("** class doesn't exist **")
    
    def do_update(self, args):
        """ """
        pass
    
    def default(self, args):
        """ """
        pass
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
