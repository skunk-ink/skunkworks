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
           HANDSHAKE PYTHON WRAPPER |:::/`-:::::;;-._ |:::::/::/
                                    |:::|  `-::::\   `|::::/::/
                                    |:::|     \:::\   \:::/::/
                                   /:::/       \:::\   \:/\:/
                                  (_::/         \:::;__ \\_\\___
                                  (_:/           \::):):)\:::):):)
                                   `"             `""""`  `""""""`      
"""

import requests

API_KEY = ''
ADDRESS = ''

class hsd:

    PORT = ''

    def __init__(self, _api_key:str, _ipaddress:str='127.0.0.1', _port:int=12037):
        """
        Description:

            Initialization of the hsd class
        
        Params:

        (*) Denotes required argument

        (*) _api_key   : HSD API key.

        (*) _ipaddress : HSD node ip. Default = '127.0.0.1'.

        (*) _port      : HSD node port. Defualt = 12037
        """
        global API_KEY
        global ADDRESS
        global PORT

        API_KEY = _api_key
        ADDRESS = _ipaddress
        PORT = str(_port)
    ### END METHOD ################################### __init__(self, _api_key:str, _ipaddress:str='127.0.0.1', _port:int=12037)

    def get(self, _endpoint:str):
        """
        Description:

            GET (json) response from API
        
        Params:

        (*) Denotes required argument

        (*) _endpoint : API endpoint to send GET request.
        """

        url = "http://x:" + API_KEY + "@" + ADDRESS + ":" + PORT + _endpoint
        getResponse = requests.get(url)
        response = getResponse.json()
        return response # Returned as json
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
        return response # Returned as json
    ### END METHOD ################################### post(self, _endpoint:str, _post_message:str)

    def getInfo(self):
        """
        Description:

            Get server Info.
        
        Params:

            None
        """

        endpoint = '/'
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getInfo(self)

    def getMemPool(self):
        """
        Description:

            Get mempool snapshot (array of json txs).
        
        Params:

            None
        """
        
        endpoint = '/mempool'
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getMemPool(self)

    def getMemPoolInvalid(self, _verbose:bool=False):
        """
        Description:

            Get mempool rejects filter (a Bloom filter used to store rejected TX hashes).
        
        
        Params:

        (*) Denotes required argument

        ( ) _verbose : (bool) Returns entire Bloom Filter in filter property, hex-encoded.
        """

        if _verbose == True:
            endpoint = '/mempool/invalid?verbose=true'
        else:
            endpoint = '/mempool/invalid'

        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getMemPoolInvalid(self, _verbose:bool=False)

    def getMemPoolInvalidHash(self, _txhash:str):
        """
        Description:

            Test a TX hash against the mempool rejects filter.
        

        Params:

        (*) Denotes required argument
        
        (*) _txhash : Transaction hash.
        """
        
        endpoint = '/mempool/invalid/' + _txhash
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getMemPoolInvalidHash(self, _txhash:str)

    def getBlockHashOrHeight(self, _blockHashOrHeight:str):
        """
        Description:

            Returns block info by block hash or height.
        
        Params:

        (*) Denotes required argument
        
        (*) _blockHashOrHeight : Hash or Height of block.
        """
        
        endpoint = '/block/' + _blockHashOrHeight
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getBlockHashOrHeight(self, _blockHashOrHeight:str)

    def getHeaderHashOrHeight(self, _headerHashOrHeight:str):
        """
        Description:

            Returns block header by block hash or height.
        
        Params:

        (*) Denotes required argument
        
        (*) _headerHashOrHeight : Hash or Height of block.
        """
        
        endpoint = '/header/' + _headerHashOrHeight
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getHeaderHashOrHeight(self, _headerHashOrHeight:str)

    def postBroadcast(self, _tx:str):
        """
        Description:

            Broadcast a transaction by adding it to the node's mempool.
            If mempool verification fails, the node will still forcefully
            advertise and relay the transaction for the next 60 seconds.
        
        Params:

        (*) Denotes required argument
        
        (*) _tx : Raw transaction in hex.
        """
        
        endpoint = '/broadcast/'
        post_message = '{"tx": "' + _tx + '"}'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### postBroadcast(self, _tx:str)

    def postBroadcastClaim(self, _claim:str):
        """
        Description:

            Broadcast a claim by adding it to the node's mempool.
        
        Params:

        (*) Denotes required argument
        
        (*) _claim : Raw claim in hex.
        """
        
        endpoint = '/claim/'
        post_message = '{ "claim": "' + _claim + '" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### postBroadcastClaim(self, _claim:str)

    def getFeeEstimate(self, _blocks:int):
        """
        Description:

            Estimate the fee required (in dollarydoos per kB) for a
            transaction to be confirmed by the network within a targeted
            number of blocks (default 1).
        
        Params:

        (*) Denotes required argument
        
        (*) _blocks : Number of blocks to target confirmation.
        """
        
        endpoint = '/fee?blocks=' + str(_blocks)
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getFeeEstimate(self, _blocks:int)

    def postReset(self, _height:int):
        """
        Description:

            Triggers a hard-reset of the blockchain. All blocks are disconnected
            from the tip down to the provided height. Indexes and Chain Entries
            are removed. Useful for "rescanning" an SPV wallet. Since there are
            no blocks stored on disk, the only way to rescan the blockchain is to
            re-request [merkle]blocks from peers.
        
        Params:

        (*) Denotes required argument
        
        (*) _height : Block height to reset chain to.
        """
        
        endpoint = '/reset'
        post_message = '{ "height": ' + str(_height) + '}'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### postReset(self, _height:int)

    def getCoinByHashIndex(self, _txhash:str, _index:int):
        """
        Description:

            Get coin by outpoint (hash and index). Returns coin in hsd coin
            JSON format. value is always expressed in subunits.
        
        Params:

        (*) Denotes required argument
        
        (*) _txhash : Hash of tx.

        (*) _index  : Output's index in tx.
        """
        
        endpoint = '/coin/' + hash + '/' + _txhash + '/' + str(_index)
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getCoinByHashIndex(self, _txhash:str, _index:int)

    def getCoinByAddress(self, _address:str):
        """
        Description:

            Get coin objects array by address.
        
        Params:

        (*) Denotes required argument
        
        (*) _address : Handshake address.
        """
        
        endpoint = '/coin/address/' + _address
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getCoinByAddress(self, _address:str)

    def getTxByHash(self, _txhash:str):
        """
        Description:

           Returns transaction objects array by hash
        
        Params:

        (*) Denotes required argument
        
        (*) _txhash : Transaction hash.
        """
        
        endpoint = '/tx/' + _txhash
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getTxByHash(self, _txhash:str)

    def getTxByAddress(self, _address:str):
        """
        Description:

           Returns transaction objects array by address.
        
        Params:

        (*) Denotes required argument
        
        (*) _address : Handshake address.
        """
        
        endpoint = '/tx/address/' + _address
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getTxByAddress(self, _address:str)

    def rpc_postStop(self):
        """
        Description:

            Stops the running node.
        
        Params:

            None
        """
        
        endpoint = '/'
        post_message = '{ "method": "stop" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_postStop(self)

    def rpc_getInfo(self):
        """
        Description:

            Returns general info.
        
        Params:

            None 
        """
        
        endpoint = '/'
        post_message = '{ "method": "getinfo" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getInfo(self)

    def rpc_getMemoryInfo(self):
        """
        Description:

            Returns Memory usage info.
        
        Params:

            None
        """
        
        endpoint = '/'
        post_message = '{ "method": "getmemoryinfo" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getMemoryInfo(self)

    def rpc_setLogLevel(self, _params:str=['NONE']): # _params = ['NONE', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'SPAM']
        """
        Description:

            Change Log level of the running node.
        
        Params:

        (*) Denotes required argument
        
        (*) _params : Level for the logger as list array.
                      [ 'NONE', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'SPAM' ] 
        """
        
        endpoint = '/'
        post_message = '{ "method": "setloglevel", "params": [ "' + _params + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_setLogLevel(self, _params:str=['NONE'])

    def rpc_validateAddress(self, _address:str):
        """
        Description:

            Validates address.
        
        Params:

        (*) Denotes required argument
        
        (*) _address : Address to validate.
        """
        
        endpoint = '/'
        post_message = '{ "validateaddress": "", "params": [ "' + _address + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_validateAddress(self, _address:str)

    def rpc_createMultiSig(self, _nrequired:int, _keyDict:str):
        """
        Description:

            Create multisig address.
        
        Params:

        (*) Denotes required argument
        
        (*) _nrequired : Required number of approvals for spending.

        (*) _keyDict   : List array of public keys.
        """
        
        endpoint = '/'
        post_message = '{ "method": "createmultisig", "params": [ ' + str(_nrequired) + ', "' + _keyDict + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_createMultiSig(self, _nrequired:int, _keyDict:str)

    def rpc_signMessageWithPrivKey(self, _privkey:str, _message:str):
        """
        Description:

            Signs message with private key. 
        
        Params:
        (*) Denotes required argument
        
        (*) _privkey : Private key.

        (*) _message : Message you want to sign.
        """
        
        endpoint = '/'
        post_message = '{ "method": "signmessagewithprivkey", "params": [ "' + _privkey + '", "' + _message + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_signMessageWithPrivKey(self, _privkey:str, _message:str)

    def rpc_verifyMessage(self, _address:str, _signature:str, _message:str):
        """
        Description:

            Verify signature.
        
        Params:

        (*) Denotes required argument
        
        (*) _address   : Address of the signer.

        (*) _signature : Signature of signed message.

        (*) _message   : Message that was signed.
        """
        
        endpoint = '/'
        post_message = '{ "method": "verifymessage", "params": [ "' + _address + '", "' + _signature + '", "' + _message + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_verifyMessage(self, _address:str, _signature:str, _message:str)

    def rpc_verifyMessageWithName(self, _name:str, _signature:str, _message:str):
        """
        Description:

            Retrieves the address that owns a name and verifies signature.
        
        Params:

        (*) Denotes required argument
        
        (*) _name      : Name to retrieve the address used to sign.

        (*) _signature : Signature of signed message.

        (*) _message   : Message that was signed.
        """
        
        endpoint = '/'
        post_message = '{ "method": "verifymessagewithname", "params": [ "' + _name + '", "' + _signature + '", "' + _message + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_verifyMessageWithName(self, _name:str, _signature:str, _message:str)

    def rpc_setMockTime(self, _timestamp:int):
        """
        Description:

            Changes network time (This is consensus-critical)
        
        Params:

        (*) Denotes required argument
        
        (*) _timestamp : Timestamp to change to.
        """
        
        endpoint = '/'
        post_message = '{ "method": "setmocktime", "params": [ ' + str(_timestamp) + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_setMockTime(self, _timestamp:int)

    def rpc_pruneBlockchain(self):
        """
        Description:

            Prunes the blockchain, it will keep blocks specified in Network Configurations.
        
        Params:

            None
        """
        
        endpoint = '/'
        post_message = '{ "method": "pruneblockchain", "params": [] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_postPruneBlockchain(self)
    
    def rpc_invalidateBlock(self, _blockhash:str):
        """
        Description:

            Invalidates the block in the chain. It will rewind network to
            blockhash and invalidate it. It won't accept that block as valid.
            Invalidation will work while running,restarting node will remove
            invalid block from list.
        
        Params:
        
        (*) Denotes required argument
        
        (*) _blockhash : Block's hash.
        """
        
        endpoint = '/'
        post_message = '{ "method": "", "params": [ "' + _blockhash + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_invalidateBlock(self, _blockhash:str)
    
    def rpc_reconsiderBlock(self, _blockhash:str):
        """
        Description:

            This rpc command will remove block from invalid block set.
        
        Params:

        (*) Denotes required argument
        
        (*) _blockhash : Block's hash.
        """
        
        endpoint = '/'
        post_message = '{ "method": "reconsiderblock", "params": [ "' + _blockhash + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_reconsiderBlock(self, _blockhash:str)

    def rpc_getBlockchainInfo(self):
        """
        Description:

            Returns blockchain information.
        
        Params:

            None
        """
        
        endpoint = '/'
        post_message = '{ "method": "getblockchaininfo" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getBlockchainInfo(self)
    
    def rpc_getBestBlockHash(self):
        """
        Description:

            Returns Block Hash of the tip.
        
        Params:

            None
        """
        
        endpoint = '/'
        post_message = '{ "method": "getbestblockhash" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getBestBlockHash(self)
    
    def rpc_getBlockCount(self):
        """
        Description:

            Returns block count.
        
        Params:

            None
        """
        
        endpoint = '/'
        post_message = '{ "method": "getblockcount" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getBlockCount(self)
    
    def rpc_getBlock(self, _blockhash:str, _verbose:bool=True, _details:bool=False):
        """
        Description:

            Returns information about block.

        Params:

        (*) Denotes required argument
        
        (*) _blockhash : Hash of the block.

        ( ) _verbose   : (bool) If set to False, it will return hex of the block.

        ( ) _details   : (bool) If set to True, it will return transaction details too.
        """

        verbose = ''
        details = ''

        if _verbose == True:
            verbose = '1'
        else:
            verbose = '0'

        if _details == True:
            details = '1'
        else:
            details = '0'
        
        endpoint = '/'
        post_message = '{ "method": "getblock", "params": [ "' + _blockhash + '", ' + verbose + ', ' + details + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getBlock(self, _blockhash:str, _verbose:bool=True, _details:bool=False)
    
    def rpc_getBlockByHeight(self, _blockheight:int, _verbose:bool=True, _details:bool=False):
        """
        Description:

            Returns information about block by height.

        Params:

        (*) Denotes required argument
        
        (*) _blockheight : Height of the block in the blockchain.

        ( ) _verbose     : (bool) If set to True, it will return hex of the block.

        ( ) _details     : (bool) If set to True, it will return transaction details too.
        """

        verbose = ''
        details = ''

        if _verbose == True:
            verbose = '1'
        else:
            verbose = '0'

        if _details == True:
            details = '1'
        else:
            details = '0'
        
        endpoint = '/'
        post_message = '{ "method": "getblockbyheight", "params": [ ' + str(_blockheight) + ', ' + verbose + ', ' + details + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getBlockByHeight(self, _blockheight:int, _verbose:bool=True, _details:bool=False)
    
    def rpc_getBlockHash(self, _blockheight:int):
        """
        Description:

            Returns block's hash given its height.

        Params:

        (*) Denotes required argument
        
        (*) _blockheight : Height of the block in the blockchain.
        """
        
        endpoint = '/'
        post_message = '{ "method": "getblockhash", "params": [ ' + str(_blockheight) + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getBlockHash(self, _blockheight:int)
    
    def rpc_getBlockHeader(self, _blockhash:str, _verbose:bool=True):
        """
        Description:

            Returns a block's header given its hash.

        Params:

        (*) Denotes required argument
        
        (*) _blockhash : Hash of the block in the blockchain.

        ( ) _verbose   : If set to False, it will return (hex) of the block.
        """

        verbose = ''

        if _verbose == True:
            verbose = '1'
        else:
            verbose = '0'
        
        endpoint = '/'
        post_message = '{ "method": "getblockheader", "params": [ "' + _blockhash + '", ' + verbose + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getBlockHeader(self, _blockhash:str, _verbose:bool=True)
    
    def rpc_getChainTips(self):
        """
        Description:

            Returns chaintips.
        
        Params:

            None
        """
        
        endpoint = '/'
        post_message = '{ "method": "getchaintips" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getChainTips(self)
    
    def rpc_getDifficulty(self):
        """
        Description:

            Returns current difficulty level.
        
        Params:

            None
        """
        
        endpoint = '/'
        post_message = '{ "method": "getdifficulty" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getDifficulty(self)
    
    def rpc_getMemPoolInfo(self):
        """
        Description:

            Returns informations about mempool.
        
        Params:

            None
        """
        
        endpoint = '/'
        post_message = '{ "method": "getmempoolinfo" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getMemPoolInfo(self)
    
    def rpc_getMemPoolAncestors(self, _txhash:str, _verbose:bool=False):
        """
        Description:

            Returns all in-mempool ancestors for a transaction in the mempool.
        
        Params:

        (*) Denotes required argument
        
        (*) _txhash  : Transaction Hash.

        ( ) _verbose : False returns only tx hashs, true - returns dependency tx info.
        """

        verbose = ''

        if _verbose == True:
            verbose = '1'
        else:
            verbose = '0'
        
        endpoint = '/'
        post_message = '{ "method": "getmempoolancestors", "params": [ "' + _txhash + '", ' + verbose + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getMemPoolAncestors(self, _txhash:str, _verbose:bool=False)
    
    def rpc_getMemPoolDescendants(self, _txhash:str, _verbose:bool=False):
        """
        Description:

            Returns all in-mempool descendants for a transaction in the mempool.
        
        Params:

        (*) Denotes required argument
        
        (*) _txhash  : Transaction Hash.

        ( ) _verbose : False returns only tx hashs, true - returns dependency tx info.
        """

        verbose = ''

        if _verbose == True:
            verbose = '1'
        else:
            verbose = '0'
        
        endpoint = '/'
        post_message = '{ "method": "getmempooldescendants", "params": [ "' + _txhash + '", ' + verbose + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getMemPoolDescendants(self, _txhash:str, _verbose:bool=False)
    
    def rpc_getMemPoolEntry(self, _txhash:str):
        """
        Description:

            Returns mempool transaction info by its hash.
        
        Params:

        (*) Denotes required argument
        
        (*) _txhash : Transaction Hash.
        """
        
        endpoint = '/'
        post_message = '{ "method": "getmempoolentry", "params": [ "' + _txhash + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getMemPoolEntry(self, _txhash:str)
    
    def rpc_getRawMemPool(self, _verbose:bool=False):
        """
        Description:

            Returns mempool detailed information (on verbose). Or mempool tx list.
        
        Params:

        (*) Denotes required argument
        
        ( ) _verbose : False returns only tx hashs, true - returns full tx info.
        """

        verbose = ''

        if _verbose == True:
            verbose = '1'
        else:
            verbose = '0'
        
        endpoint = '/'
        post_message = '{ "method": "getrawmempool", "params": [ ' + verbose + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getRawMemPool(self, _verbose:bool=False)
    
    def rpc_prioritiseTransaction(self, _txhash:str, _priorityDelta:int, _feeDelta:int):
        """
        Description:

            Prioritises the transaction.

            Note: Changing fee or priority will only trick local miner (using this mempool) into
                accepting Transaction(s) into the block. (even if Priority/Fee doen't qualify)
        
        Params:

        (*) Denotes required argument
        
        (*) _txhash        : Transaction hash.

        (*) _priorityDelta : Virtual priority to add/subtract to the entry.

        (*) _feeDelta      : Virtual fee to add/subtract to the entry.
        """
        
        endpoint = '/'
        post_message = '{ "method": "prioritisetransaction", "params": [ "' + _txhash + '", "' + str(_priorityDelta) + '", "' + str(_feeDelta) + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_prioritiseTransaction(self, _txhash:str, _priorityDelta:int, _feeDelta:int)
    
    def rpc_estimateFee(self, _nblocks:int=1):
        """
        Description:

            Estimates fee to be paid for transaction.
        
        Params:

        (*) Denotes required argument
        
        ( ) _nblocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        post_message = '{ "method": "estimatefee", "params": [ ' + str(_nblocks) + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_estimateFee(self, _nblocks:int=1)
    
    def rpc_estimatePriority(self, _nblocks:int=1):
        """
        Description:

            Estimates the priority (coin age) that a transaction
            needs in order to be included within a certain number
            of blocks as a free high-priority transaction.
        
        Params:

        (*) Denotes required argument
        
        ( ) _nblocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        post_message = '{ "method": "estimatepriority", "params": [ ' + str(_nblocks) + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_estimatePriority(self, _nblocks:int=1)
    
    def rpc_estimateSmartFee(self, _nblocks:int=1):
        """
        Description:

            Estimates smart fee to be paid for transaction.
        
        Params:

        (*) Denotes required argument
        
        ( ) _nblocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        post_message = '{ "method": "estimatesmartfee", "params": [ ' + str(_nblocks) + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_estimateSmartFee(self, _nblocks:int=1)
    
    def rpc_estimateSmartPriority(self, _nblocks:int=1):
        """
        Description:

            Estimates smart priority (coin age) that a transaction
            needs in order to be included within a certain number
            of blocks as a free high-priority transaction.
        
        Params:

        (*) Denotes required argument
        
        (*) _nblocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        post_message = '{ "method": "estimatesmartpriority", "params": [ ' + str(_nblocks) + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_estimateSmartPriority(self, _nblocks:int=1)
    
    def rpc_getTxOut(self, _txhash:str, _index:int, _includemempool:int=1):
        """
        Description:

            Get outpoint of the transaction.
        
        Params:
        
        (*) Denotes required argument
        
        (*) _txhash         : Transaction hash.

        (*) _index          : Index of the outpoint tx.

        ( ) _includemempool : Whether to include mempool transactions.
        """
        
        endpoint = '/'
        post_message = '{ "method": "gettxout", "params": [ "' + _txhash + '", ' + str(_index) + ', ' + str(_includemempool) + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getTxOut(self, _txhash:str, _index:int, _includemempool:int=1)
    
    def rpc_getTxOutSetInfo(self):
        """
        Description:

            Returns information about UTXO's from Chain.
        
        Params:

            None
        """

        endpoint = '/'
        post_message = '{ "method": "gettxoutsetinfo", "params": [] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getTxOutSetInfo(self)
    
    def rpc_getRawTransaction(self, _txhash:str, _verbose:bool=False):
        """
        Description:

            Returns raw transaction
        
        Params:

        (*) Denotes required argument
        
        (*) _txhash  : Transaction hash.

        ( ) _verbose : Returns json formatted if true.
        """

        verbose = ''

        if _verbose == True:
            verbose = '1'
        else:
            verbose = '0'
        
        endpoint = '/'
        post_message = '{ "method": "getrawtransaction", "params": [ "' + _txhash + '", ' + verbose + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getRawTransaction(self, _txhash:str, _verbose:bool=False)
    
    def rpc_decodeRawTransaction(self, _rawtx:str):
        """
        Description:

            Decodes raw tx and provide chain info.
        
        Params:

        (*) Denotes required argument
        
        (*) _rawtx : Raw transaction hex.
        """
        
        endpoint = '/'
        post_message = '{ "method": "decoderawtransaction", "params": [ "' + _rawtx + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_decodeRawTransaction(self, _rawtx:str)
    
    def rpc_decodeScript(self, _script:str):
        """
        Description:

            Decodes script.
        
        Params:

        (*) Denotes required argument
        
        (*) _script : Script hex.
        """
        
        endpoint = '/'
        post_message = '{ "method": "decodescript", "params": [ "' + _script + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_decodeScript(self, _script:str)
    
    def rpc_sendRawTransaction(self, _rawtx:str):
        """
        Description:

            Sends raw transaction without verification.
        
        Params:

        (*) Denotes required argument
        
        (*) _rawtx : Raw transaction hex.
        """
        
        endpoint = '/'
        post_message = '{ "method": "sendrawtransaction", "params": [ "' + _rawtx + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_sendRawTransaction(self, _rawtx:str)
    
    def rpc_createRawTransaction(self, _txhash:str, _txindex:int, _address:str, _amount:int, _data:str):
        """
        Description:

            Creates raw, unsigned transaction without any formal verification.
        
        Params:

        (*) Denotes required argument
        
        (*) _txhash  : Transaction hash.

        (*) _txindex : Transaction outpoint index.

        (*) _address : Recipient address.

        (*) _amount  : Amount to send in HNS (float).
        """

        endpoint = '/'
        post_message = '{ "method": "createrawtransaction", "params": [[{ "txid": "' + _txhash + '", "vout": ' + str(_txindex) + ' }], { "' + _address + '": ' + str(_amount) + ', "data": "' + _data + '" }] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_createRawTransaction(self, _txhash:str, _txindex:int, _address:str, _amount:int, _data:str)
    
    def rpc_signRawTransaction(self, _rawtx:str, _txhash:str, _txindex:int, _address:str, _amount:int, _privkey:str):
        """
        Description:

            Creates raw, unsigned transaction without any formal verification.
        
        Params:

        (*) Denotes required argument
        
        (*) _rawtx   : Raw transaction.

        (*) _txhash  : Transaction hash.

        (*) _txindex : Transaction outpoint index.

        (*) _address : Address which received the output you're going to sign.

        (*) _amount  : Amount the output is worth.

        ( ) _privkey : List of private keys.
        """

        self.rpc_createRawTransaction()

        endpoint = '/'
        post_message = '{ "method": "signrawtransaction", "params": [ "' + _rawtx + '", [{ "txid": "' + _txhash + '", "vout": ' + str(_txindex) + ', "address": "' + _address + '", "amount": ' + str(_amount) + ' }], [ "' + _privkey + '" ]] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_signRawTransaction(self, _rawtx:str, _txhash:str, _txindex:int, _address:str, _amount:int, _privkey:str)
    
    def rpc_getTxOutProof(self, _txidlist:str):
        """
        Description:

            Checks if transactions are within block. Returns proof of transaction inclusion (raw MerkleBlock).
        
        Params:

        (*) Denotes required argument
        
        (*) _txidlist  : List array of transaction ID's
        """

        endpoint = '/'
        post_message = '{ "method": "gettxoutproof", "params": [ "' + _txidlist + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getTxOutProof(self, _txidlist:str)
    
    def rpc_verifyTxOutProof(self, _proof:str):
        """
        Description:

            Checks the proof for transaction inclusion. Returns transaction hash if valid.
        
        Params:

        (*) Denotes required argument
        
        (*) _proof : Proof of transaction inclusion (raw MerkleBlock).
        """

        endpoint = '/'
        post_message = '{ "method": "verifytxoutproof", "params": [ "' + _proof + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_verifyTxOutProof(self, _proof)
    
    def rpc_getNetworkHashPerSec(self, _blocks:int=120, _height:int=1):
        """
        Description:

            Returns the estimated current or historical network hashes per second, based on last blocks.
        
        Params:

        (*) Denotes required argument
        
        (*) _blocks : Number of blocks to lookup.
        
        (*) _height : Starting height for calculations.
        """

        endpoint = '/'
        post_message = '{ "method": "getnetworkhashps", "params": [ ' + str(_blocks) + ', ' + str(_height) + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getNetworkHashPerSec(self, _blocks:int=120, _height:int=1)
    
    def rpc_getMiningInfo(self):
        """
        Description:

            Returns mining info.

            Note: currentblocksize, currentblockweight, currentblocktx, difficulty are
                  returned when there's active work. generate - is true when hsd itself
                  is mining.
        
        Params:

            None
        """

        endpoint = '/'
        post_message = '{ "method": "getmininginfo", "params": [] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getMiningInfo(self)
    
    def rpc_getWork(self, _data:str=[]):
        """
        Description:

            Returns hashing work to be solved by miner. Or submits solved block.
        
        Params:

        (*) Denotes required argument
        
        (*) _data : Data to be submitted to the network.
        """

        endpoint = '/'
        post_message = '{ "method": "getworklp", "params": [ "' + _data + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getWorkLP(self)
    
    def rpc_getWorkLP(self):
        """
        Description:

            Long polling for new work.

            Returns new work, whenever new TX is received in the mempoolor new
            block has been discovered. So miner can restart mining on new data.
        
        Params:

            None
        """

        endpoint = '/'
        post_message = '{ "method": "getworklp", "params": [] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getWorkLP(self)
    
    def rpc_getBlockTemplate(self):
        """
        Description:

            Returns block template or proposal for use with mining. Also validates proposal if mode is specified as proposal.
        
        Params:

            None
        """

        endpoint = '/'
        post_message = '{ "method": "getblocktemplate", "params": [] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getBlockTemplate(self):
    
    def rpc_submitBlock(self, _blockdata:str):
        """
        Description:

            Adds block to chain.
        
        Params:

        (*) Denotes required argument
        
        (*) _blockdata : Mined block data (hex).
        """

        endpoint = '/'
        post_message = '{ "method": "submitblock", "params": [ "' + _blockdata + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_submitBlock(self, _blockdata:str)
    
    def rpc_verifyBlock(self, _blockdata:str):
        """
        Description:

            Verifies the block data.
        
        Params:
        (*) Denotes required argument
        
        (*) _blockdata : Mined block data (hex).
        """

        endpoint = '/'
        post_message = '{ "method": "verifyblock", "params": [ "' + _blockdata + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_verifyBlock(self, _blockdata:str)
    
    def rpc_setGenerate(self, _mining:int=0, _proclimit:int=0):
        """
        Description:

            Will start the mining on CPU.
        
        Params:

        (*) Denotes required argument
        
        (*) _mining    : 1 will start mining, 0 will stop.

        (*) _proclimit : 1 will set processor limit, 0 will remove limit.
        """

        endpoint = '/'
        post_message = '{ "method": "setgenerate", "params": [ ' + str(_mining) + ', ' + str(_proclimit) + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_setGenerate(self, _mining:int=0, _proclimit:int=0)
    
    def rpc_getGenerate(self):
        """
        Description:

            Returns status of mining on Node.
        
        Params:

            None
        """

        endpoint = '/'
        post_message = '{ "method": "getgenerate", "params": [] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getGenerate(self)
    
    def rpc_Generate(self, _numblocks:int=1):
        """
        Description:

            Mines numblocks number of blocks. Will return once all blocks are mined. CLI command may timeout before that happens.
        
        Params:
        (*) Denotes required argument
        
        (*) _numblocks : Number of blocks to mine.
        """

        endpoint = '/'
        post_message = '{ "method": "generate", "params": [' + str(_numblocks) + '] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_Generate(self, _numblocks:int=1)
    
    def rpc_GenerateToAddress(self, _address:str, _numblocks:int=1):
        """
        Description:

            Mines numblocks blocks, with address as coinbase.
        
        Params:

        (*) Denotes required argument
        
        (*) _address   : Coinbase address for new blocks.

        (*) _numblocks : Number of blocks to mine.
        """

        endpoint = '/'
        post_message = '{ "method": "generatetoaddress", "params": [ ' + str(_numblocks) + ', "' + _address + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_GenerateToAddress(self, _address:str, _numblocks:int=1)
    
    def rpc_getConnectionCount(self):
        """
        Description:

            Returns connection count.
        
        Params:

            None
        """

        endpoint = '/'
        post_message = '{ "method": "getconnectioncount", "params": [] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getConnectionCount(self)
    
    def rpc_ping(self):
        """
        Description:

            Will send ping request to every connected peer.
        
        Params:

            None
        """

        endpoint = '/'
        post_message = '{ "method": "ping", "params": [] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_ping(self)
    
    def rpc_getPeerInfo(self):
        """
        Description:

            Returns information about all connected peers.
        
        Params:

            None
        """

        endpoint = '/'
        post_message = '{ "method": "getpeerinfo", "params": [] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getPeerInfo(self)
    
    def rpc_addNode(self, _nodeAddress:str, _cmd:str):
        """
        Description:

            Adds or removes peers in Host List. 
        
        Params:

        (*) Denotes required argument
        
        (*) _nodeAddress : IP Address of the Node. Eg. '127.0.0.1:14038'

        (*) _cmd         : 'add' - Adds node to Host List and connects to it.

                           'onetry' - Tries to connect to the given node.

                           'remove' - Removes node from host list.
        """

        endpoint = '/'
        post_message = '{ "method": "addnode", "params": [ "' + _nodeAddress + '", "' + _cmd + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_addNode(self, _nodeAddress:str, _cmd:str)
    
    def rpc_disconnectNode(self, _nodeAddress:str):
        """
        Description:

            Disconnects node.
        
        Params:

        (*) Denotes required argument
        
        (*) _address : IP Address of the Node. Eg. '127.0.0.1:14038'
        """

        endpoint = '/'
        post_message = '{ "method": "disconnectnode", "params": [ "' + _nodeAddress + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_disconnectNode(self, _nodeAddress:str)
    
    def rpc_getAddedNodeInfo(self, _nodeAddress:str):
        """
        Description:

            Returns node information from host list.
        
        Params:

        (*) Denotes required argument
        
        (*) _address : IP Address of the Node. Eg. '127.0.0.1:14038'
        """

        endpoint = '/'
        post_message = '{ "method": "getaddednodeinfo", "params": [ "' + _nodeAddress + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getAddedNodeInfo(self, _nodeAddress:str)
    
    def rpc_getNetTotals(self):
        """
        Description:

            Returns information about used network resources.
        
        Params:

            None
        """

        endpoint = '/'
        post_message = '{ "method": "getnettotals", "params": [] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getNetTotals(self)
    
    def rpc_getNetworkInfo(self):
        """
        Description:

            Returns local node's network information.
        
        Params:

            None
        """

        endpoint = '/'
        post_message = '{ "method": "getnetworkinfo", "params": [] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### def rpc_getNetworkInfo(self)
    
    def rpc_setBan(self, _nodeAddress:str, _cmd:str):
        """
        Description:

            Adds or removes nodes from banlist.
        
        Params:

        (*) Denotes required argument
        
        (*) _nodeAddress : IP Address of the Node. Eg. '127.0.0.1:14038'

        (*) _cmd         : 'add' - Adds node to ban list, removes from host list, disconnects.

                           'remove' - Removes node from ban list.
        """

        endpoint = '/'
        post_message = '{ "method": "setban", "params": ["' + _nodeAddress + '", "' + _cmd + '"] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_setBan(self, _nodeAddress:str, _cmd:str)
    
    def rpc_listBan(self):
        """
        Description:

            Lists all banned peers.
        
        Params:

            None
        """

        endpoint = '/'
        post_message = '{ "method": "listbanned", "params": [] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_listBan(self)
    
    def rpc_clearBanned(self):
        """
        Description:

            Removes all banned peers.
        
        Params:

            None
        """

        endpoint = '/'
        post_message = '{ "method": "clearbanned", "params": [] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_clearBanned(self)
    
    def rpc_getNameInfo(self, _name:str):
        """
        Description:

            Returns information on a given name. Use this function to query any name in any state.
        
        Params:

        (*) Denotes required argument

        (*) _name : Name you wish to look up.
        """

        endpoint = '/'
        post_message = '{ "method": "getnameinfo", "params": [ "' + _name + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getNameInfo(self, _name:str)
    
    def rpc_getNameByHash(self, _namehash:str):
        """
        Description:

            Returns the name for a from a given name hash.
        
        Params:

        (*) Denotes required argument

        (*) _namehash : Name hash you wish to look up.
        """

        endpoint = '/'
        post_message = '{ "method": "getnamebyhash", "params": [ "' + _namehash + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ###################################  rpc_getNameByHash(self, _namehash:str)
    
    def rpc_getNameResource(self, _name:str):
        """
        Description:

            Returns the resource records for the given name (added to the trie by the name owner using sendupdate).
        
        Params:

        (*) Denotes required argument

        (*) _name : Name for resource records.
        """

        endpoint = '/'
        post_message = '{ "method": "getnameresource", "params": [ "' + _name + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getNameResource(self, _name:str)
    
    def rpc_getNameProof(self, _name:str):
        """
        Description:

            Returns the merkle tree proof for a given name.
        
        Params:

        (*) Denotes required argument

        (*) _name : Domain name you to retreive the proof for.
        """

        endpoint = '/'
        post_message = '{ "method": "getnameproof", "params": [ "' + _name + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getNameProof(self, _name:str)
    
    def rpc_sendRawClaim(self, _base64_string:str):
        """
        Description:

            If you already have DNSSEC setup, you can avoid publishing a
            TXT record publicly by creating the proof locally. This requires
            that you have direct access to your zone-signing keys. The
            private keys themselves must be stored in BIND's private key
            format and naming convention.
        
        Params:

        (*) Denotes required argument

        (*) _base64_string : Raw serialized base64-string.
        """

        endpoint = '/'
        post_message = '{ "method": "sendrawclaim", "params": [ "' + _base64_string + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_sendRawClaim(self, _base64_string:str)
    
    def rpc_getDnsSecProof(self, _name:str, _estimate:bool=False, _verbose:bool=True):
        """
        Description:

            Adds or removes nodes from banlist.
        
        Params:

        (*) Denotes required argument
        
        (*) _name     : Domain name.

        (*) _estimate : No validation when True.

        (*) _verbose  : Returns (hex) when False.
        """
        
        estimate = ''
        verbose = ''

        if _verbose == True:
            verbose = '1'
        else:
            verbose = '0'

        if _estimate == True:
            estimate = '1'
        else:
            estimate = '0'

        endpoint = '/'
        post_message = '{ "method": "getdnssecproof", "params": ["' + _name + '", ' + estimate + ', ' + verbose + '] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getDnsSecProof(self, _name:str, _estimate:bool=False, _verbose:bool=True)
    
    def rpc_sendRawAirdrop(self, _base64_string:str):
        """
        Description:

            Airdrop proofs create brand new coins directly
            to a Handshake address.
        
        Params:

        (*) Denotes required argument

        (*) _base64_string : Raw serialized base64-string.
        """

        endpoint = '/'
        post_message = '{ "method": "sendrawairdrop", "params": [ "' + _base64_string + '" ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_sendRawAirdrop(self, _base64_string:str)
    
    def rpc_grindName(self, _length:int=10):
        """
        Description:

            Grind a rolled-out available name.
        
        Params:

        (*) Denotes required argument

        (*) _length : Length of name to generate.
        """

        endpoint = '/'
        post_message = '{ "method": "grindname", "params": [ ' + str(_length) + ' ] }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_grindName(self, _length:int=10)


