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
  SKUNK-INK                      \:::.  `:_|.-"`"-.    \__.-'/::\  |
░▒█▀▀▀█░▒█░▄▀░▒█░▒█░▒█▄░▒█░▒█░▄▀  '::::.:::...:::. '.       /:::|  |
░░▀▀▀▄▄░▒█▀▄░░▒█░▒█░▒█▒█▒█░▒█▀▄░   '::/::::::::::::. '-.__.:::::|  |
░▒█▄▄▄█░▒█░▒█░░▀▄▄▀░▒█░░▀█░▒█░▒█     |::::::::::::\::..../::::::| /
                                     |:::::::::::::|::::/::::::://
  ░▒█░░▒█░▒█▀▀▀█░▒█▀▀▄░▒█░▄▀░▒█▀▀▀█  \:::::::::::::|'::/::::::::/
  ░▒█▒█▒█░▒█░░▒█░▒█▄▄▀░▒█▀▄░░░▀▀▀▄▄  /\::::::::::::/  /:::::::/:|
  ░▒▀▄▀▄▀░▒█▄▄▄█░▒█░▒█░▒█░▒█░▒█▄▄▄█ |::';:::::::::/   |::::::/::;
     HANDSHAKE PYTHON WRAPPER (hsw) |:::/`-:::::;;-._ |:::::/::/
                                    |:::|  `-::::\   `|::::/::/
                                    |:::|     \:::\   \:::/::/
                                   /:::/       \:::\   \:/\:/
                                  (_::/         \:::;__ \\_\\___
                                  (_:/           \::):):)\:::):):)
                                   `"             `""""`  `""""""`      
"""

import requests

class hsd:

    API_KEY = ''
    ADDRESS = ''
    PORT = ''

    def __init__(self, _api_key:str, _address:str, _port:int=12039):
        """
        Description:

            Initialization of the hsw class
        
        Params:

        (*) Denotes required argument

        (*) _api_key : HSW API key.

        (*) _address : HSW node ip.

        (*) _port    : HSW node port.
        """
        global API_KEY
        global ADDRESS
        global PORT

        API_KEY = _api_key
        ADDRESS = _address
        PORT = str(_port)
    ### END METHOD ################################### __init__(self, _api_key:str, _address:str, _port:int=12037)

    def get(self, _endpoint:str):
        """
        Description:

            GET (json) response from API
        
        Params:

        (*) Denotes required argument

        (*) _endpoint     : API endpoint to send GET request.
        """

        url = "http://x:" + API_KEY + "@" + ADDRESS + ":" + PORT + _endpoint
        getResponse = requests.get(url)
        response = getResponse.json()
        return response # Return as json
    ### END METHOD ################################### get(self, _endpoint:str)

    def post(self, _endpoint:str, _post_message:str):
        """
        Description:

            POST (json) message to API
        
        Params:

        (*) Denotes required argument

        (*) _endpoint     : API endpoint to send POST message.

        (*) _post_message : Message to be sent.
        """
        
        url = "http://x:" + API_KEY + "@" + ADDRESS + ":" + PORT + _endpoint
        postRequest = requests.post(url, _post_message)
        response = postRequest.json()
        return response # Return as json
    ### END METHOD ################################### post(self, _endpoint:str, _post_message:str)