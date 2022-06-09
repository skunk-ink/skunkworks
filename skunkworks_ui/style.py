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
magenta_foreground = '\033[95m'
white_foreground = '\033[97m'
black_foreground = '\033[30m'
blue_foreground = '\033[94m'
cyan_foreground = '\033[96m'
green_foreground = '\033[92m'
yellow_foreground = '\033[93m'
red_foreground = '\033[91m'

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

def font(text:str, color:str = None, background:str = None, style:str = None, bold:bool = False, underline:bool = False, italic:bool = False):
    """
    DESCRIPTION:
        This function is used to create custom colored text.

    PARAMETERS:
        (*) Denotes a required parameter.

        (*) text       : The text to be colored.

        ( ) color      : The color of the text.
                            Options are: black, white, yellow, red, blue, green.

        ( ) background : The background color of the text.
                            Options: black, red, green, yellow, blue, magenta, cyan, white.

        ( ) style      : The style of the text.
                            Options: bold, underline, and italic.

        ( ) bold       : If the text should be bold.

        ( ) underline  : If the text should be underlined.

        ( ) italic     : If the text should be italic.
    """

    if color == 'white':
        text = white_foreground + text + endc
    elif color == 'red':
        text = red_foreground + text + endc
    elif color == 'green':
        text = green_foreground + text + endc
    elif color == 'blue':
        text = blue_foreground + text + endc
    elif color == 'yellow':
        text = yellow_foreground + text + endc
    elif color == 'cyan':
        text = cyan_foreground + text + endc
    elif color == 'magenta':
        text = magenta_foreground + text + endc
    elif color == 'black':
        text = black_foreground + text + endc
    
    if background == 'white':
        text = white_background + text + endc
    elif background == 'red':
        text = red_background + text + endc
    elif background == 'green':
        text = green_background + text + endc
    elif background == 'blue':
        text = blue_background + text + endc
    
    if style == 'bold' or bold:
        text = style_bold + text + endc
    elif style == 'underline' or underline:
        text = style_underline + text + endc
    elif style == 'italic' or italic:
        text = style_italic + text + endc
    
    return text
    ########################################################## END: font(color, text, background, style)


######################################################################
##                                                                  ##
##                            FONT COLORS                           ##
##                                                                  ##
######################################################################

def black_font(text):
    """
    DESCRIPTION:

        This function is used to create black text
    
    PARAMETERS:

        (*) Denotes a required parameter.

        (*) text : The text to be colored.
    """
    return black_foreground + text + endc
    ########################################################## END: black_font(text)
    
def white_font(text):
    """
    DESCRIPTION:

        This function is used to create white text
        
    PARAMETERS:
        (*) Denotes a required parameter.

        (*) text : The text to be colored.
    """
    return white_foreground + text + endc
    ########################################################## END: white_font(text)
    
def yellow_font(text):
    """
    DESCRIPTION:

        This function is used to create yellow text
    
    PARAMETERS:
        (*) Denotes a required parameter.

        (*) text : The text to be colored."""
    return yellow_foreground + text + endc
    ########################################################## END: yellow_font(text)
    
def red_font(text):
    """
    DESCRIPTION:

        This function is used to create red text

    PARAMETERS:
        (*) Denotes a required parameter.

        (*) text : The text to be colored.
    """
    return red_foreground + text + endc
    ########################################################## END: red_font(text)

def blue_font(text):
    """
    DESCRIPTION:

        This function is used to create blue text

    PARAMETERS:
        (*) Denotes a required parameter.

        (*) text : The text to be colored.
    """
    return blue_foreground + text + endc
    ########################################################## END: blue_font(text)
    
def green_font(text):
    """
    DESCRIPTION:
    
        This function is used to create green text
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return green_foreground + text + endc
    ########################################################## END: green_font(text)
    
def cyan_font(text):
    """
    DESCRIPTION:
    
        This function is used to create cyan text
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return cyan_foreground + text + endc
    ########################################################## END: cyan_font(text)
    
    
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

def bold_font(text):
    """
    DESCRIPTION:
    
        This function is used to create bold text.
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return style_bold + text + endc
    ########################################################## END: bold_font(text)
    
def underline_font(text):
    """
    DESCRIPTION:
    
        This function is used to create underlined text.
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return style_underline + text + endc
    ########################################################## END: underline_font(text)

def italic_font(text):
    """
    DESCRIPTION:
    
        This function is used to create italic text.
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return style_italic + text + endc
    ########################################################## END: italic_font(text)


##################################################################
##                                                              ## 
##                      CUSTOM FONT THEMES                      ##
##                                                              ##
##################################################################
def title_style(text):
    """
    DESCRIPTION:
    
        This function is used to create green menu titles.
    """
    return style_underline + style_bold + text + endc + endc
    ########################################################## END: title(text)
    
def prompt_style(text):
    """
    DESCRIPTION:
    
        This function is used to create yellow prompt text.
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    return yellow_foreground + style_bold + text + endc + endc
    ########################################################## END: prompt(text)
    
def error_style(text):
    """
    DESCRIPTION:
    
        This function is used to create red error text.
        
    PARAMETERS:
        (*) Denotes a required parameter.
        
        (*) text : The text to be colored.
    """
    text = ' ERROR : ' + text + ' '
    return red_background + white_foreground + text + endc + endc