class hsw:

    PORT = ''

    def __init__(self, _api_key:str, _ipaddress:str='127.0.0.1', _port:int=12039):
        """
        Description:

            Initialization of the hsw class
        
        Params:

        (*) Denotes required argument

        (*) _api_key   : HSW API key.

        ( ) _ipaddress : HSW node ip. Default = '127.0.0.1'.

        ( ) _port      : HSW node port. Default = 12039
        """
        global API_KEY
        global ADDRESS
        global PORT

        API_KEY = _api_key
        ADDRESS = _ipaddress
        PORT = str(_port)
    ### END METHOD ################################### __init__(self, _api_key:str, _ipaddress:str='127.0.0.1', _port:int=12039):

    def get(self, _endpoint:str):
        """
        Description:

            GET (json) response from API
        
        Params:

        (*) Denotes required argument

        (*) _endpoint : API endpoint to send GET request.
        """

        url = "http://x:" + API_KEY + "@" + ADDRESS + ":" + PORT + _endpoint
        getResponse = requests.get(url)
        response = getResponse.json()
        return response # Returned as json
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
        return response # Returned as json
    ### END METHOD ################################### post(self, _endpoint:str, _post_message:str)

    def put(self, _endpoint:str, _put_message:str):
        """
        Description:

            PUT (json) message to API
        
        Params:

        (*) Denotes required argument

        (*) _endpoint     : API endpoint to send POST message.

        (*) _post_message : Message to be sent.
        """
        
        url = "http://x:" + API_KEY + "@" + ADDRESS + ":" + PORT + _endpoint
        putRequest = requests.put(url, _put_message)
        response = putRequest.json()
        return response # Returned as json
    ### END METHOD ################################### put(self, _endpoint:str, _put_message:str)

    def createWallet(self, _id:str, _passphrase:str, _accountkey:str='', _type:str='pubkeyhash',
                    _mnemonic:str='',_master:str='', _watchonly:bool=True, _m:int=1, _n:int=1):
        """
        Description:

            Create a new wallet with a specified ID.
        
        Params:

            (*) Denotes required argument

            (*) _id         : Wallet ID (used for storage).

            ( ) _type       : Type of wallet (pubkeyhash, multisig). Default is 'pubkeyhash'

            ( ) _master     : Master HD key. If not present, it will be generated.

            ( ) _mnemonic   : A mnemonic phrase to use to instantiate an hd private key. One will be generated if none provided.

            ( ) _m          : 'm' value for multisig (m-of-n).

            ( ) _n          : 'n' value for multisig (m-of-n)

            (*) _passphrase : A strong passphrase used to encrypt the wallet.

            ( ) _watchonly  : Watch for CLI. Default set to True.

            (*) _accountkey : The extended public key for the primary account in the new wallet. This value is ignored if watchOnly is false (key for CLI).
        """
        
        watchonly = ''

        if _watchonly == True:
            watchonly = '1'
        else:
            watchonly = '0'

        endpoint = '/wallet/' + _id

        put_message = '{"passphrase":"' + _passphrase + '", "watchOnly": ' + watchonly + ', "accountKey":"' + _accountkey + \
                       '", "type":"' + _type + '", "master":"' + _master + '", "m": ' + str(_m) + ', "n": ' + str(_n) + ', "mnemonic":"' + _mnemonic + '"}'

        response = self.put(endpoint, put_message)
        return response
    ### END METHOD ################################### createWallet(self, _id:str, _passphrase:str, _accountkey:str='', _type:str='pubkeyhash',
    #                                                               _mnemonic:str='',_master:str=None, _watchonly:bool=True, _m:int=1, _n:int=1)

    def resetAuthToken(self, _id:str, _passphrase:str):
        """
        Description:

            Create a new wallet with a specified ID.
        
        Params:

            (*) Denotes required argument

            (*) _id         : Wallet ID (used for storage).

            (*) _passphrase : A strong passphrase used to encrypt the wallet.
        """
        

        endpoint = '/wallet/' + _id + "/retoken"

        post_message = '{"passphrase":"' + _passphrase + '"}'

        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### resetAuthToken(self, _id:str, _passphrase:str)

    def getWalletInfo(self, _id:str=''):
        """
        Description:

            Get wallet info by ID. If no id is passed in the CLI it assumes an id of primary.
        
        Params:

            (*) Denotes required argument

            ( ) _id : Name of the wallet whose info you would like to retrieve.
        """
        

        endpoint = '/wallet/' + _id
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getWalletInfo(self, _id:str='')

    def getMasterHDKey(self, _id:str):
        """
        Description:

            Get wallet master HD key. This is normally censored in the
            wallet info route.The provided API key must have admin access.
        
        Params:

            (*) Denotes required argument

            (*) _id : Name of the wallet whose info you would like to retrieve.
        """
        

        endpoint = '/wallet/' + _id + "/master"
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getMasterHDKey(self, _id:str='')

    def changePassword(self, _id:str, _new_passphrase:str, _old_passphrase:str=''):
        """
        Description:

            Change wallet passphrase. Encrypt if unencrypted.
        
        Params:

            (*) Denotes required argument

            (*) _id             : Wallet ID.

            ( ) _old_passphrase : Old passphrase. Pass in empty string if none.

            (*) _new_passphrase : New passphrase.
        """
        

        endpoint = '/wallet/' + _id + "/passphrase"

        post_message = '{"old":"' + _old_passphrase + '", "passphrase":"' + _new_passphrase + '"}'

        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### changePassword(self, _id:str, _new_passphrase:str, _old_passphrase:str='')


    def signTransaction(self, _id:str, _passphrase:str, _tx_hex:str):
        """
        Description:

            Sign a templated transaction (useful for multisig).
 
            (*) _id         : Wallet ID.

            (*) _passphrase : Passphrase to unlock the wallet.

            (*) _tx_hex     : The hex of the transaction you would like to sign.
        """
        
        endpoint = '/wallet/' + _id + "/sign"

        post_message = '{"tx":"' + _tx_hex + '", "passphrase":"' + _passphrase + '"}'

        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### signTransaction(self, _id:str, _passphrase:str, _tx_hex:str)

    def zapTransactions(self, _account:str, _id:str='primary', _age:int=0):
        """
        Description:

            Remove all pending transactions older than a specified age.
        
        Params:

            (*) Denotes required argument

            (*) _id      : Wallet ID.

            ( ) _account : Account to zap from.

            (*) _age     : Age threshold to zap up to (seconds).
        """
        
        endpoint = '/wallet/' + _id + "/zap"

        post_message = '{"account":"' + _account + '", "age":"' + _age + '"}'

        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### zapTransactions(self, _account:str, _id:str, _age:int=0)

    def createAccount(self, _id:str, _passphrase:str, _name:str='', _accountkey:str='', _type:str='pubkeyhash', _m:int=1, _n:int=1):
        """
        Description:

            Create account with specified account name.
        
        Params:

            (*) Denotes required argument

            (*) _id         : Wallet ID (used for storage).

            (*) _passphrase : A strong passphrase used to encrypt the wallet.

            (*) _name       : Name to give the account. Option can be account or name.

            (*) _type       : Type of wallet (pubkeyhash, multisig). Default is 'pubkeyhash'

            ( ) _accountkey : The extended public key for the account. This is ignored for
                              non watch only wallets. Watch only accounts can't accept private
                              keys for import (or sign transactions).

            ( ) _m          : 'm' value for multisig (m-of-n).

            ( ) _n          : 'n' value for multisig (m-of-n)
        """
        

        endpoint = '/wallet/' + _id + "/account/" + _name

        put_message = '{"type":"' + _type + '", "passphrase":"' + _passphrase + '", "accountKey":"' + _accountkey + '", "m": ' + str(_m) + ', "n": ' + str(_n) + '}'

        response = self.put(endpoint, put_message)
        return response
    ### END METHOD ################################### createAccount(self, _id:str, _passphrase:str, _name:str='', _accountkey:str='',
    #                                                                _type:str='pubkeyhash', _m:int=1, _n:int=1)