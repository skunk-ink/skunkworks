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
              HANDSHAKE API WRAPPER |:::/`-:::::;;-._ |:::::/::/
                                    |:::|  `-::::\   `|::::/::/
                                    |:::|     \:::\   \:::/::/
                                   /:::/       \:::\   \:/\:/
                                  (_::/         \:::;__ \\_\\___
                                  (_:/           \::):):)\:::):):)
                                   `"             `""""`  `""""""`      
"""

import os
import sys
from getpass import getpass
from time import sleep

if sys.platform == 'win32':
    from msvcrt import getch as pause
elif sys.platform == 'linux':
    from getch import getch as pause

class Menu:
    def __init__(self, title:str, options:dict):
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
        self.clear_screen()
        print('    ' + self.title + '\n')
        for option in self.options:
            if option == 'space' or option == '':
                print('')
            else:
                print('\t' + str(option) + ': ' + self.options[option])
        
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

    def clear_screen(self):
        """
        DESCRIPTION:
        
            This function is used to clear the screen.
            
        PARAMETERS:
        
            None.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        ############################################################ END: clear_screen(self)

    def pause(self):
        """
        DESCRIPTION:
        
            This function is used to pause the menu.
            
        PARAMETERS:
        
            None.
        """
        pause()
        ############################################################ END: pause(self)

    def wait(self, seconds:int):
        """
        DESCRIPTION:
        
            This function is used to wait for a certain amount of time.
            
        PARAMETERS:
        
            None.
        """
        sleep(seconds)
        ############################################################ END: wait(self)

    def quit(self):
        """
        DESCRIPTION:
        
            This function is used to quit the menu.
            
        PARAMETERS:
        
            None.
        """
        self.clear_screen()
        sys.exit(0)
        ############################################################ END: quit(self)