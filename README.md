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
  SKUNK-INK                      \:::.  `:_|.-"`"-.    \__.-'/::\  |
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
## **Python**

***

### **Handshake API Python Wrapper** [(View Source)](python/handshake.py)

```python
from skunkworks.python.handshake import hsd, hsw

# Used default ip and port

hsd_api = hsd('api-key')
hsw_api = hsw('api-key')

# Or specify

hsd_api = hsd('api-key', '0.0.0.0', 14037)
hsw_api = hsw('api-key', '0.0.0.0', 14039)

# Then use

response = hsd_api.getInfo()
print(response)

response = hsw_api.resetAuthToken('primary', 'secret123')

```
> *For more information on using the Handshake API, visit the **[Handshake API Docs](https://hsd-dev.org/api-docs/#introduction)***


### **Initialization Defaults**
 - **`hsd`**
   - _ipaddress = `'127.0.0.1'`
   - _port = `12037`
 - **`hsw`**
   - _ipaddress = `'127.0.0.1'`
   - _port = `12039`

***