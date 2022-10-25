#!/usr/bin/python3
"""
This module contains the class HBNBCommand
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class implements a basic prompt to handle objects
    """

    prompt = '(hbnb) '

    def do_EOF(self, line):
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        quit()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()


