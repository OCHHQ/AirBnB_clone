#!/usr/bin/python3
"""
Console module
Defines the command interpreter for the AirBnB clone project.
"""

import cmd

class AirBnBConsole(cmd.Cmd):
    """Command interpreter for the AirBnB clone project"""

    prompt = "(hbnb) "

    def do_help(self, arg):
        """Show help message for the specified command"""
        cmd.Cmd.do_help(self, arg)

    def do_quit(self, arg):
        """Quit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter"""
        print("")  # Print a newline for cleaner output
        return True

if __name__ == "__main__":
    AirBnBConsole().cmdloop()
