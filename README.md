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
# **Python**
Install the `skunkworks-repo` package using PIP:
```
pip install skunkworks-repo
```


## **Handshake Wrapper** ( [`api.py`](handshake/api.py) )
> *For more information on using the Handshake API, visit the **[Handshake API Docs](https://hsd-dev.org/api-docs/#introduction)***

```python
from handshake import api

# Use default ip and port

hsd = api.hsd('api-key')
hsw = api.hsw('api-key')

# Or specify

hsd = api.hsd('api-key', '0.0.0.0', 14037)
hsw = api.hsw('api-key', '0.0.0.0', 14039)

# Then use

response = hsd.getInfo()
print(response)

response = hsw.resetAuthToken('primary', 'secret123')
print(response)

```

## **Skunkworks UI** ( [`cli.py`](skunkworks_ui/cli.py) | [`style.py`](skunkworks_ui/style.py) )

```python
# Import

from skunkworks_ui.cli import Menu
from skunkworks_ui.style import *

# Use the `style` module to stylize text
# ex. style.font(text, color, background, style)

print(font("Skunkworks UI", 'green', 'white', 'bold'))

# Use the `cli` module to construct a command-line menu

menu = Menu("Skunkworks UI", ["Test 1", "Test 2", "Test 3"])
menu.display()
user_input = menu.get_input("Press `ENTER` to continue...")

# Use both the `cli` and `style` modules to customize your menus

menu = Menu(font(underline("Skunkworks UI Styled"), 'green', style='bold'), [cyan("Test 1"), cyan("Test 2"), cyan("Test 3")])
menu.display()
user_input = menu.get_input(prompt("Press `ENTER` to quit..."))

```

***