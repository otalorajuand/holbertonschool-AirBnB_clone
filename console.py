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


class HBNBCommand(cmd.Cmd):
    """This class implements a basic prompt to handle objects
    """

    prompt = '(hbnb) '

    class_id = {"User":"user", "BaseModel":"base_model", "State": "state", "City": "city",
            "Amenity":"amenity", "Place":"place", "Review":"review"}

    def do_create(self, line):
        """ Creates a new instance of BaseModel"""

        line_read = line.split(" ")
        if line_read == ['']:
            print("** class name missing **")
        elif line_read[0] not in HBNBCommand.class_id.keys():
            print("** class doesn't exist **")
        else:
            b1 = eval(f"models.{HBNBCommand.class_id[line_read[0]]}.{line_read[0]}()")
            b1.save()
            print(b1.id)
    
    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""

        line_read = line.split(" ")
        if line_read == ['']:
            print("** class name missing **")
        elif line_read[0] not in HBNBCommand.class_id.keys():
            print("** class doesn't exist **")
        elif len(line_read) < 2:
            print("** instance id missing **")
        elif not models.storage._FileStorage__objects.get(conct := line_read[0] + "." + line_read[1]):
            print("** no instance found **")
        else:
            obj = models.storage._FileStorage__objects[conct]
            print(obj)
            
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        line_read = line.split(" ")
        if line_read == ['']:
            print("** class name missing **")
        elif line_read[0] not in HBNBCommand.class_id.keys():
            print("** class doesn't exist **")
        elif len(line_read) < 2:
            print("** instance id missing **")
        elif not models.storage._FileStorage__objects.get(conct := line_read[0] + "." + line_read[1]):
            print("** no instance found **")

        else:
            del models.storage._FileStorage__objects[conct]
            models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""

        line_read = line.split(" ")
        if line_read[0] not in HBNBCommand.class_id.keys():
            print("** class doesn't exist **")
        else:
            list_to_print = []
            for key, value in models.storage._FileStorage__objects.items():
                if value.__class__.__name__ in HBNBCommand.class_id.keys() or line_read == ['']:
                    list_to_print.append(str(value))
            print(list_to_print)

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or updating attribute """

        line_read = line.split(' ')
        if line_read == ['']:
            print("** class name missing **")
        elif line_read[0] not in HBNBCommand.class_id.keys():
            print("** class doesn't exist **")
        elif len(line_read) < 2:
            print("** instance id missing **")
        elif not models.storage._FileStorage__objects.get(conct := line_read[0] + "." + line_read[1]):
            print("** no instance found **")
        elif len(line_read) < 3:
            print("** attribute name missing **")
        elif len(line_read) < 4:
            print("** value missing **")

        else:
            obj = models.storage._FileStorage__objects[conct]
            setattr(obj, line_read[2], eval(line_read[3]))

    def do_EOF(self, line):
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        quit()
        return True

    def emptyline(self):
        pass
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
