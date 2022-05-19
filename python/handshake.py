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

########################################################################################################
########################################################################################################
####                                                                                                ####
####                              Begin Handshake Daemon Class                                      ####
####                                                                                                ####
########################################################################################################
########################################################################################################

class hsd:

    API_KEY = ''
    ADDRESS = ''
    PORT = ''

    def __init__(self, _api_key:str, _ipaddress:str='127.0.0.1', _port:int=12037):
        """
        DESCRIPTION:

            Initialization of the hsd class
        
        PARAMS:

        (*) Denotes required argument

        (*) _api_key   : HSD API key.

        (*) _ipaddress : HSD node ip. Default = '127.0.0.1'.

        (*) _port      : HSD node port. Defualt = 12037
        """

        self.API_KEY = _api_key
        self.ADDRESS = _ipaddress
        self.PORT = str(_port)
    ### END METHOD ################################### __init__(self, _api_key:str, _ipaddress:str='127.0.0.1', _port:int=12037)

    def get(self, _endpoint:str):
        """
        DESCRIPTION:

            GET (json) response from API
        
        PARAMS:

        (*) Denotes required argument

        (*) _endpoint : API endpoint to send GET request.
        """

        url = 'http://x:' + self.API_KEY + '@' + self.ADDRESS + ':' + self.PORT + _endpoint
        getResponse = requests.get(url)
        response = getResponse.json()
        return response # Returned as json
    ### END METHOD ################################### get(self, _endpoint:str)

    def post(self, _endpoint:str, _message:str):
        """
        DESCRIPTION:

            POST (json) message to API
        
        PARAMS:

        (*) Denotes required argument

        (*) _endpoint : API endpoint to send POST message.

        (*) _message  : Message to be sent.
        """
        
        url = 'http://x:' + self.API_KEY + '@' + self.ADDRESS + ':' + self.PORT + _endpoint
        postRequest = requests.post(url, _message)
        response = postRequest.json()
        return response # Returned as json
    ### END METHOD ################################### post(self, _endpoint:str, _message:str)

    def getInfo(self):
        """
        DESCRIPTION:

            Get server Info.
        
        PARAMS:

            None
        """

        endpoint = '/'
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getInfo(self)

    def getMemPool(self):
        """
        DESCRIPTION:

            Get mempool snapshot (array of json txs).
        
        PARAMS:

            None
        """
        
        endpoint = '/mempool'
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getMemPool(self)

    def getMemPoolInvalid(self, _verbose:bool=False):
        """
        DESCRIPTION:

            Get mempool rejects filter (a Bloom filter used to store rejected TX hashes).
        
        
        PARAMS:

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
        DESCRIPTION:

            Test a TX hash against the mempool rejects filter.
        

        PARAMS:

        (*) Denotes required argument
        
        (*) _txhash : Transaction hash.
        """
        
        endpoint = '/mempool/invalid/' + _txhash
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getMemPoolInvalidHash(self, _txhash:str)

    def getBlockHashOrHeight(self, _blockHashOrHeight:str):
        """
        DESCRIPTION:

            Returns block info by block hash or height.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _blockHashOrHeight : Hash or Height of block.
        """
        
        endpoint = '/block/' + _blockHashOrHeight
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getBlockHashOrHeight(self, _blockHashOrHeight:str)

    def getHeaderHashOrHeight(self, _headerHashOrHeight:str):
        """
        DESCRIPTION:

            Returns block header by block hash or height.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _headerHashOrHeight : Hash or Height of block.
        """
        
        endpoint = '/header/' + _headerHashOrHeight
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getHeaderHashOrHeight(self, _headerHashOrHeight:str)

    def postBroadcast(self, _tx:str):
        """
        DESCRIPTION:

            Broadcast a transaction by adding it to the node's mempool.
            If mempool verification fails, the node will still forcefully
            advertise and relay the transaction for the next 60 seconds.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _tx : Raw transaction in hex.
        """
        
        endpoint = '/broadcast/'
        _message = '{"tx": "' + _tx + '"}'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### postBroadcast(self, _tx:str)

    def postBroadcastClaim(self, _claim:str):
        """
        DESCRIPTION:

            Broadcast a claim by adding it to the node's mempool.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _claim : Raw claim in hex.
        """
        
        endpoint = '/claim/'
        _message = '{ "claim": "' + _claim + '" }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### postBroadcastClaim(self, _claim:str)

    def getFeeEstimate(self, _blocks:int):
        """
        DESCRIPTION:

            Estimate the fee required (in dollarydoos per kB) for a
            transaction to be confirmed by the network within a targeted
            number of blocks (default 1).
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _blocks : Number of blocks to target confirmation.
        """
        
        endpoint = '/fee?blocks=' + str(_blocks)
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getFeeEstimate(self, _blocks:int)

    def postReset(self, _height:int):
        """
        DESCRIPTION:

            Triggers a hard-reset of the blockchain. All blocks are disconnected
            from the tip down to the provided height. Indexes and Chain Entries
            are removed. Useful for "rescanning" an SPV wallet. Since there are
            no blocks stored on disk, the only way to rescan the blockchain is to
            re-request [merkle]blocks from peers.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _height : Block height to reset chain to.
        """
        
        endpoint = '/reset'
        _message = '{ "height": ' + str(_height) + '}'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### postReset(self, _height:int)

    def getCoinByHashIndex(self, _txhash:str, _index:int):
        """
        DESCRIPTION:

            Get coin by outpoint (hash and index). Returns coin in hsd coin
            JSON format. value is always expressed in subunits.
        
        PARAMS:

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
        DESCRIPTION:

            Get coin objects array by address.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _address : Handshake address.
        """
        
        endpoint = '/coin/address/' + _address
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getCoinByAddress(self, _address:str)

    def getTxByHash(self, _txhash:str):
        """
        DESCRIPTION:

           Returns transaction objects array by hash
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _txhash : Transaction hash.
        """
        
        endpoint = '/tx/' + _txhash
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getTxByHash(self, _txhash:str)

    def getTxByAddress(self, _address:str):
        """
        DESCRIPTION:

           Returns transaction objects array by address.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _address : Handshake address.
        """
        
        endpoint = '/tx/address/' + _address
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getTxByAddress(self, _address:str)

    def rpc_postStop(self):
        """
        DESCRIPTION:

            Stops the running node.
        
        PARAMS:

            None
        """
        
        endpoint = '/'
        _message = '{ "method": "stop" }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_postStop(self)

    def rpc_getInfo(self):
        """
        DESCRIPTION:

            Returns general info.
        
        PARAMS:

            None 
        """
        
        endpoint = '/'
        _message = '{ "method": "getinfo" }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getInfo(self)

    def rpc_getMemoryInfo(self):
        """
        DESCRIPTION:

            Returns Memory usage info.
        
        PARAMS:

            None
        """
        
        endpoint = '/'
        _message = '{ "method": "getmemoryinfo" }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getMemoryInfo(self)

    def rpc_setLogLevel(self, _params:str=['NONE']): # _params = ['NONE', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'SPAM']
        """
        DESCRIPTION:

            Change Log level of the running node.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _params : Level for the logger as list array.
                      [ 'NONE', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'SPAM' ] 
        """
        
        endpoint = '/'
        _message = '{ "method": "setloglevel", "params": [ "' + _params + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_setLogLevel(self, _params:str=['NONE'])

    def rpc_validateAddress(self, _address:str):
        """
        DESCRIPTION:

            Validates address.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _address : Address to validate.
        """
        
        endpoint = '/'
        _message = '{ "validateaddress": "", "params": [ "' + _address + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_validateAddress(self, _address:str)

    def rpc_createMultiSig(self, _nrequired:int, _keyDict:str):
        """
        DESCRIPTION:

            Create multisig address.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _nrequired : Required number of approvals for spending.

        (*) _keyDict   : List array of public keys.
        """
        
        endpoint = '/'
        _message = '{ "method": "createmultisig", "params": [ ' + str(_nrequired) + ', "' + _keyDict + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_createMultiSig(self, _nrequired:int, _keyDict:str)

    def rpc_signMessageWithPrivKey(self, _privkey:str, _message:str):
        """
        DESCRIPTION:

            Signs message with private key. 
        
        PARAMS:
        (*) Denotes required argument
        
        (*) _privkey : Private key.

        (*) _message : Message you want to sign.
        """
        
        endpoint = '/'
        _message = '{ "method": "signmessagewithprivkey", "params": [ "' + _privkey + '", "' + _message + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_signMessageWithPrivKey(self, _privkey:str, _message:str)

    def rpc_verifyMessage(self, _address:str, _signature:str, _message:str):
        """
        DESCRIPTION:

            Verify signature.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _address   : Address of the signer.

        (*) _signature : Signature of signed message.

        (*) _message   : Message that was signed.
        """
        
        endpoint = '/'
        _message = '{ "method": "verifymessage", "params": [ "' + _address + '", "' + _signature + '", "' + _message + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_verifyMessage(self, _address:str, _signature:str, _message:str)

    def rpc_verifyMessageWithName(self, _name:str, _signature:str, _message:str):
        """
        DESCRIPTION:

            Retrieves the address that owns a name and verifies signature.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _name      : Name to retrieve the address used to sign.

        (*) _signature : Signature of signed message.

        (*) _message   : Message that was signed.
        """
        
        endpoint = '/'
        _message = '{ "method": "verifymessagewithname", "params": [ "' + _name + '", "' + _signature + '", "' + _message + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_verifyMessageWithName(self, _name:str, _signature:str, _message:str)

    def rpc_setMockTime(self, _timestamp:int):
        """
        DESCRIPTION:

            Changes network time (This is consensus-critical)
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _timestamp : Timestamp to change to.
        """
        
        endpoint = '/'
        _message = '{ "method": "setmocktime", "params": [ ' + str(_timestamp) + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_setMockTime(self, _timestamp:int)

    def rpc_pruneBlockchain(self):
        """
        DESCRIPTION:

            Prunes the blockchain, it will keep blocks specified in Network Configurations.
        
        PARAMS:

            None
        """
        
        endpoint = '/'
        _message = '{ "method": "pruneblockchain", "params": [] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_postPruneBlockchain(self)
    
    def rpc_invalidateBlock(self, _blockhash:str):
        """
        DESCRIPTION:

            Invalidates the block in the chain. It will rewind network to
            blockhash and invalidate it. It won't accept that block as valid.
            Invalidation will work while running,restarting node will remove
            invalid block from list.
        
        PARAMS:
        
        (*) Denotes required argument
        
        (*) _blockhash : Block's hash.
        """
        
        endpoint = '/'
        _message = '{ "method": "", "params": [ "' + _blockhash + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_invalidateBlock(self, _blockhash:str)
    
    def rpc_reconsiderBlock(self, _blockhash:str):
        """
        DESCRIPTION:

            This rpc command will remove block from invalid block set.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _blockhash : Block's hash.
        """
        
        endpoint = '/'
        _message = '{ "method": "reconsiderblock", "params": [ "' + _blockhash + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_reconsiderBlock(self, _blockhash:str)

    def rpc_getBlockchainInfo(self):
        """
        DESCRIPTION:

            Returns blockchain information.
        
        PARAMS:

            None
        """
        
        endpoint = '/'
        _message = '{ "method": "getblockchaininfo" }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getBlockchainInfo(self)
    
    def rpc_getBestBlockHash(self):
        """
        DESCRIPTION:

            Returns Block Hash of the tip.
        
        PARAMS:

            None
        """
        
        endpoint = '/'
        _message = '{ "method": "getbestblockhash" }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getBestBlockHash(self)
    
    def rpc_getBlockCount(self):
        """
        DESCRIPTION:

            Returns block count.
        
        PARAMS:

            None
        """
        
        endpoint = '/'
        _message = '{ "method": "getblockcount" }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getBlockCount(self)
    
    def rpc_getBlock(self, _blockhash:str, _verbose:bool=True, _details:bool=False):
        """
        DESCRIPTION:

            Returns information about block.

        PARAMS:

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
        _message = '{ "method": "getblock", "params": [ "' + _blockhash + '", ' + verbose + ', ' + details + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getBlock(self, _blockhash:str, _verbose:bool=True, _details:bool=False)
    
    def rpc_getBlockByHeight(self, _blockheight:int, _verbose:bool=True, _details:bool=False):
        """
        DESCRIPTION:

            Returns information about block by height.

        PARAMS:

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
        _message = '{ "method": "getblockbyheight", "params": [ ' + str(_blockheight) + ', ' + verbose + ', ' + details + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getBlockByHeight(self, _blockheight:int, _verbose:bool=True, _details:bool=False)
    
    def rpc_getBlockHash(self, _blockheight:int):
        """
        DESCRIPTION:

            Returns block's hash given its height.

        PARAMS:

        (*) Denotes required argument
        
        (*) _blockheight : Height of the block in the blockchain.
        """
        
        endpoint = '/'
        _message = '{ "method": "getblockhash", "params": [ ' + str(_blockheight) + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getBlockHash(self, _blockheight:int)
    
    def rpc_getBlockHeader(self, _blockhash:str, _verbose:bool=True):
        """
        DESCRIPTION:

            Returns a block's header given its hash.

        PARAMS:

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
        _message = '{ "method": "getblockheader", "params": [ "' + _blockhash + '", ' + verbose + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getBlockHeader(self, _blockhash:str, _verbose:bool=True)
    
    def rpc_getChainTips(self):
        """
        DESCRIPTION:

            Returns chaintips.
        
        PARAMS:

            None
        """
        
        endpoint = '/'
        _message = '{ "method": "getchaintips" }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getChainTips(self)
    
    def rpc_getDifficulty(self):
        """
        DESCRIPTION:

            Returns current difficulty level.
        
        PARAMS:

            None
        """
        
        endpoint = '/'
        _message = '{ "method": "getdifficulty" }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getDifficulty(self)
    
    def rpc_getMemPoolInfo(self):
        """
        DESCRIPTION:

            Returns informations about mempool.
        
        PARAMS:

            None
        """
        
        endpoint = '/'
        _message = '{ "method": "getmempoolinfo" }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getMemPoolInfo(self)
    
    def rpc_getMemPoolAncestors(self, _txhash:str, _verbose:bool=False):
        """
        DESCRIPTION:

            Returns all in-mempool ancestors for a transaction in the mempool.
        
        PARAMS:

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
        _message = '{ "method": "getmempoolancestors", "params": [ "' + _txhash + '", ' + verbose + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getMemPoolAncestors(self, _txhash:str, _verbose:bool=False)
    
    def rpc_getMemPoolDescendants(self, _txhash:str, _verbose:bool=False):
        """
        DESCRIPTION:

            Returns all in-mempool descendants for a transaction in the mempool.
        
        PARAMS:

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
        _message = '{ "method": "getmempooldescendants", "params": [ "' + _txhash + '", ' + verbose + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getMemPoolDescendants(self, _txhash:str, _verbose:bool=False)
    
    def rpc_getMemPoolEntry(self, _txhash:str):
        """
        DESCRIPTION:

            Returns mempool transaction info by its hash.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _txhash : Transaction Hash.
        """
        
        endpoint = '/'
        _message = '{ "method": "getmempoolentry", "params": [ "' + _txhash + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getMemPoolEntry(self, _txhash:str)
    
    def rpc_getRawMemPool(self, _verbose:bool=False):
        """
        DESCRIPTION:

            Returns mempool detailed information (on verbose). Or mempool tx list.
        
        PARAMS:

        (*) Denotes required argument
        
        ( ) _verbose : False returns only tx hashs, true - returns full tx info.
        """

        verbose = ''

        if _verbose == True:
            verbose = '1'
        else:
            verbose = '0'
        
        endpoint = '/'
        _message = '{ "method": "getrawmempool", "params": [ ' + verbose + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getRawMemPool(self, _verbose:bool=False)
    
    def rpc_prioritiseTransaction(self, _txhash:str, _priorityDelta:int, _feeDelta:int):
        """
        DESCRIPTION:

            Prioritises the transaction.

            Note: Changing fee or priority will only trick local miner (using this mempool) into
                accepting Transaction(s) into the block. (even if Priority/Fee doen't qualify)
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _txhash        : Transaction hash.

        (*) _priorityDelta : Virtual priority to add/subtract to the entry.

        (*) _feeDelta      : Virtual fee to add/subtract to the entry.
        """
        
        endpoint = '/'
        _message = '{ "method": "prioritisetransaction", "params": [ "' + _txhash + '", "' + str(_priorityDelta) + '", "' + str(_feeDelta) + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_prioritiseTransaction(self, _txhash:str, _priorityDelta:int, _feeDelta:int)
    
    def rpc_estimateFee(self, _nblocks:int=1):
        """
        DESCRIPTION:

            Estimates fee to be paid for transaction.
        
        PARAMS:

        (*) Denotes required argument
        
        ( ) _nblocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        _message = '{ "method": "estimatefee", "params": [ ' + str(_nblocks) + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_estimateFee(self, _nblocks:int=1)
    
    def rpc_estimatePriority(self, _nblocks:int=1):
        """
        DESCRIPTION:

            Estimates the priority (coin age) that a transaction
            needs in order to be included within a certain number
            of blocks as a free high-priority transaction.
        
        PARAMS:

        (*) Denotes required argument
        
        ( ) _nblocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        _message = '{ "method": "estimatepriority", "params": [ ' + str(_nblocks) + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_estimatePriority(self, _nblocks:int=1)
    
    def rpc_estimateSmartFee(self, _nblocks:int=1):
        """
        DESCRIPTION:

            Estimates smart fee to be paid for transaction.
        
        PARAMS:

        (*) Denotes required argument
        
        ( ) _nblocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        _message = '{ "method": "estimatesmartfee", "params": [ ' + str(_nblocks) + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_estimateSmartFee(self, _nblocks:int=1)
    
    def rpc_estimateSmartPriority(self, _nblocks:int=1):
        """
        DESCRIPTION:

            Estimates smart priority (coin age) that a transaction
            needs in order to be included within a certain number
            of blocks as a free high-priority transaction.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _nblocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        _message = '{ "method": "estimatesmartpriority", "params": [ ' + str(_nblocks) + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_estimateSmartPriority(self, _nblocks:int=1)
    
    def rpc_getTxOut(self, _txhash:str, _index:int, _includemempool:int=1):
        """
        DESCRIPTION:

            Get outpoint of the transaction.
        
        PARAMS:
        
        (*) Denotes required argument
        
        (*) _txhash         : Transaction hash.

        (*) _index          : Index of the outpoint tx.

        ( ) _includemempool : Whether to include mempool transactions.
        """
        
        endpoint = '/'
        _message = '{ "method": "gettxout", "params": [ "' + _txhash + '", ' + str(_index) + ', ' + str(_includemempool) + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getTxOut(self, _txhash:str, _index:int, _includemempool:int=1)
    
    def rpc_getTxOutSetInfo(self):
        """
        DESCRIPTION:

            Returns information about UTXO's from Chain.
        
        PARAMS:

            None
        """

        endpoint = '/'
        _message = '{ "method": "gettxoutsetinfo", "params": [] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getTxOutSetInfo(self)
    
    def rpc_getRawTransaction(self, _txhash:str, _verbose:bool=False):
        """
        DESCRIPTION:

            Returns raw transaction
        
        PARAMS:

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
        _message = '{ "method": "getrawtransaction", "params": [ "' + _txhash + '", ' + verbose + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getRawTransaction(self, _txhash:str, _verbose:bool=False)
    
    def rpc_decodeRawTransaction(self, _rawtx:str):
        """
        DESCRIPTION:

            Decodes raw tx and provide chain info.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _rawtx : Raw transaction hex.
        """
        
        endpoint = '/'
        _message = '{ "method": "decoderawtransaction", "params": [ "' + _rawtx + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_decodeRawTransaction(self, _rawtx:str)
    
    def rpc_decodeScript(self, _script:str):
        """
        DESCRIPTION:

            Decodes script.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _script : Script hex.
        """
        
        endpoint = '/'
        _message = '{ "method": "decodescript", "params": [ "' + _script + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_decodeScript(self, _script:str)
    
    def rpc_sendRawTransaction(self, _rawtx:str):
        """
        DESCRIPTION:

            Sends raw transaction without verification.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _rawtx : Raw transaction hex.
        """
        
        endpoint = '/'
        _message = '{ "method": "sendrawtransaction", "params": [ "' + _rawtx + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_sendRawTransaction(self, _rawtx:str)
    
    def rpc_createRawTransaction(self, _txhash:str, _txindex:int, _address:str, _amount:int, _data:str):
        """
        DESCRIPTION:

            Creates raw, unsigned transaction without any formal verification.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _txhash  : Transaction hash.

        (*) _txindex : Transaction outpoint index.

        (*) _address : Recipient address.

        (*) _amount  : Amount to send in HNS (float).
        """

        endpoint = '/'
        _message = '{ "method": "createrawtransaction", "params": [[{ "txid": "' + _txhash + '", "vout": ' + str(_txindex) + ' }], { "' + _address + '": ' + str(_amount) + ', "data": "' + _data + '" }] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_createRawTransaction(self, _txhash:str, _txindex:int, _address:str, _amount:int, _data:str)
    
    def rpc_signRawTransaction(self, _rawtx:str, _txhash:str, _txindex:int, _address:str, _amount:int, _privkey:str):
        """
        DESCRIPTION:

            Creates raw, unsigned transaction without any formal verification.
        
        PARAMS:

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
        _message = '{ "method": "signrawtransaction", "params": [ "' + _rawtx + '", [{ "txid": "' + _txhash + '", "vout": ' + str(_txindex) + ', "address": "' + _address + '", "amount": ' + str(_amount) + ' }], [ "' + _privkey + '" ]] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_signRawTransaction(self, _rawtx:str, _txhash:str, _txindex:int, _address:str, _amount:int, _privkey:str)
    
    def rpc_getTxOutProof(self, _txidlist:str):
        """
        DESCRIPTION:

            Checks if transactions are within block. Returns proof of transaction inclusion (raw MerkleBlock).
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _txidlist  : List array of transaction ID's
        """

        endpoint = '/'
        _message = '{ "method": "gettxoutproof", "params": [ "' + _txidlist + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getTxOutProof(self, _txidlist:str)
    
    def rpc_verifyTxOutProof(self, _proof:str):
        """
        DESCRIPTION:

            Checks the proof for transaction inclusion. Returns transaction hash if valid.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _proof : Proof of transaction inclusion (raw MerkleBlock).
        """

        endpoint = '/'
        _message = '{ "method": "verifytxoutproof", "params": [ "' + _proof + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_verifyTxOutProof(self, _proof)
    
    def rpc_getNetworkHashPerSec(self, _blocks:int=120, _height:int=1):
        """
        DESCRIPTION:

            Returns the estimated current or historical network hashes per second, based on last blocks.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _blocks : Number of blocks to lookup.
        
        (*) _height : Starting height for calculations.
        """

        endpoint = '/'
        _message = '{ "method": "getnetworkhashps", "params": [ ' + str(_blocks) + ', ' + str(_height) + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getNetworkHashPerSec(self, _blocks:int=120, _height:int=1)
    
    def rpc_getMiningInfo(self):
        """
        DESCRIPTION:

            Returns mining info.

            Note: currentblocksize, currentblockweight, currentblocktx, difficulty are
                  returned when there's active work. generate - is true when hsd itself
                  is mining.
        
        PARAMS:

            None
        """

        endpoint = '/'
        _message = '{ "method": "getmininginfo", "params": [] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getMiningInfo(self)
    
    def rpc_getWork(self, _data:str=[]):
        """
        DESCRIPTION:

            Returns hashing work to be solved by miner. Or submits solved block.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _data : Data to be submitted to the network.
        """

        endpoint = '/'
        _message = '{ "method": "getworklp", "params": [ "' + _data + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getWorkLP(self)
    
    def rpc_getWorkLP(self):
        """
        DESCRIPTION:

            Long polling for new work.

            Returns new work, whenever new TX is received in the mempoolor new
            block has been discovered. So miner can restart mining on new data.
        
        PARAMS:

            None
        """

        endpoint = '/'
        _message = '{ "method": "getworklp", "params": [] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getWorkLP(self)
    
    def rpc_getBlockTemplate(self):
        """
        DESCRIPTION:

            Returns block template or proposal for use with mining. Also validates proposal if mode is specified as proposal.
        
        PARAMS:

            None
        """

        endpoint = '/'
        _message = '{ "method": "getblocktemplate", "params": [] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getBlockTemplate(self):
    
    def rpc_submitBlock(self, _blockdata:str):
        """
        DESCRIPTION:

            Adds block to chain.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _blockdata : Mined block data (hex).
        """

        endpoint = '/'
        _message = '{ "method": "submitblock", "params": [ "' + _blockdata + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_submitBlock(self, _blockdata:str)
    
    def rpc_verifyBlock(self, _blockdata:str):
        """
        DESCRIPTION:

            Verifies the block data.
        
        PARAMS:
        (*) Denotes required argument
        
        (*) _blockdata : Mined block data (hex).
        """

        endpoint = '/'
        _message = '{ "method": "verifyblock", "params": [ "' + _blockdata + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_verifyBlock(self, _blockdata:str)
    
    def rpc_setGenerate(self, _mining:int=0, _proclimit:int=0):
        """
        DESCRIPTION:

            Will start the mining on CPU.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _mining    : 1 will start mining, 0 will stop.

        (*) _proclimit : 1 will set processor limit, 0 will remove limit.
        """

        endpoint = '/'
        _message = '{ "method": "setgenerate", "params": [ ' + str(_mining) + ', ' + str(_proclimit) + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_setGenerate(self, _mining:int=0, _proclimit:int=0)
    
    def rpc_getGenerate(self):
        """
        DESCRIPTION:

            Returns status of mining on Node.
        
        PARAMS:

            None
        """

        endpoint = '/'
        _message = '{ "method": "getgenerate", "params": [] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getGenerate(self)
    
    def rpc_Generate(self, _numblocks:int=1):
        """
        DESCRIPTION:

            Mines numblocks number of blocks. Will return once all blocks are mined. CLI command may timeout before that happens.
        
        PARAMS:
        (*) Denotes required argument
        
        (*) _numblocks : Number of blocks to mine.
        """

        endpoint = '/'
        _message = '{ "method": "generate", "params": [' + str(_numblocks) + '] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_Generate(self, _numblocks:int=1)
    
    def rpc_GenerateToAddress(self, _address:str, _numblocks:int=1):
        """
        DESCRIPTION:

            Mines numblocks blocks, with address as coinbase.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _address   : Coinbase address for new blocks.

        (*) _numblocks : Number of blocks to mine.
        """

        endpoint = '/'
        _message = '{ "method": "generatetoaddress", "params": [ ' + str(_numblocks) + ', "' + _address + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_GenerateToAddress(self, _address:str, _numblocks:int=1)
    
    def rpc_getConnectionCount(self):
        """
        DESCRIPTION:

            Returns connection count.
        
        PARAMS:

            None
        """

        endpoint = '/'
        _message = '{ "method": "getconnectioncount", "params": [] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getConnectionCount(self)
    
    def rpc_ping(self):
        """
        DESCRIPTION:

            Will send ping request to every connected peer.
        
        PARAMS:

            None
        """

        endpoint = '/'
        _message = '{ "method": "ping", "params": [] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_ping(self)
    
    def rpc_getPeerInfo(self):
        """
        DESCRIPTION:

            Returns information about all connected peers.
        
        PARAMS:

            None
        """

        endpoint = '/'
        _message = '{ "method": "getpeerinfo", "params": [] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getPeerInfo(self)
    
    def rpc_addNode(self, _nodeAddress:str, _cmd:str):
        """
        DESCRIPTION:

            Adds or removes peers in Host List. 
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _nodeAddress : IP Address of the Node. Eg. '127.0.0.1:14038'

        (*) _cmd         : 'add' - Adds node to Host List and connects to it.

                           'onetry' - Tries to connect to the given node.

                           'remove' - Removes node from host list.
        """

        endpoint = '/'
        _message = '{ "method": "addnode", "params": [ "' + _nodeAddress + '", "' + _cmd + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_addNode(self, _nodeAddress:str, _cmd:str)
    
    def rpc_disconnectNode(self, _nodeAddress:str):
        """
        DESCRIPTION:

            Disconnects node.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _address : IP Address of the Node. Eg. '127.0.0.1:14038'
        """

        endpoint = '/'
        _message = '{ "method": "disconnectnode", "params": [ "' + _nodeAddress + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_disconnectNode(self, _nodeAddress:str)
    
    def rpc_getAddedNodeInfo(self, _nodeAddress:str):
        """
        DESCRIPTION:

            Returns node information from host list.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _address : IP Address of the Node. Eg. '127.0.0.1:14038'
        """

        endpoint = '/'
        _message = '{ "method": "getaddednodeinfo", "params": [ "' + _nodeAddress + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getAddedNodeInfo(self, _nodeAddress:str)
    
    def rpc_getNetTotals(self):
        """
        DESCRIPTION:

            Returns information about used network resources.
        
        PARAMS:

            None
        """

        endpoint = '/'
        _message = '{ "method": "getnettotals", "params": [] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getNetTotals(self)
    
    def rpc_getNetworkInfo(self):
        """
        DESCRIPTION:

            Returns local node's network information.
        
        PARAMS:

            None
        """

        endpoint = '/'
        _message = '{ "method": "getnetworkinfo", "params": [] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### def rpc_getNetworkInfo(self)
    
    def rpc_setBan(self, _nodeAddress:str, _cmd:str):
        """
        DESCRIPTION:

            Adds or removes nodes from banlist.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) _nodeAddress : IP Address of the Node. Eg. '127.0.0.1:14038'

        (*) _cmd         : 'add' - Adds node to ban list, removes from host list, disconnects.

                           'remove' - Removes node from ban list.
        """

        endpoint = '/'
        _message = '{ "method": "setban", "params": ["' + _nodeAddress + '", "' + _cmd + '"] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_setBan(self, _nodeAddress:str, _cmd:str)
    
    def rpc_listBan(self):
        """
        DESCRIPTION:

            Lists all banned peers.
        
        PARAMS:

            None
        """

        endpoint = '/'
        _message = '{ "method": "listbanned", "params": [] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_listBan(self)
    
    def rpc_clearBanned(self):
        """
        DESCRIPTION:

            Removes all banned peers.
        
        PARAMS:

            None
        """

        endpoint = '/'
        _message = '{ "method": "clearbanned", "params": [] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_clearBanned(self)
    
    def rpc_getNameInfo(self, _name:str):
        """
        DESCRIPTION:

            Returns information on a given name. Use this function to query any name in any state.
        
        PARAMS:

        (*) Denotes required argument

        (*) _name : Name you wish to look up.
        """

        endpoint = '/'
        _message = '{ "method": "getnameinfo", "params": [ "' + _name + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getNameInfo(self, _name:str)
    
    def rpc_getNameByHash(self, _namehash:str):
        """
        DESCRIPTION:

            Returns the name for a from a given name hash.
        
        PARAMS:

        (*) Denotes required argument

        (*) _namehash : Name hash you wish to look up.
        """

        endpoint = '/'
        _message = '{ "method": "getnamebyhash", "params": [ "' + _namehash + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ###################################  rpc_getNameByHash(self, _namehash:str)
    
    def rpc_getNameResource(self, _name:str):
        """
        DESCRIPTION:

            Returns the resource records for the given name (added to the trie by the name owner using sendupdate).
        
        PARAMS:

        (*) Denotes required argument

        (*) _name : Name for resource records.
        """

        endpoint = '/'
        _message = '{ "method": "getnameresource", "params": [ "' + _name + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getNameResource(self, _name:str)
    
    def rpc_getNameProof(self, _name:str):
        """
        DESCRIPTION:

            Returns the merkle tree proof for a given name.
        
        PARAMS:

        (*) Denotes required argument

        (*) _name : Domain name you to retreive the proof for.
        """

        endpoint = '/'
        _message = '{ "method": "getnameproof", "params": [ "' + _name + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getNameProof(self, _name:str)
    
    def rpc_sendRawClaim(self, _base64_string:str):
        """
        DESCRIPTION:

            If you already have DNSSEC setup, you can avoid publishing a
            TXT record publicly by creating the proof locally. This requires
            that you have direct access to your zone-signing keys. The
            private keys themselves must be stored in BIND's private key
            format and naming convention.
        
        PARAMS:

        (*) Denotes required argument

        (*) _base64_string : Raw serialized base64-string.
        """

        endpoint = '/'
        _message = '{ "method": "sendrawclaim", "params": [ "' + _base64_string + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_sendRawClaim(self, _base64_string:str)
    
    def rpc_getDnsSecProof(self, _name:str, _estimate:bool=False, _verbose:bool=True):
        """
        DESCRIPTION:

            Adds or removes nodes from banlist.
        
        PARAMS:

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
        _message = '{ "method": "getdnssecproof", "params": ["' + _name + '", ' + estimate + ', ' + verbose + '] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_getDnsSecProof(self, _name:str, _estimate:bool=False, _verbose:bool=True)
    
    def rpc_sendRawAirdrop(self, _base64_string:str):
        """
        DESCRIPTION:

            Airdrop proofs create brand new coins directly
            to a Handshake address.
        
        PARAMS:

        (*) Denotes required argument

        (*) _base64_string : Raw serialized base64-string.
        """

        endpoint = '/'
        _message = '{ "method": "sendrawairdrop", "params": [ "' + _base64_string + '" ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_sendRawAirdrop(self, _base64_string:str)
    
    def rpc_grindName(self, _length:int=10):
        """
        DESCRIPTION:

            Grind a rolled-out available name.
        
        PARAMS:

        (*) Denotes required argument

        (*) _length : Length of name to generate.
        """

        endpoint = '/'
        _message = '{ "method": "grindname", "params": [ ' + str(_length) + ' ] }'
        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### rpc_grindName(self, _length:int=10)


