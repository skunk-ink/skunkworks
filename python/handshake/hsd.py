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
           HANDSHAKE PYTHON WRAPPER |:::/`-:::::;;-._ |:::::/::/
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

    def __init__(self, _api_key, _address, _port="12037"):
        global API_KEY
        global ADDRESS
        global PORT

        API_KEY = _api_key
        ADDRESS = _address
        PORT = _port

### BEGIN: GET methods
    def get(self, _endpoint):
        url = "http://x:" + API_KEY + "@" + ADDRESS + ":" + PORT + _endpoint
        print(url)
        getResponse = requests.get(url)
        response = getResponse.json() if getResponse and getResponse.status_code == 200 else None
        return response # Returned as json
    ### END METHOD ################################### get(_endpoint)

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

    def getMemPoolInvalid(self, _verbose='false'):
        """
        Description:
            Get mempool rejects filter (a Bloom filter used to store rejected TX hashes).
        
        
        Params:
        (*) Denotes required argument

        ( ) _verbose : (bool) Returns entire Bloom Filter in filter property, hex-encoded.
        """

        _verbose = _verbose.lower()
        if _verbose == "true":
            endpoint = '/mempool/invalid?verbose=' + _verbose
        else:
            endpoint = '/mempool/invalid'

        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getMemPoolInvalid(self)

    def getMemPoolInvalidHash(self, _hash):
        """
        Description:
            Test a TX hash against the mempool rejects filter.
        

        Params:
        (*) Denotes required argument
        
        (*) _hash : Transaction hash.
        """
        
        endpoint = '/mempool/invalid/' + _hash
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getMemPoolInvalidHash(self, _hash)

    def getBlockHashOrHeight(self, _blockHashOrHeight):
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
    ### END METHOD ################################### getBlockHashOrHeight(self, _blockHashOrHeight)

    def getHeaderHashOrHeight(self, _headerHashOrHeight):
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
    ### END METHOD ################################### getHeaderHashOrHeight(self _headerHashOrHeight)

    def getFeeEstimate(self, _blocks):
        """
        Description:
            Estimate the fee required (in dollarydoos per kB) for a
            transaction to be confirmed by the network within a targeted
            number of blocks (default 1).
        
        Params:
        (*) Denotes required argument
        
        (*) _blocks : Number of blocks to target confirmation.
        """
        
        endpoint = '/fee?blocks=' + _blocks
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getFeeEstimate(self, _blocks)

    def getCoinByHashIndex(self, _hash, _index):
        """
        Description:
            Get coin by outpoint (hash and index). Returns coin in hsd coin
            JSON format. value is always expressed in subunits.
        
        Params:
        (*) Denotes required argument
        
        (*) _hash  : Hash of tx.
        (*) _index : Output's index in tx.
        """
        
        endpoint = '/coin/' + hash + '/' + _hash + '/' + _index
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getCoinByHashIndex(self, _hash, _index)

    def getCoinByAddress(self, _address):
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
    ### END METHOD ################################### getCoinByAddress(self, _address)

    def getTxByHash(self, _txhash):
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
    ### END METHOD ################################### getTxHash(self, _hash)

    def getTxByAddress(self, _address):
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
    ### END METHOD ################################### getTxHash(self, _address)

    def rpc_getInfo(self):
        """
        Description:
            Returns general info.
        
        Params:
            None 
        """
        
        endpoint = '/'
        post_message = "{ 'method': 'stop' }"
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
    
    def rpc_getBlock(self, _hash, _verbose='true', _details='false'):
        """
        Description:
            Returns information about block.

        Params:
        (*) Denotes required argument
        
        (*) _hash    : Hash of the block.
        ( ) _verbose : If set to false, it will return hex of the block.
        ( ) _details : If set to true, it will return transaction details too.
        """

        _verbose = _verbose.lower()
        _details = _details.lower()
        
        endpoint = '/'
        post_message = '{ "method": "getblock", "params": [ ' + _hash + ', "' + _verbose + ', "' + _details + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getBlock(self, _hash, _verbose='true', _details='false')
    
    def rpc_getBlockByHeight(self, _blockheight, _verbose='true', _details='false'):
        """
        Description:
            Returns information about block by height.

        Params:
        (*) Denotes required argument
        
        (*) _hash : Hash of the block.
        ( ) _verbose : If set to false, it will return hex of the block.
        ( ) _details : If set to true, it will return transaction details too.
        """

        _verbose = _verbose.lower()
        _details = _details.lower()
        
        endpoint = '/'
        post_message = '{ "method": "getblockbyheight", "params": [ ' + _blockheight + ', "' + _verbose + ', "' + _details + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getBlockByHeight(self, _blockheight, _verbose='true', _details='false')
    
    def rpc_getBlockHash(self, _blockheight):
        """
        Description:
            Returns block's hash given its height.

        Params:
        (*) Denotes required argument
        
        (*) _blockheight : Height of the block in the blockchain.
        """
        
        endpoint = '/'
        post_message = '{ "method": "getblockhash", "params": [ ' + _blockheight + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getBlockHash(self, _blockheight)
    
    def rpc_getBlockHeader(self, _hash, _verbose='true'):
        """
        Description:
            Returns a block's header given its hash.

        Params:
        (*) Denotes required argument
        
        (*) _hash    : Hash of the block in the blockchain.
        ( ) _verbose : If set to false, it will return hex of the block.
        """

        _verbose = _verbose.lower()
        
        endpoint = '/'
        post_message = '{ "method": "getblockheader", "params": [ ' + _hash + ', "' + _verbose + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getBlockHeader(self, _hash, _verbose='true')
    
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
    
    def rpc_getMemPoolAncestors(self, _txhash, _verbose='false'):
        """
        Description:
            Returns all in-mempool ancestors for a transaction in the mempool.
        
        Params:
        (*) Denotes required argument
        
        (*) _txhash  : Transaction Hash.
        ( ) _verbose : False returns only tx hashs, true - returns dependency tx info.
        """

        _verbose = _verbose.lower()
        
        endpoint = '/'
        post_message = '{ "method": "getmempoolancestors", "params": [ ' + _txhash + ', "' + _verbose + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getMemPoolAncestors(self, _txhash, _verbose='false')
    
    def rpc_getMemPoolDescendants(self, _txhash, _verbose='false'):
        """
        Description:
            Returns all in-mempool descendants for a transaction in the mempool.
        
        Params:
        (*) Denotes required argument
        
        (*) _txhash  : Transaction Hash.
        ( ) _verbose : False returns only tx hashs, true - returns dependency tx info.
        """
        
        endpoint = '/'
        post_message = '{ "method": "getmempooldescendants", "params": [ ' + _txhash + ', "' + _verbose + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getMemPoolDescendants(self, _txhash, _verbose='false')
    
    def rpc_getMemPoolEntry(self, _txhash):
        """
        Description:
            Returns mempool transaction info by its hash.
        
        Params:
        (*) Denotes required argument
        
        (*) _txhash : Transaction Hash.
        """
        
        endpoint = '/'
        post_message = '{ "method": "getmempoolentry", "params": [ ' + _txhash + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getMemPoolEntry(self, _txhash)
    
    def rpc_getRawMemPool(self, _verbose='false'):
        """
        Description:
            Returns mempool detailed information (on verbose). Or mempool tx list.
        
        Params:
        (*) Denotes required argument
        
        ( ) _verbose : False returns only tx hashs, true - returns full tx info.
        """

        _verbose = _verbose.lower()
        
        endpoint = '/'
        post_message = '{ "method": "getrawmempool", "params": [ ' + _verbose + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getRawMemPool(self, _verbose='false')
    
    def rpc_prioritiseTransaction(self, _txhash, _priorityDelta, _feeDelta):
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
        post_message = '{ "method": "prioritisetransaction", "params": [ ' + _txhash + ', "' + _priorityDelta + ', "' + _feeDelta + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_prioritiseTransaction(self, _txhash, _priorityDelta, _feeDelta)
    
    def rpc_estimateFee(self, _nblocks=1):
        """
        Description:
            Estimates fee to be paid for transaction.
        
        Params:
        (*) Denotes required argument
        
        (*) _nblocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        post_message = '{ "method": "estimatefee", "params": [ ' + _nblocks + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_estimateFee(self, _nblocks=1)
    
    def rpc_estimatePriority(self, _nblocks=1):
        """
        Description:
            Estimates the priority (coin age) that a transaction
            needs in order to be included within a certain number
            of blocks as a free high-priority transaction.
        
        Params:
        (*) Denotes required argument
        
        (*) _nblocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        post_message = '{ "method": "estimatepriority", "params": [ ' + _nblocks + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_estimatePriority(self, _nblocks=1)
    
    def rpc_estimateSmartFee(self, _nblocks=1):
        """
        Description:
            Estimates smart fee to be paid for transaction.
        
        Params:
        (*) Denotes required argument
        
        (*) _nblocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        post_message = '{ "method": "estimatesmartfee", "params": [ ' + _nblocks + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_estimateSmartFee(self, _nblocks=1)
    
    def rpc_estimateSmartPriority(self, _nblocks=1):
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
        post_message = '{ "method": "estimatesmartpriority", "params": [ ' + _nblocks + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_estimateSmartPriority(self, _nblocks=1)
    
    def rpc_getTxOut(self, _txhash, _index, _includemempool='true'):
        """
        Description:
            Get outpoint of the transaction.
        
        Params:
        (*) Denotes required argument
        
        (*) _txhash         : Transaction hash.
        (*) _index          : Index of the Outpoint tx.
        (*) _includemempool : Whether to include mempool transactions.
        """

        _includemempool = _includemempool.lower()
        
        endpoint = '/'
        post_message = '{ "method": "gettxout", "params": [ ' + _txhash + ', "' + _index + ', "' + _includemempool + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_getTxOut(self, _txhash, _index, _includemempool='true')


###########################################################################################################


### BEGIN: POST methods ##############################
    def post(self, _endpoint, _post_message):
        """
        Description:
        
        
        Params:
            None
        """
        
        url = "http://x:" + API_KEY + "@" + ADDRESS + ":" + PORT + _endpoint
        postRequest = requests.post(url, _post_message)
        response = postRequest.json() if postRequest and postRequest.status_code == 200 else None
        return response # Returned as json
    ### END METHOD ################################### post(_endpoint, _post_message)

    def postBroadcast(self, _tx):
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
    ### END METHOD ################################### postBroadcast(self, _tx)

    def postBroadcastClaim(self, _claim):
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
    ### END METHOD ################################### postBroadcastClaim(self, _claim)

    def postReset(self, _height):
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
        post_message = '{ "height": ' + _height + '}'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### postReset(self, _height)

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

    def rpc_setLogLevel(self, _params=['none']): # _params = ['NONE', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'SPAM']
        """
        Description:
            Change Log level of the running node.
        
        Params:
        (*) Denotes required argument
        
        (*) _params : Level for the logger as dictionary array.
                      Levels are: NONE, ERROR, WARNING, INFO, DEBUG, SPAM 
        """
        
        endpoint = '/'
        post_message = '{ "method": "setloglevel", "params": "' + _params + '" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_postSetLogLevel(self, _params)

    def rpc_validateAddress(self, _address):
        """
        Description:
            Validates address.
        
        Params:
        (*) Denotes required argument
        
        (*) _address : Address to validate.
        """
        
        endpoint = '/'
        post_message = '{ "validateaddress": "", "params": "' + _address + '" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_postValidateAddress(self, _address)

    def rpc_createMultiSig(self, _nrequired, _keyDict):
        """
        Description:
            Create multisig address.
        
        Params:
        (*) Denotes required argument
        
        (*) _nrequired : Required number of approvals for spending.
        (*) _keyDict   : Dictionary of public keys.
        """
        
        endpoint = '/'
        post_message = '{ "method": "createmultisig", "params": [ ' + _nrequired + ', "' + _keyDict + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_postCreateMultiSig(self, _nrequired, _keyDict)

    def rpc_signMessageWithPrivKey(self, _privkey, _message):
        """
        Description:
            Signs message with private key. 
        
        Params:
        (*) Denotes required argument
        
        (*) _privkey : Private key.
        (*) _message : Message you want to sign.
        """
        
        endpoint = '/'
        post_message = '{ "method": "signmessagewithprivkey", "params": [ ' + _privkey + ', "' + _message + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### def rpc_postSignMessageWithPrivKey(self, _privkey, _message)

    def rpc_verifyMessage(self, _address, _signature, _message):
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
        post_message = '{ "method": "verifymessage", "params": [ ' + _address + ', "' + _signature + ', "' + _message + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_postVerifyMessage(self, _address, _signature, _message)

    def rpc_verifyMessageWithName(self, _name, _signature, _message):
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
        post_message = '{ "method": "verifymessagewithname", "params": [ ' + _name + ', "' + _signature + ', "' + _message + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_postVerifyMessageWithName(self, _name, _signature, _message)

    def rpc_setMockTime(self, _timestamp):
        """
        Description:
            Changes network time (This is consensus-critical)
        
        Params:
        (*) Denotes required argument
        
        (*) _timestamp : Timestamp to change to.
        """
        
        endpoint = '/'
        post_message = '{ "method": "setmocktime", "params": [ ' + _timestamp + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_postSetMockTime(self, _timestamp)

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
    
    def rpc_invalidateBlock(self, _blockhash):
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
        post_message = '{ "method": "", "params": [ ' + _blockhash + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_postInvalidateBlock(self, _blockhash)
    
    def rpc_reconsiderBlock(self, _blockhash):
        """
        Description:
            This rpc command will remove block from invalid block set.
        
        Params:
        (*) Denotes required argument
        
        (*) _blockhash : Block's hash.
        """
        
        endpoint = '/'
        post_message = '{ "method": "reconsiderblock", "params": [ ' + _blockhash + ' ]" }'
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### rpc_postReconsiderBlock(self, _blockhash)