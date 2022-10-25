#!/usr/bin/python3
import cmd
import readline


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        quit()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()