########################################################################################################
########################################################################################################
####                                                                                                ####
####                              Begin Handshake Wallet Class                                      ####
####                                                                                                ####
########################################################################################################
########################################################################################################

class hsw:
    API_KEY = ''
    ADDRESS = ''
    PORT = ''

    def __init__(self, _api_key:str, _ipaddress:str='127.0.0.1', _port:int=12039):
        """
        DESCRIPTION:

            Initialization of the hsw class
        
        PARAMS:

        (*) Denotes required argument

        (*) _api_key   : HSW API key.

        ( ) _ipaddress : HSW node ip. Default = '127.0.0.1'.

        ( ) _port      : HSW node port. Default = 12039
        """

        self.API_KEY = _api_key
        self.ADDRESS = _ipaddress
        self.PORT = str(_port)
    ### END METHOD ################################### __init__(self, _api_key:str, _ipaddress:str='127.0.0.1', _port:int=12039):

    def get(self, _endpoint:str):
        """
        DESCRIPTION:

            GET (json) response from API
        
        PARAMS:

        (*) Denotes required argument

        (*) _endpoint : API endpoint to send GET request.
        """

        url = 'http://x:' + self.API_KEY + '@' + self.ADDRESS + ':' + self.PORT + _endpoint
        getResponse = requests.get(url)
        response = getResponse.json()
        return response # Returned as json
    ### END METHOD ################################### get(self, _endpoint:str)

    def post(self, _endpoint:str, _message:str):
        """
        DESCRIPTION:

            POST (json) message to API
        
        PARAMS:

        (*) Denotes required argument

        (*) _endpoint : API endpoint to send POST message.

        (*) _message  : Message to be sent.
        """
        
        url = 'http://x:' + self.API_KEY + '@' + self.ADDRESS + ':' + self.PORT + _endpoint
        postRequest = requests.post(url, _message)
        response = postRequest.json()
        return response # Returned as json
    ### END METHOD ################################### post(self, _endpoint:str, _message:str)

    def put(self, _endpoint:str, _message:str=''):
        """
        DESCRIPTION:

            PUT (json) message to API
        
        PARAMS:

        (*) Denotes required argument

        (*) _endpoint : API endpoint to send POST message.

        (*) _message  : Message to be sent.
        """
        
        url = 'http://x:' + self.API_KEY + '@' + self.ADDRESS + ':' + self.PORT + _endpoint
        putRequest = requests.put(url, _message)
        response = putRequest.json()
        return response # Returned as json
    ### END METHOD ################################### put(self, _endpoint:str, _message:str)

    def delete(self, _endpoint:str, _message:str):
        """
        DESCRIPTION:

            PUT (json) message to API
        
        PARAMS:

        (*) Denotes required argument

        (*) _endpoint : API endpoint to send POST message.

        (*) _message  : Message to be sent.
        """
        
        url = 'http://x:' + self.API_KEY + '@' + self.ADDRESS + ':' + self.PORT + _endpoint
        putRequest = requests.delete(url, _message)
        response = putRequest.json()
        return response # Returned as json
    ### END METHOD ################################### put(self, _endpoint:str, _message:str)

    def createWallet(self, _passphrase:str, _id:str='primary', _accountkey:str='', _type:str='pubkeyhash',
                    _mnemonic:str='',_master:str='', _watchonly:bool=True, _m:int=1, _n:int=1):
        """
        DESCRIPTION:

            Create a new wallet with a specified ID.
        
        PARAMS:

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

        _message = '{"passphrase":"' + _passphrase + '", "watchOnly": ' + watchonly + ', "accountKey":"' + _accountkey + \
                       '", "type":"' + _type + '", "master":"' + _master + '", "m": ' + str(_m) + ', "n": ' + str(_n) + ', "mnemonic":"' + _mnemonic + '"}'

        response = self.put(endpoint, _message)
        return response
    ### END METHOD ################################### createWallet(self, _id:str='primary', _passphrase:str, _accountkey:str='', _type:str='pubkeyhash',
    #                                                               _mnemonic:str='',_master:str=None, _watchonly:bool=True, _m:int=1, _n:int=1)

    def resetAuthToken(self, _passphrase:str, _id:str='primary'):
        """
        DESCRIPTION:

            Create a new wallet with a specified ID.
        
        PARAMS:

            (*) Denotes required argument

            (*) _id         : Wallet ID.

            (*) _passphrase : A strong passphrase used to encrypt the wallet.
        """
        
        endpoint = '/wallet/' + _id + '/retoken'

        _message = '{"passphrase":"' + _passphrase + '"}'

        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### resetAuthToken(self, _id:str='primary', _passphrase:str)

    def getWalletInfo(self, _id:str=''):
        """
        DESCRIPTION:

            Get wallet info by ID. If no id is passed in the CLI it assumes an id of primary.
        
        PARAMS:

            (*) Denotes required argument

            ( ) _id : Name of the wallet whose info you would like to retrieve.
        """
        
        endpoint = '/wallet/' + _id
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getWalletInfo(self, _id:str='')

    def getMasterHDKey(self, _id:str='primary'):
        """
        DESCRIPTION:

            Get wallet master HD key. This is normally censored in the
            wallet info route.The provided API key must have admin access.
        
        PARAMS:

            (*) Denotes required argument

            (*) _id : Name of the wallet whose info you would like to retrieve.
        """
        
        endpoint = '/wallet/' + _id + '/master'
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getMasterHDKey(self, _id:str='')

    def changePassword(self, _new_passphrase:str, _id:str='primary', _old_passphrase:str=''):
        """
        DESCRIPTION:

            Change wallet passphrase. Encrypt if unencrypted.
        
        PARAMS:

            (*) Denotes required argument

            (*) _id             : Wallet ID.

            ( ) _old_passphrase : Old passphrase. Pass in empty string if none.

            (*) _new_passphrase : New passphrase.
        """
        
        endpoint = '/wallet/' + _id + '/passphrase'

        _message = '{"old":"' + _old_passphrase + '", "passphrase":"' + _new_passphrase + '"}'

        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### changePassword(self, _id:str='primary', _new_passphrase:str, _old_passphrase:str='')

    def signTransaction(self, _passphrase:str, _tx_hex:str, _id:str='primary'):
        """
        DESCRIPTION:

            Sign a templated transaction (useful for multisig).
 
            (*) _id         : Wallet ID.

            (*) _passphrase : Passphrase to unlock the wallet.

            (*) _tx_hex     : The hex of the transaction you would like to sign.
        """
        
        endpoint = '/wallet/' + _id + '/sign'

        _message = '{"tx":"' + _tx_hex + '", "passphrase":"' + _passphrase + '"}'

        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### signTransaction(self, _id:str='primary', _passphrase:str, _tx_hex:str)

    def zapTransactions(self, _account:str, _id:str='primary', _age:int=0):
        """
        DESCRIPTION:

            Remove all pending transactions older than a specified age.
        
        PARAMS:

            (*) Denotes required argument

            (*) _id      : Wallet ID.

            ( ) _account : Account to zap from.

            (*) _age     : Age threshold to zap up to (seconds).
        """
        
        endpoint = '/wallet/' + _id + '/zap'

        _message = '{"account":"' + _account + '", "age":"' + _age + '"}'

        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### zapTransactions(self, _account:str, _id:str='primary', _age:int=0)

    def lockWallet(self, _id:str='primary'):
        """
        DESCRIPTION:

            If unlock was called, zero the derived AES key and revert to normal behavior.
        
        PARAMS:

            (*) Denotes required argument

            ( ) _id : Name ID of wallet to lock.
        """
        
        endpoint = '/wallet/' + _id + '/lock'

        _message = ''

        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### lockWallet(self, _id:str='primary')

    def importPublicKey(self, _account:str, _pub_key:str, _id:str='primary'):
        """
        DESCRIPTION:

            Import a standard (public) WIF key.

            A rescan will be required to see any transaction history associated with the key.
            
            Note: Imported keys do not exist anywhere in the wallet's HD tree.They can be
                  associated with accounts but will not be properly backed up with only the
                  mnemonic. 
        
        PARAMS:

            (*) Denotes required argument

            (*) _id      : ID of target wallet to import key into.

            ( ) _pub_key : Hex encoded public key.
        """
        
        endpoint = '/wallet/' + _id + '/import'

        _message = '{"account":"' + _account + '", "publicKey":"' + _pub_key + '"}'

        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### importPublicKey(self, _account:str, _pub_key:str, _id:str='primary')

    def importPrivateKey(self, _account:str, _priv_key:str, _id:str='primary'):
        """
        DESCRIPTION:

            Import a standard (private) WIF key.

            A rescan will be required to see any transaction history associated with the key.
            
            Note: Imported keys do not exist anywhere in the wallet's HD tree.They can be
                  associated with accounts but will not be properly backed up with only the
                  mnemonic. 
        
        PARAMS:

            (*) Denotes required argument

            (*) _id       : ID of target wallet to import key into.

            ( ) _priv_key : Hex encoded public key.
        """
        
        endpoint = '/wallet/' + _id + '/import'

        _message = '{"account":"' + _account + '", "privateKey":"' + _priv_key + '"}'

        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### importPrivateKey(self, _account:str, _priv_key:str, _id:str='primary')

    def getBlocksWithWalletTX(self, _id:str='primary'):
        """
        DESCRIPTION:

            List all block heights which contain any wallet transactions. Returns an array of block heights.
        
        PARAMS:

            (*) Denotes required argument

            (*) _id : Name of the wallet.
        """
        
        endpoint = '/wallet/' + _id + '/block'
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getBlocksWithWalletTX(self, _id:str='primary')

    def getWalletBlockByHeight(self, _height:int, _id:str='primary'):
        """
        DESCRIPTION:

            Get block info by height.
        
        PARAMS:

            (*) Denotes required argument

            (*) _height : Height of block being queried.

            ( ) _id     : Name of the wallet.
        """
        
        endpoint = '/wallet/' + _id + '/block/' + str(_height)
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getWalletBlockByHeight(self, _id:str='primary')

    def addXPubKey(self, _accountkey:str, _account:str='default'):
        """
        DESCRIPTION:

            Add a shared xpubkey to wallet. Must be a multisig wallet.

            Note: Since it must be a multisig, the wallet on creation should
            be set with `m` and `n` where `n` is greater than 1 (since the first key
            is always that wallet's own xpubkey). Creating new addresses from
            this account will not be possible until `n` number of xpubkeys are
            added to the account.

            Response will return `addedKey: true` if key was added on this
            request. Returns `addedKey: false` if key already added, but
            will still return `success: true` with status `200`.
        
        PARAMS:

            (*) Denotes required argument

            (*) _accountkey : xpubkey to add to the multisig wallet.

            ( ) _account    : Multisig account to add the xpubkey to (default='default').
        """

        endpoint = '/wallet/multisig3/shared-key/'

        _message = '{"accountKey":"' + _accountkey + '", "account":"' + _account + '"}'

        response = self.put(endpoint, _message)
        return response
    ### END METHOD ################################### addXPubKey(self, _accountkey:str, _account:str='default')

    def removeXPubKey(self, _accountkey:str, _account:str='default'):
        """
        DESCRIPTION:

            Remove shared xpubkey from wallet if present.

            Response will return `removedKey: true` if key was removed on
            this request. Returns `removedKey: false` if key was already removed, but will
            still return `success: true` with status `200`.

            Note: Remove Key is only available to a multisig wallet that is
            not yet "complete" -- as in, `n-1` number of keys have not yet been
            added to the wallet's own original key. Once a multisig wallet
            has the right number of keys to create m-of-n addresses, this
            function will return an error
        
        PARAMS:

            (*) Denotes required argument

            (*) _accountkey : xpubkey to add to the multisig wallet.

            ( ) _account    : Multisig account to remove the xpubkey from (default='default').
        """

        endpoint = '/wallet/multisig3/shared-key/'

        _message = '{"accountKey":"' + _accountkey + '", "account":"' + _account + '"}'

        response = self.delete(endpoint, _message)
        return response
    ### END METHOD ################################### removeXPubKey(self, _accountkey:str, _account:str='default')

    def getPublicKeyByAddress(self, _address:str, _id:str='primary'):
        """
        DESCRIPTION:

            Get wallet key by address. Returns wallet information with address and public key.
        
        PARAMS:

            (*) Denotes required argument

            (*) _address : Bech32 encoded address to get corresponding public key for.

            ( ) _id      : Name of wallet.
        """
        
        endpoint = '/wallet/' + _id + '/key/' + _address
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getPublicKeyByAddress(self, _address:str, _id:str='primary')

    def getPrivateKeyByAddress(self, _address:str, _passphrase:str, _id:str='primary'):
        """
        DESCRIPTION:

            Get wallet private key (WIF format) by address. Returns just the private key.
        
        PARAMS:

            (*) Denotes required argument

            (*) _address    : Address to get corresponding private key for.

            (*) _passphrase : Passphrase of wallet.

            ( ) _id         : Name of wallet.
        """
        
        endpoint = '/wallet/' + _id + '/wif/' + _address + '?passphrase=' + _passphrase
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getPrivateKeyByAddress(self, _address:str, _passphrase:str, _id:str='primary')

    def generateReceivingAddress(self, _account:str, _id:str='primary'):
        """
        DESCRIPTION:

            Derive new receiving address for account.
        
        PARAMS:

            (*) Denotes required argument

            (*) _id       : Name of wallet.

            (*) _account  : BIP44 account to generate address from.
        """
        
        endpoint = '/wallet/' + _id + '/address'

        _message = '{"account":"' + _account + '"}'

        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### generateReceivingAddress(self, _account:str, _id:str='primary')

    def generateChangeAddress(self, _account:str='default', _id:str='primary'):
        """
        DESCRIPTION:

            Derive new change address for account.
        
        PARAMS:

            (*) Denotes required argument

            (*) _id       : Name of wallet.

            (*) _account  : BIP44 account to generate address from. Default = 'defualt'
        """
        
        endpoint = '/wallet/' + _id + '/change'

        _message = '{"account":"' + _account + '"}'

        response = self.post(endpoint, _message)
        return response
    ### END METHOD ################################### generateChangeAddress(self, _account:str='default', _id:str='primary')

    def getBalance(self, _account:str='', _id:str='primary'):
        """
        DESCRIPTION:

            Get wallet or account balance. If no account option is passed,
            the call defaults to wallet balance (with account index of -1).
            Balance values for `unconfirmed` and `confirmed` are expressed in
            subunits.
        
        PARAMS:

            (*) Denotes required argument

            (*) _account    : Address to get corresponding private key for.

            ( ) _id         : Wallet ID.
        """
        
        endpoint = '/wallet/' + _id + '/balance?account=' + _account
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getBalance(self, _account:str='', _id:str='primary')

    def listCoins(self, _id:str='primary'):
        """
        DESCRIPTION:

            List all wallet coins available.
        
        PARAMS:

            (*) Denotes required argument

            ( ) _id : Wallet ID.
        """
        
        endpoint = '/wallet/' + _id + '/coin'
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### listCoins(self, _id:str='primary')

    def lockCoinOutpoints(self, _txhash:str, _index:str='0', _id:str='primary'):
        """
        DESCRIPTION:

            Lock outpoints.
        
        PARAMS:

            (*) Denotes required argument

            (*) _txhash : Hash of transaction that created the outpoint.

            ( ) _index  : Index of the output in the transaction being referenced. Default = '0'

            ( ) _id     : ID of wallet that contains the outpoint. Default = 'primary'
        """

        endpoint = '/wallet/' + _id + '/locked/' + _txhash + '/' + _index
        response = self.put(endpoint)
        return response
    ### END METHOD ################################### lockCoinOutpoints(self, _txhash:str, _index:str='0', _id:str='primary')

    def createAccount(self, _passphrase:str, _id:str='primary', _name:str='', _accountkey:str='', _type:str='pubkeyhash', _m:int=1, _n:int=1):
        """
        DESCRIPTION:

            Create account with specified account name.
        
        PARAMS:

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
        
        endpoint = '/wallet/' + _id + '/account/' + _name

        _message = '{"type":"' + _type + '", "passphrase":"' + _passphrase + '", "accountKey":"' + _accountkey + '", "m": ' + str(_m) + ', "n": ' + str(_n) + '}'

        response = self.put(endpoint, _message)
        return response
    ### END METHOD ################################### createAccount(self, _id:str='primary', _passphrase:str, _name:str='', _accountkey:str='',
    #                                                                _type:str='pubkeyhash', _m:int=1, _n:int=1)