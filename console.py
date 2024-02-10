#!/usr/bin/python3


import cmd

class HBNBCommand(cmd.Cmd):
    """hbnb console """
    prompt = "hbnb "

    def do_quit(self, args):
        """ This command ends the program """
        return True
    
    def do_EOF(self, args):
        """ End of file (exits the program) """
        print()
        return True
    
    def emptyline(self, args):
        """ This print a new line after the promth """
        pass
    
    def do_create(self, args):
        pass
    
    def do_destory(self, args):
        """ """
        pass
    
    def do_how(self, args):
        """ """
        pass
    
    def do_all(self, args):
        """ """
        pass
    
    def do_update(self, args):
        """ """
        pass
    
    def default(self, args):
        """ """
        pass
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
