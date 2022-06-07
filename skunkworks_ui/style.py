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

# FONT COLORS
magenta_fg = '\033[95m'
white_fg = '\033[97m'
black_fg = '\033[30m'
blue_fg = '\033[94m'
cyan_fg = '\033[96m'
green_fg = '\033[92m'
yellow_fg = '\033[93m'
red_fg = '\033[91m'

# FONT BACKGROUNDS
white_background = '\033[107m'
red_background = '\033[41m'
green_background = '\033[102m'
blue_background = '\033[44m'

# FONT STYLES
style_bold = '\033[1m'
style_underline = '\033[4m'
style_italic = '\033[3m'

# CUSTOM FONT STYLES
alert = '\033[1m\033[41m'

# ESCAPE SEQUENCE
endc = '\033[0m'

def font(text:str, color:str, background:str = None, style:str = None):
    """
    DESCRIPTION:
        This function is used to create custom colored text.

    PARAMETERS:
        (*) Denotes a required parameter.

        (*) text       : The text to be colored.

        (*) color      : The color of the text.
                            Options are: black, white, yellow, red, blue, green.

        ( ) background : The background color of the text.
                            Options: black, red, green, yellow, blue, magenta, cyan, white.

        ( ) style      : The style of the text.
                            Options: bold, underline, and italic.
    """

    if color == 'white':
        text = white_fg + text + endc
    elif color == 'red':
        text = red_fg + text + endc
    elif color == 'green':
        text = green_fg + text + endc
    elif color == 'blue':
        text = blue_fg + text + endc
    elif color == 'yellow':
        text = yellow_fg + text + endc
    elif color == 'cyan':
        text = cyan_fg + text + endc
    elif color == 'magenta':
        text = magenta_fg + text + endc
    elif color == 'black':
        text = black_fg + text + endc
    
    if background == 'white':
        text = white_background + text + endc
    elif background == 'red':
        text = red_background + text + endc
    elif background == 'green':
        text = green_background + text + endc
    elif background == 'blue':
        text = blue_background + text + endc
    
    if style == 'bold':
        text = style_bold + text + endc
    elif style == 'underline':
        text = style_underline + text + endc
    elif style == 'italic':
        text = style_italic + text + endc
    
    return text
    ########################################################## END: font(color, text, background, style)


######################################################################
##                                                                  ##
##                            FONT COLORS                           ##
##                                                                  ##
######################################################################

def black(text):
    """
    DESCRIPTION:

        This function is used to create black text
    
    PARAMETERS:

        (*) Denotes a required parameter.

        (*) text : The text to be colored.
    """
    return black_fg + text + endc
    ########################################################## END: black(text)
    
def white(text):
    """
    DESCRIPTION:

        This function is used to create white text
        
    PARAMETERS:
        (*) Denotes a required parameter.

        (*) text : The text to be colored.
    """
    return white_fg + text + endc
    ########################################################## END: white(text)
    
def yellow(text):
    """
    DESCRIPTION:

        This function is used to create yellow text
    
    PARAMETERS:
        (*) Denotes a required parameter.

        (*) text : The text to be colored."""
    return yellow_fg + text + endc
    ########################################################## END: yellow(text)
    
def red(text):
    """
    DESCRIPTION:

        This function is used to create red text

    PARAMETERS:
        (*) Denotes a required parameter.

        (*) text : The text to be colored.
    """
    return red_fg + text + endc
    ########################################################## END: red(text)

def blue(text):
    """
    DESCRIPTION:

        This function is used to create blue text

    PARAMETERS:
        (*) Denotes a required parameter.

        (*) text : The text to be colored.
    """
    return blue_fg + text + endc
    
def green(text):
    """
    DESCRIPTION:
    
        This function is used to create green text
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return green_fg + text + endc
    ########################################################## END: green(text)
    
def cyan(text):
    """
    DESCRIPTION:
    
        This function is used to create cyan text
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return cyan_fg + text + endc
    ########################################################## END: cyan(text)
    
    
##################################################################
##                                                              ##
##                       BACKGROUND COLORS                      ##
##                                                              ##
##################################################################

def white_bg(text):
    """
    DESCRIPTION:

        This function is used to create text with a white background.

    PARAMETERS:

        (*) Denotes a required parameter.

        (*) text : The text to be colored.
    """
    return white_background + text + endc
    ########################################################## END: white_bg(text)
    
def red_bg(text):
    """
    DESCRIPTION:
    
        This function is used to create text with a red background.
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return red_background + text + endc
    ########################################################## END: red_bg(text)

def green_bg(text):
    """
    DESCRIPTION:
    
        This function is used to create text with a green background.
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return green_background + text + endc
    ########################################################## END: green_bg(text)

def blue_bg(text):
    """
    DESCRIPTION:
    
        This function is used to create text with a blue background.
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return blue_background + text + endc
    ########################################################## END: blue_bg(text)
    

##################################################################
##                                                              ##
##                         FONT STYLES                          ##
##                                                              ##
##################################################################

def bold(text):
    """
    DESCRIPTION:
    
        This function is used to create bold text.
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return style_bold + text + endc
    ########################################################## END: bold(text)
    
def underline(text):
    """
    DESCRIPTION:
    
        This function is used to create underlined text.
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return style_underline + text + endc
    ########################################################## END: underline(text)

def italic(text):
    """
    DESCRIPTION:
    
        This function is used to create italic text.
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return style_italic + text + endc
    ########################################################## END: italic(text)


##################################################################
##                                                              ## 
##                      CUSTOM FONT THEMES                      ##
##                                                              ##
##################################################################
def title(text):
    """
    DESCRIPTION:
    
        This function is used to create green menu titles.
    """
    return green_fg + style_bold + text + endc + endc
    ########################################################## END: title(text)
    
def prompt(text):
    """
    DESCRIPTION:
    
        This function is used to create yellow prompt text.
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return yellow_fg + style_bold + text + endc + endc
    ########################################################## END: prompt(text)
    
def error(text):
    """
    DESCRIPTION:
    
        This function is used to create red error text.
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    text = ' ERROR : ' + text + ' '
    return red_background + white_fg + text + endc + endc