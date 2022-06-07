"""                      _..._ ___
                       .:::::::.  `"-._.-''.
                  ,   /:::::::::\     ':    \                     _._
                  \:-::::::::::::\     :.    |     /|.-'         /:::\ 
                   \::::::::\:::::|    ':     |   |  /           |:::|
                    `:::::::|:::::\     ':    |   `\ |    __     |\::/\ 
                       -:::-|::::::|    ':    |  .`\ .\_.'  `.__/      |
                            |::::::\    ':.   |   \ ';:: /.-._   ,    /
                            |:::::::|    :.   /   ,`\;:: \'./0)  |_.-/
                            ;:::::::|    ':  |    \.`;::.   ``   |  |
                             \::::::/    :'  /     _\::::'      /  /
                              \::::|   :'   /    ,=:;::/           |
                               \:::|   :'  |    (='` //        /   |
                                \::\   `:  /     '--' |       /\   |
  GITHUB.COM/SKUNK-INK           \:::.  `:_|.-"`"-.    \__.-'/::\  |
░▒█▀▀▀█░▒█░▄▀░▒█░▒█░▒█▄░▒█░▒█░▄▀  '::::.:::...:::. '.       /:::|  |
░░▀▀▀▄▄░▒█▀▄░░▒█░▒█░▒█▒█▒█░▒█▀▄░   '::/::::::::::::. '-.__.:::::|  |
░▒█▄▄▄█░▒█░▒█░░▀▄▄▀░▒█░░▀█░▒█░▒█     |::::::::::::\::..../::::::| /
                                     |:::::::::::::|::::/::::::://
  ░▒█░░▒█░▒█▀▀▀█░▒█▀▀▄░▒█░▄▀░▒█▀▀▀█  \:::::::::::::|'::/::::::::/
  ░▒█▒█▒█░▒█░░▒█░▒█▄▄▀░▒█▀▄░░░▀▀▀▄▄  /\::::::::::::/  /:::::::/:|
  ░▒▀▄▀▄▀░▒█▄▄▄█░▒█░▒█░▒█░▒█░▒█▄▄▄█ |::';:::::::::/   |::::::/::;
             COMMAND LINE INTERFACE |:::/`-:::::;;-._ |:::::/::/
                                    |:::|  `-::::\   `|::::/::/
                                    |:::|     \:::\   \:::/::/
                                   /:::/       \:::\   \:/\:/
                                  (_::/         \:::;__ \\_\\___
                                  (_:/           \::):):)\:::):):)
                                   `"             `""""`  `""""""`      
"""

import os
from getpass import getpass

class Menu:
    def __init__(self, title, options):
        """
        DESCRIPTION:
        
            This function is used to initialize the Menu class.
        
        PARAMETERS:
            (*) Denotes a required parameter.
            
            (*) title   : The title of the menu.
            (*) options : The options to be displayed.
        """
        self.clear_screen()
        self.title = title
        self.options = options
        ############################################################ END: __init__(self, title, options)

    def display(self):
        """
        DESCRIPTION:
        
            This function is used to display the menu.
            
        PARAMETERS:
            
            None.
        """
        print('    ' + self.title + '\n')
        for i, option in enumerate(self.options):
            print(f'\t{i + 1} : {option}')
        
        print()
        ############################################################ END: display(self)

    def get_input(self, prompt:str=None):
        """
        DESCRIPTION:
        
            This function is used to get the user's input.
            
        PARAMETERS:
        
            None.
        """
        if prompt == None:
            choice = input('    Enter your choice: ')
        else:
            choice = input('    ' + prompt)

        return choice
        ############################################################ END: get_input(self)

    def get_input_pass(self, prompt:str=None):
        """
        DESCRIPTION:
        
            This function is used to get the user's password.
            
        PARAMETERS:
        
            None.
        """
        if prompt == None:
            choice = getpass('    Enter your password: ')
        else:
            choice = getpass('    ' + prompt)

        return choice
        ############################################################ END: get_input_pass(self)

    def run(self):
        """
        DESCRIPTION:

            This function is used to run the menu.
            
        PARAMETERS:
        
            None.
        """
        self.display()
        choice = self.get_input()
        if choice == 'q':
            self.clear_screen()
            exit()
        elif choice.isdigit():
            self.clear_screen()
            return self.options[int(choice) - 1]
        else:
            self.clear_screen()
            return self.run()
        ############################################################ END: run(self)

    def clear_screen(self):
        """
        DESCRIPTION:
        
            This function is used to clear the screen.
            
        PARAMETERS:
        
            None.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        ############################################################ END: clear_screen(self)