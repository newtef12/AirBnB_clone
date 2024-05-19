#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Command processor for the HBNB console."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)."""
        print()  # To ensure the prompt goes to the next line
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_help(self, arg):
        """List available commands with 'help' or detailed help with 'help <command>'."""
        return super().do_help(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
