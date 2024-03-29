# Skunk Works
```
                         _..._ ___
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
                    CODE REPOSITORY |:::/`-:::::;;-._ |:::::/::/
                                    |:::|  `-::::\   `|::::/::/
                                    |:::|     \:::\   \:::/::/
                                   /:::/       \:::\   \:/\:/
                                  (_::/         \:::;__ \\_\\___
                                  (_:/           \::):):)\:::):):)
                                   `"             `""""`  `""""""`   
```
# **The Repository**
- **Python**
  - [Skunkworks UI](#skunkworks-ui)
# **Python**
Install the `skunkworks-repo` package using PIP:
```
pip install skunkworks-repo
```
***

## **Skunkworks UI**
**Source Code: [`cli.py`](skunkworks_ui/cli.py) | [`style.py`](skunkworks_ui/style.py)**

```python
# Import

from skunkworks_ui.cli import Menu
from skunkworks_ui.style import *
```

```python
# Use the `style` module to stylize text
# ex. font(text, color, background, style)

styledText = font('Skunkworks UI', 'green', 'white', 'bold')
print(styledText)
```

```python
# Use the `cli` module to construct a comman-line menu
# ex. Menu(title, options)

menu_title = 'Skunkworks UI'

menu_options = {
                '1': 'Bold blue text',
                '2': 'Red text, white Background',
                'Q': 'Quit'
                }

menu = Menu(menu_title, menu_options)
menu.display()
user_input = menu.get_input()
```

```python
# Use the `cli` and `style` modules to create menu themes

menu_title = green_font(title('Skunkworks UI'))

menu_options = { 
                cyan_font('1'): 'Bold blue text',
                cyan_font('2'): 'Red text, white Background',
                cyan_font('Q'): 'Quit'
              }

menu = Menu(menu_title, menu_options)
menu.display()
user_input = menu.get_input(prompt('Select an option : '))
```

```python
# Then add menu logic

if user_input.lower() == '1':
    print(font('Bold blue text', 'blue', bold=True))
elif user_input.lower() == '2':
    print(font('Red text, white Background', 'red', 'white'))
elif user_input.lower() == 'q':
    menu.quit()
```

***
