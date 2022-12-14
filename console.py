#!/usr/bin/python3
"""
This module contains the class HBNBCommand
"""
import cmd
import models.base_model
import models
import models.user
import models.city
import models.state
import models.amenity
import models.place
import models.review
import re


class HBNBCommand(cmd.Cmd):
    """This class implements a basic prompt to handle objects
    """

    prompt = '(hbnb) '

    class_id = {
        "User": "user",
        "BaseModel": "base_model",
        "State": "state",
        "City": "city",
        "Amenity": "amenity",
        "Place": "place",
        "Review": "review"}

    def do_create(self, line):
        """ Creates a new instance of BaseModel"""

        line_read = line.split(" ")
        if line_read == ['']:
            print("** class name missing **")
        elif line_read[0] not in HBNBCommand.class_id.keys():
            print("** class doesn't exist **")
        else:
            module = HBNBCommand.class_id[line_read[0]]
            b1 = eval(
                f"models.{module}.{line_read[0]}()")
            b1.save()
            print(b1.id)

    def do_show(self, line):
        """Prints the string representation of an
            instance based on the class name and id"""

        line_read = line.split(" ")
        if line_read == ['']:
            print("** class name missing **")
            return
        elif line_read[0] not in HBNBCommand.class_id.keys():
            print("** class doesn't exist **")
            return
        elif len(line_read) < 2:
            print("** instance id missing **")
            return

        conct = line_read[0] + "." + line_read[1]
        if not models.storage._FileStorage__objects.get(conct):
            print("** no instance found **")
        else:
            obj = models.storage._FileStorage__objects[conct]
            print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        line_read = line.split(" ")
        if line_read == ['']:
            print("** class name missing **")
            return
        elif line_read[0] not in HBNBCommand.class_id.keys():
            print("** class doesn't exist **")
            return
        elif len(line_read) < 2:
            print("** instance id missing **")
            return

        conct = line_read[0] + "." + line_read[1]
        if not models.storage._FileStorage__objects.get(conct):
            print("** no instance found **")

        else:
            del models.storage._FileStorage__objects[conct]
            models.storage.save()

    def do_all(self, line):
        """Prints all string representation of
        all instances based or not on the class name"""

        line_read = line.split(" ")
        if line_read[0] not in [*HBNBCommand.class_id.keys(), '']:
            print("** class doesn't exist **")
        else:
            list_to_print = []
            for value in models.storage._FileStorage__objects.values():
                if (value.__class__.__name__ == line_read[0] or
                        line_read == ['']):
                    list_to_print.append(str(value))
            print(list_to_print)

    def do_update(self, line):
        """ Updates an instance based on the class
            name and id by adding or updating attribute """

        line_read = line.split(' ')
        if line_read == ['']:
            print("** class name missing **")
            return
        elif line_read[0] not in HBNBCommand.class_id.keys():
            print("** class doesn't exist **")
            return
        elif len(line_read) < 2:
            print("** instance id missing **")
            return

        conct = line_read[0] + "." + line_read[1]
        if not models.storage._FileStorage__objects.get(conct):
            print("** no instance found **")
        elif len(line_read) < 3:
            print("** attribute name missing **")
        elif len(line_read) < 4:
            print("** value missing **")
        else:
            obj = models.storage._FileStorage__objects[conct]
            setattr(obj, line_read[2], eval(line_read[3]))

    def default(self, *args):
        splitted_args = args[0].split('.')
        if len(splitted_args) < 2:
            print("** incorrect command **")
            return

        if splitted_args[1] == "all()":
            self.do_all(f'{splitted_args[0]}')
        elif splitted_args[1] == "count()":

            classes = models.storage._FileStorage__objects.items()
            print(len([k for k, v in classes
                       if v.__class__.__name__ == splitted_args[0]]))
        elif re.search("show()", splitted_args[1]):
            object_id = splitted_args[1].replace("show(", "")[:-1]
            self.do_show(splitted_args[0] + " " + object_id)

        elif re.search("destroy()", splitted_args[1]):
            object_id = splitted_args[1].replace("destroy(", "")[:-1]
            self.do_destroy(splitted_args[0] + " " + object_id)
        elif re.search("update()", splitted_args[1]):
            object_args = splitted_args[1].replace("update(", "")[:-1]
            args = object_args.split(", ", 1)

            if len(args) < 2:
                print("** usage: <class name>.update(<id>,"
                      " <attribute name>, <attribute value>)")
            elif "{" in args[1] and "}" in args[1] and ":" in args[1]:
                dict_args = eval(args[1])
                for key, value in dict_args.items():
                    if type(value) is str:
                        s = f"{splitted_args[0]} {args[0]} {key} \"{value}\""
                    else:
                        s = f"{splitted_args[0]} {args[0]} {key} {value}"
                    self.do_update(s)
            else:
                object_args = object_args.replace(",", "")
                self.do_update(splitted_args[0] + " " + object_args)

    def do_EOF(self, line):
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
