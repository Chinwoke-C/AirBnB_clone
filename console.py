#!/usr/bin/python3


import cmd

class HBNBCommand(cmd.Cmd):
    """ """
    prompt = ">>> "

    def quit(self, args):
        return True
    
    def EOF(self, args):
        """ """
        print()
        return True
    
    def emptyline(self, args):
        """ """
        pass
    
    def create(self, args):
        pass
    
    def destory(self, args):
        """ """
        pass
    
    def show(self, args):
        """ """
        pass
    
    def all(self, args):
        """ """
        pass
    
    def update(self, args):
        """ """
        pass
    
    def default(self, args):
        """ """
        pass
    


    # if __name__ == '__main__':
    #     HBNBCommand().cmdloop()
