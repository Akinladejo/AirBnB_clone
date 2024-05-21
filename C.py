#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def default(self, line):
        """Catch commands if nothing else matches then."""
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        match = re.match(r"^(\w*)\.(\w+)\(([^)]*)\)$", line)
        if not match:
            return line

        classname, method, args = match.groups()
        uid, attr_or_dict = None, None

        match_uid_and_args = re.match(r'^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid, attr_or_dict = match_uid_and_args.groups()

        if method == "update" and attr_or_dict:
            match_dict = re.match(r'^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""

            match_attr_and_value = re.match(r'^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr, value = match_attr_and_value.groups()
                attr_or_dict = (attr or "") + " " + (value or "")

        command = f"{method} {classname} {uid} {attr_or_dict or ''}"
        self.onecmd(command.strip())
        return command

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s_dict = s_dict.replace("'", '"')
        d = json.loads(s_dict)
        key = f"{classname}.{uid}"

        if classname not in storage.classes():
            print("** class doesn't exist **")
        elif key not in storage.all():
            print("** no instance found **")
        else:
            obj = storage.all()[key]
            attributes = storage.attributes()[classname]
            for attr, value in d.items():
                if attr in attributes:
                    value = attributes[attr](value)
                setattr(obj, attr, value)
            obj.save()

    def do_EOF(self, line):
        """Handles End Of File character."""
        print()
        return True

    def do_quit(self, line):
        """Exits the program."""
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass

    def do_create(self, line):
        """Creates an instance."""
        if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            obj = storage.classes()[line]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance."""
        if not line:
            print("** class name missing **")
        else:
            words = line.split()
            classname, uid = words[0], words[1] if len(words) > 1 else None
            key = f"{classname}.{uid}"

            if classname not in storage.classes():
                print("** class doesn't exist **")
            elif not uid:
                print("** instance id missing **")
            elif key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        if not line:
            print("** class name missing **")
        else:
            words = line.split()
            classname, uid = words[0], words[1] if len(words) > 1 else None
            key = f"{classname}.{uid}"

            if classname not in storage.classes():
                print("** class doesn't exist **")
            elif not uid:
                print("** instance id missing **")
            elif key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances."""
        if line:
            if line not in storage.classes():
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in storage.all().values() if obj.__class__.__name__ == line])
        else:
            print([str(obj) for obj in storage.all().values()])

    def do_count(self, line):
        """Counts the instances of a class."""
        if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            count = sum(1 for key in storage.all() if key.startswith(f"{line}."))
            print(count)

    def do_update(self, line):
        """Updates an instance by adding or updating attribute."""
        if not line:
            print("** class name missing **")
            return

        match = re.match(r'^(\S+)\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(\S+)))?)?', line)
        if not match:
            print("** class name missing **")
            return

        classname, uid, attr, value = match.groups()
        key = f"{classname}.{uid}"

        if classname not in storage.classes():
            print("** class doesn't exist **")
        elif not uid:
            print("** instance id missing **")
        elif key not in storage.all():
            print("** no instance found **")
        elif not attr:
            print("** attribute name missing **")
        elif not value:
            print("** value missing **")
        else:
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            else:
                try:
                    value = int(value) if '.' not in value else float(value)
                except ValueError:
                    pass

            obj = storage.all()[key]
            attributes = storage.attributes().get(classname, {})
            if attr in attributes:
                value = attributes[attr](value)
            setattr(obj, attr, value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
