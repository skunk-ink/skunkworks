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

import json
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

    def __init__(self, api_key:str, ip_address:str='127.0.0.1', port:int=12037):
        """
        DESCRIPTION:

            Initialization of the hsd class
        
        PARAMS:

        (*) Denotes required argument

        (*) api_key    : HSD API key.

        ( ) ip_address : HSD node ip. Default = '127.0.0.1'.

        ( ) port       : HSD node port. Defualt = 12037
        """

        self.API_KEY = api_key
        self.ADDRESS = ip_address
        self.PORT = str(port)
    ### END METHOD ################################### __init__(self, api_key:str, ip_address:str='127.0.0.1', port:int=12037)

    def get(self, endpoint:str):
        """
        DESCRIPTION:

            GET (json) response from API
        
        PARAMS:

        (*) Denotes required argument

        (*) endpoint : API endpoint to send GET request.
        """

        url = 'http://x:' + self.API_KEY + '@' + self.ADDRESS + ':' + self.PORT + endpoint

        get_response = requests.get(url)
        response = get_response.json()
        return response # Returned as json
    ### END METHOD ################################### get(self, endpoint:str)

    def post(self, endpoint:str, message:str=''):
        """
        DESCRIPTION:

            Send POST (json) message to API
        
        PARAMS:

        (*) Denotes required argument

        (*) endpoint : API endpoint to send POST message.

        (*) message  : Message to be sent.
        """
        
        url = 'http://x:' + self.API_KEY + '@' + self.ADDRESS + ':' + self.PORT + endpoint
 
        post_request = requests.post(url, message)
        response = post_request.json()
        return response # Returned as json
    ### END METHOD ################################### post(self, endpoint:str, message:str='')

    def getInfo(self):
        """
        DESCRIPTION:

            Get server Info.
        
        PARAMS:

            None
        """

        endpoint = '/'
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get server info'}"
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
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get snapshot of mempool'}"
        return response
    ### END METHOD ################################### getMemPool(self)

    def getMemPoolInvalid(self, verbose:bool=False):
        """
        DESCRIPTION:

            Get mempool rejects filter (a Bloom filter used to store rejected TX hashes).
        
        
        PARAMS:

        (*) Denotes required argument

        ( ) verbose : (bool) Returns entire Bloom Filter in filter property, hex-encoded.
        """

        if verbose == True:
            endpoint = '/mempool/invalid?verbose=true'
        else:
            endpoint = '/mempool/invalid'

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get invalid mempool transaction hashes'}"
        return response
    ### END METHOD ################################### getMemPoolInvalid(self, verbose:bool=False)

    def getMemPoolInvalidHash(self, tx_hash:str):
        """
        DESCRIPTION:

            Test a TX hash against the mempool rejects filter.
        

        PARAMS:

        (*) Denotes required argument
        
        (*) tx_hash : Transaction hash.
        """
        
        endpoint = '/mempool/invalid/' + tx_hash
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to check mempool for invalid hash'}"
        return response
    ### END METHOD ################################### getMemPoolInvalidHash(self, tx_hash:str)

    def getBlockByHashOrHeight(self, block_hash_or_height:str):
        """
        DESCRIPTION:

            Returns block info by block hash or height.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) block_hash_or_height : Hash or Height of block.
        """
        
        endpoint = '/block/' + block_hash_or_height
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get block by hash or height'}"
        return response
    ### END METHOD ################################### getBlockByHashOrHeight(self, block_hash_or_height:str)

    def getHeaderByHashOrHeight(self, header_hash_or_height:str):
        """
        DESCRIPTION:

            Returns block header by block hash or height.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) header_hash_or_height : Hash or Height of block.
        """
        
        endpoint = '/header/' + header_hash_or_height
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get header by hash or height'}"
        return response
    ### END METHOD ################################### getHeaderByHashOrHeight(self, header_hash_or_height:str)

    def broadcast(self, tx_hex:str):
        """
        DESCRIPTION:

            Broadcast a transaction by adding it to the node's mempool.
            If mempool verification fails, the node will still forcefully
            advertise and relay the transaction for the next 60 seconds.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) tx_hex : Raw transaction in hex.
        """
        
        endpoint = '/broadcast/'
        message = '{"tx": "' + tx_hex + '"}'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to broadcast transaction'}"
        return response
    ### END METHOD ################################### broadcast(self, tx_hex:str)

    def broadcastClaim(self, claim:str):
        """
        DESCRIPTION:

            Broadcast a claim by adding it to the node's mempool.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) claim : Raw claim in hex.
        """
        
        endpoint = '/claim/'
        message = '{ "claim": "' + claim + '" }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to broadcast claim'}"
        return response
    ### END METHOD ################################### broadcastClaim(self, claim:str)

    def getFeeEstimate(self, blocks:int):
        """
        DESCRIPTION:

            Estimate the fee required (in dollarydoos per kB) for a
            transaction to be confirmed by the network within a targeted
            number of blocks (default 1).
        
        PARAMS:

        (*) Denotes required argument
        
        (*) blocks : Number of blocks to target confirmation.
        """
        
        endpoint = '/fee?blocks=' + str(blocks)
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to estimate fee required for "' + blocks + '" blocks'}"
        return response
    ### END METHOD ################################### getFeeEstimate(self, blocks:int)

    def reset(self, height:int):
        """
        DESCRIPTION:

            Triggers a hard-reset of the blockchain. All blocks are disconnected
            from the tip down to the provided height. Indexes and Chain Entries
            are removed. Useful for "rescanning" an SPV wallet. Since there are
            no blocks stored on disk, the only way to _rescan the blockchain is to
            re-request [merkle]blocks from peers.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) height : Block height to reset chain to.
        """
        
        endpoint = '/reset'
        message = '{ "height": ' + str(height) + '}'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to hard-reset blockchain'}"
        return response
    ### END METHOD ################################### reset(self, height:int)

    def getCoinByHashIndex(self, tx_hash:str, index:int):
        """
        DESCRIPTION:

            Get coin by outpoint (hash and index). Returns coin in hsd coin
            JSON format. value is always expressed in subunits.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) tx_hash : Hash of tx.

        (*) index   : Output's index in tx.
        """
        
        endpoint = '/coin/' + hash + '/' + tx_hash + '/' + str(index)
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get coin from hash and index'}"
        return response
    ### END METHOD ################################### getCoinByHashIndex(self, tx_hash:str, index:int)

    def getCoinByAddress(self, address:str):
        """
        DESCRIPTION:

            Get coin objects array by address.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) address : Handshake address.
        """
        
        endpoint = '/coin/address/' + address
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get coins for address " + address + "'}"
        return response
    ### END METHOD ################################### getCoinByAddress(self, address:str)

    def getTxByHash(self, tx_hash:str):
        """
        DESCRIPTION:

           Returns transaction objects array by hash
        
        PARAMS:

        (*) Denotes required argument
        
        (*) tx_hash : Transaction hash.
        """
        
        endpoint = '/tx/' + tx_hash
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get transactions for hash " + tx_hash + "'}"
        return response
    ### END METHOD ################################### getTxByHash(self, tx_hash:str)

    def getTxByAddress(self, address:str):
        """
        DESCRIPTION:

           Returns transaction objects array by address.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) address : Handshake address.
        """
        
        endpoint = '/tx/address/' + address
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get transactions for address " + address + "'}"
        return response
    ### END METHOD ################################### getTxByAddress(self, address:str)

    def rpc_stop(self):
        """
        DESCRIPTION:

            Stops the running node.
        
        PARAMS:

            None
        """
        
        endpoint = '/'
        message = '{ "method": "stop" }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to stop node'}"
        return response
    ### END METHOD ################################### rpc_stop(self)

    def rpc_getInfo(self):
        """
        DESCRIPTION:

            Returns general info.
        
        PARAMS:

            None 
        """
        
        endpoint = '/'
        message = '{ "method": "getinfo" }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get information'}"
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
        message = '{ "method": "getmemoryinfo" }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get memory usage information'}"
        return response
    ### END METHOD ################################### rpc_getMemoryInfo(self)

    def rpc_setLogLevel(self, log_level:str='NONE'):
        """
        DESCRIPTION:

            Change Log level of the running node.

            Levels are: `NONE`, `ERROR`, `WARNING`, `INFO`, `DEBUG`, `SPAM`
        
        PARAMS:

            (*) Denotes required argument

            ( ) log_level : Level for the logger. Default = `NONE`
        """
        
        endpoint = '/'
        message = '{ "method": "setloglevel", "params": [ "' + log_level + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to set log level to " + log_level + "'}"
        return response
    ### END METHOD ################################### rpc_setLogLevel(self, log_level:str='NONE')

    def rpc_validateAddress(self, address:str):
        """
        DESCRIPTION:

            Validates address.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) address : Address to validate.
        """
        
        endpoint = '/'
        message = '{ "validateaddress": "", "params": [ "' + address + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to validate address " + address + "'}"
        return response
    ### END METHOD ################################### rpc_validateAddress(self, address:str)

    def rpc_createMultiSig(self, nrequired:int, key_dict:str):
        """
        DESCRIPTION:

            Create multisig address.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) nrequired : Required number of approvals for spending.

        (*) key_dict  : List array of public keys.
        """
        
        endpoint = '/'
        message = '{ "method": "createmultisig", "params": [ ' + str(nrequired) + ', "' + key_dict + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to create multisig address'}"
        return response
    ### END METHOD ################################### rpc_createMultiSig(self, nrequired:int, key_dict:str)

    def rpc_signMessageWithPrivKey(self, private_key:str, message:str):
        """
        DESCRIPTION:

            Signs message with private key. 
        
        PARAMS:
        (*) Denotes required argument
        
        (*) private_key : Private key.

        (*) message : Message you want to sign.
        """
        
        endpoint = '/'
        message = '{ "method": "signmessagewithprivkey", "params": [ "' + private_key + '", "' + message + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to sign message with private key'}"
        return response
    ### END METHOD ################################### rpc_signMessageWithPrivKey(self, private_key:str, message:str)

    def rpc_verifyMessage(self, address:str, signature:str, message:str):
        """
        DESCRIPTION:

            Verify signature.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) address   : Address of the signer.

        (*) signature : Signature of signed message.

        (*) message   : Message that was signed.
        """
        
        endpoint = '/'
        message = '{ "method": "verifymessage", "params": [ "' + address + '", "' + signature + '", "' + message + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to verify signature of address " + address + "'}"
        return response
    ### END METHOD ################################### rpc_verifyMessage(self, address:str, signature:str, message:str)

    def rpc_verifyMessageWithName(self, name:str, signature:str, message:str):
        """
        DESCRIPTION:

            Retrieves the address that owns a name and verifies signature.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) name      : Name to retrieve the address used to sign.

        (*) signature : Signature of signed message.

        (*) message   : Message that was signed.
        """
        
        endpoint = '/'
        message = '{ "method": "verifymessagewithname", "params": [ "' + name + '", "' + signature + '", "' + message + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to verify message for the name " + name + "'}"
        return response
    ### END METHOD ################################### rpc_verifyMessageWithName(self, name:str, signature:str, message:str)

    def rpc_setMockTime(self, timestamp:int):
        """
        DESCRIPTION:

            Changes network time (This is consensus-critical)
        
        PARAMS:

        (*) Denotes required argument
        
        (*) timestamp : Timestamp to change to.
        """
        
        endpoint = '/'
        message = '{ "method": "setmocktime", "params": [ ' + str(timestamp) + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to set network time to " + timestamp + "'}"
        return response
    ### END METHOD ################################### rpc_setMockTime(self, timestamp:int)

    def rpc_pruneBlockchain(self):
        """
        DESCRIPTION:

            Prunes the blockchain, it will keep blocks specified in Network Configurations.
        
        PARAMS:

            None
        """
        
        endpoint = '/'
        message = '{ "method": "pruneblockchain", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to prune the blockchain'}"
        return response
    ### END METHOD ################################### rpc_pruneBlockchain(self)
    
    def rpc_invalidateBlock(self, block_hash:str):
        """
        DESCRIPTION:

            Invalidates the block in the chain. It will rewind network to
            blockhash and invalidate it. It won't accept that block as valid.
            Invalidation will work while running,restarting node will remove
            invalid block from list.
        
        PARAMS:
        
        (*) Denotes required argument
        
        (*) block_hash : Block's hash.
        """
        
        endpoint = '/'
        message = '{ "method": "", "params": [ "' + block_hash + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to invalidate block hash " + block_hash + "'}"
        return response
    ### END METHOD ################################### rpc_invalidateBlock(self, block_hash:str)
    
    def rpc_reconsiderBlock(self, block_hash:str):
        """
        DESCRIPTION:

            This rpc command will remove block from invalid block set.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) block_hash : Block's hash.
        """
        
        endpoint = '/'
        message = '{ "method": "reconsiderblock", "params": [ "' + block_hash + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to remove block from hash " + block_hash + "'}"
        return response
    ### END METHOD ################################### rpc_reconsiderBlock(self, block_hash:str)

    def rpc_getBlockchainInfo(self):
        """
        DESCRIPTION:

            Returns blockchain information.
        
        PARAMS:

            None
        """
        
        endpoint = '/'
        message = '{ "method": "getblockchaininfo" }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get blockchain information'}"
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
        message = '{ "method": "getbestblockhash" }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get block hash at the tip'}"
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
        message = '{ "method": "getblockcount" }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to retreive current block count'}"
        return response
    ### END METHOD ################################### rpc_getBlockCount(self)
    
    def rpc_getBlock(self, block_hash:str, verbose:bool=True, details:bool=False):
        """
        DESCRIPTION:

            Returns information about block.

        PARAMS:

        (*) Denotes required argument
        
        (*) block_hash : Hash of the block.

        ( ) verbose    : (bool) If set to False, it will return hex of the block.

        ( ) details    : (bool) If set to True, it will return transaction details too.
        """

        _verbose = ''
        _details = ''

        if verbose == True:
            _verbose = '1'
        else:
            _verbose = '0'

        if details == True:
            _details = '1'
        else:
            _details = '0'
        
        endpoint = '/'
        message = '{ "method": "getblock", "params": [ "' + block_hash + '", ' + _verbose + ', ' + _details + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get information for the block hash " + block_hash + "'}"
        return response
    ### END METHOD ################################### rpc_getBlock(self, block_hash:str, verbose:bool=True, details:bool=False)
    
    def rpc_getBlockByHeight(self, block_height:int, verbose:bool=True, details:bool=False):
        """
        DESCRIPTION:

            Returns information about block by height.

        PARAMS:

        (*) Denotes required argument
        
        (*) block_height : Height of the block in the blockchain.

        ( ) verbose      : (bool) If set to True, it will return hex of the block.

        ( ) details      : (bool) If set to True, it will return transaction details too.
        """

        _verbose = ''
        _details = ''

        if verbose == True:
            _verbose = '1'
        else:
            _verbose = '0'

        if details == True:
            _details = '1'
        else:
            _details = '0'
        
        endpoint = '/'
        message = '{ "method": "getblockbyheight", "params": [ ' + str(block_height) + ', ' + _verbose + ', ' + _details + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get block at height " + block_height + "'}"
        return response
    ### END METHOD ################################### rpc_getBlockByHeight(self, block_height:int, verbose:bool=True, details:bool=False)
    
    def rpc_getBlockHash(self, block_height:int):
        """
        DESCRIPTION:

            Returns block's hash given its height.

        PARAMS:

        (*) Denotes required argument
        
        (*) block_height : Height of the block in the blockchain.
        """
        
        endpoint = '/'
        message = '{ "method": "getblockhash", "params": [ ' + str(block_height) + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get hash for the block at height " + block_height + "'}"
        return response
    ### END METHOD ################################### rpc_getBlockHash(self, block_height:int)
    
    def rpc_getBlockHeader(self, block_hash:str, verbose:bool=True):
        """
        DESCRIPTION:

            Returns a block's header given its hash.

        PARAMS:

        (*) Denotes required argument
        
        (*) block_hash : Hash of the block in the blockchain.

        ( ) verbose    : If set to False, it will return (hex) of the block.
        """

        _verbose = ''

        if verbose == True:
            _verbose = '1'
        else:
            _verbose = '0'
        
        endpoint = '/'
        message = '{ "method": "getblockheader", "params": [ "' + block_hash + '", ' + _verbose + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get block header for hash " + block_hash + "'}"
        return response
    ### END METHOD ################################### rpc_getBlockHeader(self, block_hash:str, verbose:bool=True)
    
    def rpc_getChainTips(self):
        """
        DESCRIPTION:

            Returns chaintips.
        
        PARAMS:

            None
        """
        
        endpoint = '/'
        message = '{ "method": "getchaintips" }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get chaintips'}"
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
        message = '{ "method": "getdifficulty" }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get current difficulty level'}"
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
        message = '{ "method": "getmempoolinfo" }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get information about mempool'}"
        return response
    ### END METHOD ################################### rpc_getMemPoolInfo(self)
    
    def rpc_getMemPoolAncestors(self, tx_hash:str, verbose:bool=False):
        """
        DESCRIPTION:

            Returns all in-mempool ancestors for a transaction in the mempool.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) tx_hash  : Transaction Hash.

        ( ) verbose : False returns only tx hashs, true - returns dependency tx info.
        """

        _verbose = ''

        if verbose == True:
            _verbose = '1'
        else:
            _verbose = '0'
        
        endpoint = '/'
        message = '{ "method": "getmempoolancestors", "params": [ "' + tx_hash + '", ' + _verbose + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get mempool ancestors for transaction hash " + tx_hash + "'}"
        return response
    ### END METHOD ################################### rpc_getMemPoolAncestors(self, tx_hash:str, verbose:bool=False)
    
    def rpc_getMemPoolDescendants(self, tx_hash:str, verbose:bool=False):
        """
        DESCRIPTION:

            Returns all in-mempool descendants for a transaction in the mempool.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) tx_hash  : Transaction Hash.

        ( ) verbose : False returns only tx hashs, true - returns dependency tx info.
        """

        _verbose = ''

        if verbose == True:
            _verbose = '1'
        else:
            _verbose = '0'
        
        endpoint = '/'
        message = '{ "method": "getmempooldescendants", "params": [ "' + tx_hash + '", ' + _verbose + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get mempool descendants for transaction hash " + tx_hash + "'}"
        return response
    ### END METHOD ################################### rpc_getMemPoolDescendants(self, tx_hash:str, verbose:bool=False)
    
    def rpc_getMemPoolEntry(self, tx_hash:str):
        """
        DESCRIPTION:

            Returns mempool transaction info by its hash.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) tx_hash : Transaction Hash.
        """
        
        endpoint = '/'
        message = '{ "method": "getmempoolentry", "params": [ "' + tx_hash + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get mempool entry for the transaction hash " + tx_hash + "'}"
        return response
    ### END METHOD ################################### rpc_getMemPoolEntry(self, tx_hash:str)
    
    def rpc_getRawMemPool(self, verbose:bool=False):
        """
        DESCRIPTION:

            Returns mempool detailed information (on verbose). Or mempool tx list.
        
        PARAMS:

        (*) Denotes required argument
        
        ( ) verbose : False returns only tx hashs, true - returns full tx info.
        """

        _verbose = ''

        if verbose == True:
            _verbose = '1'
        else:
            _verbose = '0'
        
        endpoint = '/'
        message = '{ "method": "getrawmempool", "params": [ ' + _verbose + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get raw mempool data'}"
        return response
    ### END METHOD ################################### rpc_getRawMemPool(self, verbose:bool=False)
    
    def rpc_prioritiseTransaction(self, tx_hash:str, priority_delta:int, fee_delta:int):
        """
        DESCRIPTION:

            Prioritises the transaction.

            Note: Changing fee or priority will only trick local miner (using this mempool) into
                accepting Transaction(s) into the block. (even if Priority/Fee doen't qualify)
        
        PARAMS:

        (*) Denotes required argument
        
        (*) tx_hash        : Transaction hash.

        (*) priority_delta : Virtual priority to add/subtract to the entry.

        (*) fee_delta      : Virtual fee to add/subtract to the entry.
        """
        
        endpoint = '/'
        message = '{ "method": "prioritisetransaction", "params": [ "' + tx_hash + '", "' + str(priority_delta) + '", "' + str(fee_delta) + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to prioritize the transaction hash " + tx_hash + "'}"
        return response
    ### END METHOD ################################### rpc_prioritiseTransaction(self, tx_hash:str, priority_delta:int, fee_delta:int)
    
    def rpc_estimateFee(self, n_blocks:int=1):
        """
        DESCRIPTION:

            Estimates fee to be paid for transaction.
        
        PARAMS:

        (*) Denotes required argument
        
        ( ) n_blocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        message = '{ "method": "estimatefee", "params": [ ' + str(n_blocks) + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to estimate fee for transaction of "' + n_blocks + '" blocks'}"
        return response
    ### END METHOD ################################### rpc_estimateFee(self, n_blocks:int=1)
    
    def rpc_estimatePriority(self, n_blocks:int=1):
        """
        DESCRIPTION:

            Estimates the priority (coin age) that a transaction
            needs in order to be included within a certain number
            of blocks as a free high-priority transaction.
        
        PARAMS:

        (*) Denotes required argument
        
        ( ) n_blocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        message = '{ "method": "estimatepriority", "params": [ ' + str(n_blocks) + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to estimate the priority of "' + n_blocks + '" blocks'}"
        return response
    ### END METHOD ################################### rpc_estimatePriority(self, n_blocks:int=1)
    
    def rpc_estimateSmartFee(self, n_blocks:int=1):
        """
        DESCRIPTION:

            Estimates smart fee to be paid for transaction.
        
        PARAMS:

        (*) Denotes required argument
        
        ( ) n_blocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        message = '{ "method": "estimatesmartfee", "params": [ ' + str(n_blocks) + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to estimate the smart fee for " + n_blocks + " blocks'}"
        return response
    ### END METHOD ################################### rpc_estimateSmartFee(self, n_blocks:int=1)
    
    def rpc_estimateSmartPriority(self, n_blocks:int=1):
        """
        DESCRIPTION:

            Estimates smart priority (coin age) that a transaction
            needs in order to be included within a certain number
            of blocks as a free high-priority transaction.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) n_blocks : Number of blocks to check for estimation.
        """
        
        endpoint = '/'
        message = '{ "method": "estimatesmartpriority", "params": [ ' + str(n_blocks) + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to estimate the smart priority for " + n_blocks + " blocks'}"
        return response
    ### END METHOD ################################### rpc_estimateSmartPriority(self, n_blocks:int=1)
    
    def rpc_getTxOut(self, tx_hash:str, index:int, include_mempool:int=1):
        """
        DESCRIPTION:

            Get outpoint of the transaction.
        
        PARAMS:
        
        (*) Denotes required argument
        
        (*) tx_hash         : Transaction hash.

        (*) index           : Index of the outpoint tx.

        ( ) include_mempool : Whether to include mempool transactions.
        """
        
        endpoint = '/'
        message = '{ "method": "gettxout", "params": [ "' + tx_hash + '", ' + str(index) + ', ' + str(include_mempool) + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get oupoint for the transaction hash " + tx_hash + "'}"
        return response
    ### END METHOD ################################### rpc_getTxOut(self, tx_hash:str, index:int, include_mempool:int=1)
    
    def rpc_getTxOutSetInfo(self):
        """
        DESCRIPTION:

            Returns information about UTXO's from Chain.
        
        PARAMS:

            None
        """

        endpoint = '/'
        message = '{ "method": "gettxoutsetinfo", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get UTXO information from chain'}"
        return response
    ### END METHOD ################################### rpc_getTxOutSetInfo(self)
    
    def rpc_getRawTransaction(self, tx_hash:str, verbose:bool=False):
        """
        DESCRIPTION:

            Returns raw transaction
        
        PARAMS:

        (*) Denotes required argument
        
        (*) tx_hash  : Transaction hash.

        ( ) verbose : Returns json formatted if true.
        """

        _verbose = ''

        if verbose == True:
            _verbose = '1'
        else:
            _verbose = '0'
        
        endpoint = '/'
        message = '{ "method": "getrawtransaction", "params": [ "' + tx_hash + '", ' + _verbose + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get raw transaction for hash " + tx_hash + "'}"
        return response
    ### END METHOD ################################### rpc_getRawTransaction(self, tx_hash:str, verbose:bool=False)
    
    def rpc_decodeRawTransaction(self, raw_tx:str):
        """
        DESCRIPTION:

            Decodes raw tx and provide chain info.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) raw_tx : Raw transaction hex.
        """
        
        endpoint = '/'
        message = '{ "method": "decoderawtransaction", "params": [ "' + raw_tx + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to decode raw transcation " + raw_tx + "'}"
        return response
    ### END METHOD ################################### rpc_decodeRawTransaction(self, raw_tx:str)
    
    def rpc_decodeScript(self, script:str):
        """
        DESCRIPTION:

            Decodes script.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) script : Script hex.
        """
        
        endpoint = '/'
        message = '{ "method": "decodescript", "params": [ "' + script + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to decond script " + script + "'}"
        return response
    ### END METHOD ################################### rpc_decodeScript(self, script:str)
    
    def rpc_sendRawTransaction(self, raw_tx:str):
        """
        DESCRIPTION:

            Sends raw transaction without verification.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) raw_tx : Raw transaction hex.
        """
        
        endpoint = '/'
        message = '{ "method": "sendrawtransaction", "params": [ "' + raw_tx + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to send raw transaction without verification'}"
        return response
    ### END METHOD ################################### rpc_sendRawTransaction(self, raw_tx:str)
    
    def rpc_createRawTransaction(self, tx_hash:str, tx_index:int, address:str, amount:int, data:str):
        """
        DESCRIPTION:

            Creates raw, unsigned transaction without any formal verification.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) tx_hash  : Transaction hash.

        (*) tx_index : Transaction outpoint index.

        (*) address  : Recipient address.

        (*) amount   : Amount to send in HNS (float).
        """

        endpoint = '/'
        message = '{ "method": "createrawtransaction", "params": [[{ "txid": "' + tx_hash + '", "vout": ' + str(tx_index) + ' }], { "' + address + '": ' + str(amount) + ', "data": "' + data + '" }] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to create raw unsigned transaction'}"
        return response
    ### END METHOD ################################### rpc_createRawTransaction(self, tx_hash:str, tx_index:int, address:str, amount:int, data:str)
    
    def rpc_signRawTransaction(self, raw_tx:str, tx_hash:str, tx_index:int, address:str, amount:int, private_key:str):
        """
        DESCRIPTION:

            Signs raw transaction.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) raw_tx      : Raw transaction.

        (*) tx_hash     : Transaction hash.

        (*) tx_index    : Transaction outpoint index.

        (*) address     : Address which received the output you're going to sign.

        (*) amount      : Amount the output is worth.

        ( ) private_key : List of private keys.
        """

        endpoint = '/'
        message = '{ "method": "signrawtransaction", "params": [ "' + raw_tx + '", [{ "txid": "' + tx_hash + '", "vout": ' + str(tx_index) + ', "address": "' + address + '", "amount": ' + str(amount) + ' }], [ "' + private_key + '" ]] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to sign raw transaction'}"
        return response
    ### END METHOD ################################### rpc_signRawTransaction(self, raw_tx:str, tx_hash:str, tx_index:int, address:str, amount:int, private_key:str)
    
    def rpc_getTxOutProof(self, tx_id_list:str):
        """
        DESCRIPTION:

            Checks if transactions are within block. Returns proof of transaction inclusion (raw MerkleBlock).
        
        PARAMS:

        (*) Denotes required argument
        
        (*) tx_id_list : List array of transaction ID's
        """

        endpoint = '/'
        message = '{ "method": "gettxoutproof", "params": [ "' + tx_id_list + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get proof for transactions " + tx_id_list + "'}"
        return response
    ### END METHOD ################################### rpc_getTxOutProof(self, tx_id_list:str)
    
    def rpc_verifyTxOutProof(self, proof:str):
        """
        DESCRIPTION:

            Checks the proof for transaction inclusion. Returns transaction hash if valid.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) proof : Proof of transaction inclusion (raw MerkleBlock).
        """

        endpoint = '/'
        message = '{ "method": "verifytxoutproof", "params": [ "' + proof + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to verify proof " + proof + "'}"
        return response
    ### END METHOD ################################### rpc_verifyTxOutProof(self, proof)
    
    def rpc_getNetworkHashPerSec(self, blocks:int=120, height:int=1):
        """
        DESCRIPTION:

            Returns the estimated current or historical network hashes per second, based on last blocks.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) blocks : Number of blocks to lookup.
        
        (*) height : Starting height for calculations.
        """

        endpoint = '/'
        message = '{ "method": "getnetworkhashps", "params": [ ' + str(blocks) + ', ' + str(height) + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to retreive historical hashes per second estimation'}"
        return response
    ### END METHOD ################################### rpc_getNetworkHashPerSec(self, blocks:int=120, height:int=1)
    
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
        message = '{ "method": "getmininginfo", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get mining information'}"
        return response
    ### END METHOD ################################### rpc_getMiningInfo(self)
    
    def rpc_getWork(self, data:str=[]):
        """
        DESCRIPTION:

            Returns hashing work to be solved by miner. Or submits solved block.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) data : Data to be submitted to the network.
        """

        endpoint = '/'
        message = '{ "method": "getworklp", "params": [ "' + data + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get hashing work'}"
        return response
    ### END METHOD ################################### rpc_getWork(self, data:str=[])
    
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
        message = '{ "method": "getworklp", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get work from long polling'}"
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
        message = '{ "method": "getblocktemplate", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get block template'}"
        return response
    ### END METHOD ################################### rpc_getBlockTemplate(self):
    
    def rpc_submitBlock(self, block_data:str):
        """
        DESCRIPTION:

            Adds block to chain.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) block_data : Mined block data (hex).
        """

        endpoint = '/'
        message = '{ "method": "submitblock", "params": [ "' + block_data + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to add block to chain'}"
        return response
    ### END METHOD ################################### rpc_submitBlock(self, block_data:str)
    
    def rpc_verifyBlock(self, block_data:str):
        """
        DESCRIPTION:

            Verifies the block data.
        
        PARAMS:
        (*) Denotes required argument
        
        (*) block_data : Mined block data (hex).
        """

        endpoint = '/'
        message = '{ "method": "verifyblock", "params": [ "' + block_data + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to verify block data'}"
        return response
    ### END METHOD ################################### rpc_verifyBlock(self, block_data:str)
    
    def rpc_setGenerate(self, mining:int=0, proc_limit:int=0):
        """
        DESCRIPTION:

            Will start the mining on CPU.
        
        PARAMS:

        (*) Denotes required argument
        
        ( ) mining    : 1 will start mining, 0 will stop. Default = 0

        ( ) proc_limit : 1 will set processor limit, 0 will remove limit. Default = 0
        """

        endpoint = '/'
        message = '{ "method": "setgenerate", "params": [ ' + str(mining) + ', ' + str(proc_limit) + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to set mining status'}"
        return response
    ### END METHOD ################################### rpc_setGenerate(self, mining:int=0, proc_limit:int=0)
    
    def rpc_getGenerate(self):
        """
        DESCRIPTION:

            Returns status of mining on Node.
        
        PARAMS:

            None
        """

        endpoint = '/'
        message = '{ "method": "getgenerate", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to return status of the mining node'}"
        return response
    ### END METHOD ################################### rpc_getGenerate(self)
    
    def rpc_generate(self, num_blocks:int=1):
        """
        DESCRIPTION:

            Mines numblocks number of blocks. Will return once all blocks are mined. CLI command may timeout before that happens.
        
        PARAMS:
        (*) Denotes required argument
        
        ( ) num_blocks : Number of blocks to mine.
        """

        endpoint = '/'
        message = '{ "method": "generate", "params": [' + str(num_blocks) + '] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to generate "' + num_blocks + '" blocks'}"
        return response
    ### END METHOD ################################### rpc_generate(self, num_blocks:int=1)
    
    def rpc_generateToAddress(self, address:str, num_blocks:int=1):
        """
        DESCRIPTION:

            Mines numblocks blocks, with address as coinbase.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) address   : Coinbase address for new blocks.

        ( ) num_blocks : Number of blocks to mine.
        """
        response = ""

        try:
            endpoint = '/'
            message = '{ "method": "generatetoaddress", "params": [ ' + str(num_blocks) + ', "' + address + '" ] }'
            response = self.post(endpoint, message)
        except (ValueError, TypeError):
            endpoint = '/'
            try:
                address = address['result']
                message = '{ "method": "generatetoaddress", "params": [ ' + str(num_blocks) + ', "' + address + '" ] }'
                response = self.post(endpoint, message)
            except KeyError as e:
                print('hsd.rpc_GenerateToAddress() Error: The key ' + str(e) + " was not located in JSON.")
            except:
                response = {}
                response['error'] = "{'message': 'RPC failed to generate "' + num_blocks + '" blocks for the address " + address + "'}"
        return response
    ### END METHOD ################################### rpc_generateToAddress(self, address:str, num_blocks:int=1)
    
    def rpc_getConnectionCount(self):
        """
        DESCRIPTION:

            Returns connection count.
        
        PARAMS:

            None
        """

        endpoint = '/'
        message = '{ "method": "getconnectioncount", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get peer connection count'}"
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
        message = '{ "method": "ping", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to ping connected peers'}"
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
        message = '{ "method": "getpeerinfo", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get information for connected peers'}"
        return response
    ### END METHOD ################################### rpc_getPeerInfo(self)
    
    def rpc_addNode(self, node_address:str, cmd:str):
        """
        DESCRIPTION:

            Adds or removes peers in Host List. 
        
        PARAMS:

        (*) Denotes required argument
        
        (*) node_address : IP Address of the Node. Eg. '127.0.0.1:14038'

        (*) cmd          : 'add' - Adds node to Host List and connects to it.

                           'onetry' - Tries to connect to the given node.

                           'remove' - Removes node from host list.
        """

        endpoint = '/'
        message = '{ "method": "addnode", "params": [ "' + node_address + '", "' + cmd + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to "' + cmd + '" node for address " + node_address + "'}"
        return response
    ### END METHOD ################################### rpc_addNode(self, node_address:str, cmd:str)
    
    def rpc_disconnectNode(self, node_address:str):
        """
        DESCRIPTION:

            Disconnects node.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) address : IP Address of the Node. Eg. '127.0.0.1:14038'
        """

        endpoint = '/'
        message = '{ "method": "disconnectnode", "params": [ "' + node_address + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to disconnect node at address " + node_address + "'}"
        return response
    ### END METHOD ################################### rpc_disconnectNode(self, node_address:str)
    
    def rpc_getAddedNodeInfo(self, node_address:str):
        """
        DESCRIPTION:

            Returns node information from host list.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) address : IP Address of the Node. Eg. '127.0.0.1:14038'
        """

        endpoint = '/'
        message = '{ "method": "getaddednodeinfo", "params": [ "' + node_address + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get node information for the node address " + node_address + "'}"
        return response
    ### END METHOD ################################### rpc_getAddedNodeInfo(self, node_address:str)
    
    def rpc_getNetTotals(self):
        """
        DESCRIPTION:

            Returns information about used network resources.
        
        PARAMS:

            None
        """

        endpoint = '/'
        message = '{ "method": "getnettotals", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get information about used network resources'}"
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
        message = '{ "method": "getnetworkinfo", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get network info for local node'}"
        return response
    ### END METHOD ################################### def rpc_getNetworkInfo(self)
    
    def rpc_setBan(self, node_address:str, cmd:str):
        """
        DESCRIPTION:

            Adds or removes nodes from banlist.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) node_address : IP Address of the Node. Eg. '127.0.0.1:14038'

        (*) cmd         : 'add' - Adds node to ban list, removes from host list, disconnects.

                           'remove' - Removes node from ban list.
        """

        endpoint = '/'
        message = '{ "method": "setban", "params": ["' + node_address + '", "' + cmd + '"] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to ' + cmd + ' ban for node at address " + node_address + "'}"
        return response
    ### END METHOD ################################### rpc_setBan(self, node_address:str, cmd:str)
    
    def rpc_listBan(self):
        """
        DESCRIPTION:

            Lists all banned peers.
        
        PARAMS:

            None
        """

        endpoint = '/'
        message = '{ "method": "listbanned", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get list of banned peers'}"
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
        message = '{ "method": "clearbanned", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'PRC failed to remove banned peers'}"
        return response
    ### END METHOD ################################### rpc_clearBanned(self)
    
    def rpc_getNameInfo(self, name:str=''):
        """
        DESCRIPTION:

            Returns information on a given name. Use this function to query any name in any state.
        
        PARAMS:

        (*) Denotes required argument

        (*) name : Name you wish to look up.
        """

        endpoint = '/'
        message = '{ "method": "getnameinfo", "params": [ "' + name + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get information for name " + name + "'}"
        return response
    ### END METHOD ################################### rpc_getNameInfo(self, name:str='')
    
    def rpc_getNameByHash(self, name_hash:str=''):
        """
        DESCRIPTION:

            Returns the name for a from a given name hash.
        
        PARAMS:

        (*) Denotes required argument

        (*) name_hash : Name hash you wish to look up.
        """

        endpoint = '/'
        message = '{ "method": "getnamebyhash", "params": [ "' + name_hash + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get the name for the hash " + name_hash + "'}"
        return response
    ### END METHOD ###################################  rpc_getNameByHash(self, name_hash:str='')
    
    def rpc_getNameResource(self, name:str=''):
        """
        DESCRIPTION:

            Returns the resource records for the given name (added to the trie by the name owner using sendupdate).
        
        PARAMS:

        (*) Denotes required argument

        (*) name : Name for resource records.
        """

        endpoint = '/'
        message = '{ "method": "getnameresource", "params": [ "' + name + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get resource records for name " + name + "'}"
        return response
    ### END METHOD ################################### rpc_getNameResource(self, name:str='')
    
    def rpc_getNameProof(self, name:str=''):
        """
        DESCRIPTION:

            Returns the merkle tree proof for a given name.
        
        PARAMS:

        (*) Denotes required argument

        (*) name : Domain name you to retreive the proof for.
        """

        endpoint = '/'
        message = '{ "method": "getnameproof", "params": [ "' + name + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get name proof for name " + name + "'}"
        return response
    ### END METHOD ################################### rpc_getNameProof(self, name:str='')
    
    def rpc_sendRawClaim(self, base64_string:str):
        """
        DESCRIPTION:

            If you already have DNSSEC setup, you can avoid publishing a
            TXT record publicly by creating the proof locally. This requires
            that you have direct access to your zone-signing keys. The
            private keys themselves must be stored in BIND's private key
            format and naming convention.
        
        PARAMS:

        (*) Denotes required argument

        (*) base64_string : Raw serialized base64-string.
        """

        endpoint = '/'
        message = '{ "method": "sendrawclaim", "params": [ "' + base64_string + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to send raw claim'}"
        return response
    ### END METHOD ################################### rpc_sendRawClaim(self, base64_string:str='')
    
    def rpc_getDnsSecProof(self, name:str='', estimate:bool=False, verbose:bool=True):
        """
        DESCRIPTION:

            Adds or removes nodes from banlist.
        
        PARAMS:

        (*) Denotes required argument
        
        (*) name     : Domain name.

        ( ) estimate : No validation when True.

        ( ) verbose  : Returns (hex) when False.
        """
        
        _estimate = ''
        _verbose = ''

        if verbose == True:
            _verbose = '1'
        else:
            _verbose = '0'

        if estimate == True:
            _estimate = '1'
        else:
            _estimate = '0'

        endpoint = '/'
        message = '{ "method": "getdnssecproof", "params": ["' + name + '", ' + _estimate + ', ' + _verbose + '] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get DNS security proof'}"
        return response
    ### END METHOD ################################### rpc_getDnsSecProof(self, name:str='', estimate:bool=False, verbose:bool=True)
    
    def rpc_sendRawAirdrop(self, base64_string:str=''):
        """
        DESCRIPTION:

            Airdrop proofs create brand new coins directly
            to a Handshake address.
        
        PARAMS:

        (*) Denotes required argument

        (*) base64_string : Raw serialized base64-string.
        """

        endpoint = '/'
        message = '{ "method": "sendrawairdrop", "params": [ "' + base64_string + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to send raw airdrom'}"
        return response
    ### END METHOD ################################### rpc_sendRawAirdrop(self, base64_string:str='')
    
    def rpc_grindName(self, length:int=10):
        """
        DESCRIPTION:

            Grind a rolled-out available name.
        
        PARAMS:

        (*) Denotes required argument

        (*) length : Length of name to generate.
        """

        endpoint = '/'
        message = '{ "method": "grindname", "params": [ ' + str(length) + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to grind name'}"
        return response
    ### END METHOD ################################### rpc_grindName(self, length:int=10)


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

    def __init__(self, api_key:str, ip_address:str='127.0.0.1', port:int=12039):
        """
        DESCRIPTION:

            Initialization of the hsw class
        
        PARAMS:

        (*) Denotes required argument

        (*) api_key    : HSW API key.

        ( ) ip_address : HSW node ip. Default = '127.0.0.1'.

        ( ) port       : HSW node port. Default = 12039
        """

        self.API_KEY = api_key
        self.ADDRESS = ip_address
        self.PORT = str(port)
    ### END METHOD ################################### __init__(self, api_key:str, ip_address:str='127.0.0.1', port:int=12039):

    def get(self, endpoint:str):
        """
        DESCRIPTION:

            GET (json) response from API
        
        PARAMS:

        (*) Denotes required argument

        (*) endpoint : API endpoint to send GET request.
        """

        url = 'http://x:' + self.API_KEY + '@' + self.ADDRESS + ':' + self.PORT + endpoint

        get_response = requests.get(url)
        response = get_response.json()
        return response # Returned as json
    ### END METHOD ################################### get(self, endpoint:str)

    def post(self, endpoint:str, message:str=''):
        """
        DESCRIPTION:

            POST (json) message to API
        
        PARAMS:

        (*) Denotes required argument

        (*) endpoint : API endpoint to send POST message.

        (*) message  : Message to be sent.
        """
        
        url = 'http://x:' + self.API_KEY + '@' + self.ADDRESS + ':' + self.PORT + endpoint

        post_request = requests.post(url, message)
        response = post_request.json()
        return response # Returned as json
    ### END METHOD ################################### post(self, endpoint:str, message:str='')

    def put(self, endpoint:str, message:str=''):
        """
        DESCRIPTION:

            Send PUT (json) message to API
        
        PARAMS:

        (*) Denotes required argument

        (*) endpoint : API endpoint to send POST message.

        (*) message  : Message to be sent.
        """
        
        url = 'http://x:' + self.API_KEY + '@' + self.ADDRESS + ':' + self.PORT + endpoint

        putRequest = requests.put(url, message)
        response = putRequest.json()
        return response # Returned as json
    ### END METHOD ################################### put(self, endpoint:str, message:str='')

    def delete(self, endpoint:str, message:str=''):
        """
        DESCRIPTION:

            Send DELETE (json) message to API
        
        PARAMS:

        (*) Denotes required argument

        (*) endpoint : API endpoint to send POST message.

        (*) message  : Message to be sent.
        """
        
        url = 'http://x:' + self.API_KEY + '@' + self.ADDRESS + ':' + self.PORT + endpoint
    
        putRequest = requests.delete(url, message)
        response = putRequest.json()
        return response # Returned as json
    ### END METHOD ################################### delete(self, endpoint:str, message:str='')

    def createWallet(self, passphrase:str, id:str='primary', account_key:str='', type:str='pubkeyhash',
                    mnemonic:str='', master:str='', watch_only:bool=True, m:int=1, n:int=1):
        """
        DESCRIPTION:

            Create a new wallet with a specified ID.
        
        PARAMS:

            (*) Denotes required argument

            (*) id          : Wallet ID (used for storage).

            ( ) type        : Type of wallet (pubkeyhash, multisig). Default is 'pubkeyhash'

            ( ) master      : Master HD key. If not present, it will be generated.

            ( ) mnemonic    : A mnemonic phrase to use to instantiate an hd private key. One will be generated if none provided.

            ( ) m           : 'm' value for multisig (m-of-n).

            ( ) n           : 'n' value for multisig (m-of-n)

            (*) passphrase  : A strong passphrase used to encrypt the wallet.

            ( ) watch_only  : Watch for CLI. Default set to True.

            (*) account_key : The extended public key for the primary account in the new wallet. This value is ignored if _watch_only is false (key for CLI).
        """
        
        _watch_only = ''

        if watch_only == True:
            _watch_only = '1'
        else:
            _watch_only = '0'

        endpoint = '/wallet/' + id

        message = '{"passphrase":"' + passphrase + '", "_watch_only": ' + str(_watch_only) + ', "accountKey":"' + account_key + \
                       '", "type":"' + type + '", "master":"' + master + '", "m": ' + str(m) + ', "n": ' + str(n) + ', "mnemonic":"' + mnemonic + '"}'
        try:
            response = self.put(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to create new wallet'}"
        return response
    ### END METHOD ################################### createWallet(self, id:str='primary', passphrase:str, account_key:str='', type:str='pubkeyhash',
    #                                                               mnemonic:str='',master:str=None, watch_only:bool=True, m:int=1, n:int=1)

    def resetAuthToken(self, passphrase:str, id:str='primary'):
        """
        DESCRIPTION:

            Create a new wallet with a specified ID.
        
        PARAMS:

            (*) Denotes required argument

            (*) id         : Wallet ID.

            (*) passphrase : A strong passphrase used to encrypt the wallet.
        """
        
        endpoint = '/wallet/' + id + '/retoken'

        message = '{"passphrase":"' + passphrase + '"}'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to reset auth token for the wallet " + id + "'}"
        return response
    ### END METHOD ################################### resetAuthToken(self, id:str='primary', passphrase:str)

    def getWalletInfo(self, id:str=''):
        """
        DESCRIPTION:

            Get wallet info by ID. If no id is passed in the CLI it assumes an id of primary.
        
        PARAMS:

            (*) Denotes required argument

            ( ) id : Name of the wallet whose info you would like to retrieve.
        """
        
        endpoint = '/wallet/' + id
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get info for wallet " + id + "'}"
        return response
    ### END METHOD ################################### getWalletInfo(self, id:str='')

    def getMasterHDKey(self, id:str='primary'):
        """
        DESCRIPTION:

            Get wallet master HD key. This is normally censored in the
            wallet info route.The provided API key must have admin access.
        
        PARAMS:

            (*) Denotes required argument

            (*) id : Name of the wallet whose info you would like to retrieve.
        """
        
        endpoint = '/wallet/' + id + '/master'

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get master HD key'}"
        return response
    ### END METHOD ################################### getMasterHDKey(self, id:str='')

    def changePassword(self, new_passphrase:str, id:str='primary', old_passphrase:str=''):
        """
        DESCRIPTION:

            Change wallet passphrase. Encrypt if unencrypted.
        
        PARAMS:

            (*) Denotes required argument

            (*) id             : Wallet ID.

            ( ) old_passphrase : Old passphrase. Pass in empty string if none.

            (*) new_passphrase : New passphrase.
        """
        
        endpoint = '/wallet/' + id + '/passphrase'

        message = '{"old":"' + old_passphrase + '", "passphrase":"' + new_passphrase + '"}'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to change password'}"
        return response
    ### END METHOD ################################### changePassword(self, id:str='primary', new_passphrase:str, old_passphrase:str='')

    def signTransaction(self, passphrase:str, tx_hex:str, id:str='primary'):
        """
        DESCRIPTION:

            Sign a templated transaction (useful for multisig).
 
            (*) id         : Wallet ID.

            (*) passphrase : Passphrase to unlock the wallet.

            (*) tx_hex     : The (hex) of the transaction you would like to sign.
        """
        
        endpoint = '/wallet/' + id + '/sign'

        message = '{"tx":"' + tx_hex + '", "passphrase":"' + passphrase + '"}'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to sign transaction (hex) " + tx_hex + "'}"
        return response
    ### END METHOD ################################### signTransaction(self, id:str='primary', passphrase:str, tx_hex:str)

    def sendTransaction(self, id:str, passphrase:str, rate:int, value:float=None, smart:bool=False, blocks:int=None, max_fee:int=None, subtract_fee:bool=False,
                        subtract_index:int=None, selection:str='all', depth:int=None, address:str=''):
        """
        Description:

            Create, sign, and send a transaction.
        
        Params:

            (*) Denotes required argument

            (*) id             : Account to use for transaction.

            (*) passphrase     : Passphrase to unlock the account.

            (*) rate           : The rate for transaction fees. Denominated in subunits per kb.

            ( ) value          : Value to send in subunits (or whole HNS, see warning above).

            ( ) smart          : Whether or not to choose smart coins, will also used unconfirmed transactions.

            ( ) blocks         : Number of blocks to use for fee estimation.

            ( ) max_fee        : Maximum fee you're willing to pay.

            ( ) subtract_fee   : Whether to subtract fee from outputs (evenly).

            ( ) subtract_index : Subtract only from specified output index.

            ( ) selection      : How to select coins.

            ( ) depth          : Number of confirmation for coins to spend.

            ( ) address        : Destination address for transaction.
        """

        _smart = ''
        _subtract_fee = ''

        if smart == True:
            _smart = '1'
        else:
            _smart = '0'

        if subtract_fee == True:
            _subtract_fee = '1'
        else:
            _subtract_fee = '0'

        outputs = '[{"address":"' + address + '", "value":' + str(value) + ', "smart":' + _smart + ', "blocks":' + str(blocks) + \
                 ', "maxFee":' + str(max_fee) + ', "_subtract_fee":' + _subtract_fee + ', "subtractIndex":' + str(subtract_index) + \
                 ', "selection":"' + selection + '", "depth":' + str(depth) + '}]'
        
        print(outputs)

        endpoint = '/wallet/' + id + "/send"

        message = '{"passphrase":"' + passphrase + '", "rate":' + str(rate) + ', "outputs": [' + outputs + ']}'

        response = self.post(endpoint, message)
        return response
    ### END METHOD ################################### def sendTransaction(self, id:str, new_passphrase:str, old_passphrase:str='')

    def createTransaction(self, id:str, passphrase:str, rate:int, value:float=None, smart:bool=False, blocks:int=None, max_fee:int=None, subtract_fee:bool=False,
                        subtract_index:int=None, selection:str='all', depth:int=None, address:str=''):
        """
        Description:

            Create and template a transaction (useful for multisig). Does not broadcast or add to wallet.
        
        Params:

            (*) Denotes required argument

            (*) id             : Account to use for transaction.

            (*) passphrase     : Passphrase to unlock the account.

            (*) rate           : The rate for transaction fees. Denominated in subunits per kb.

            ( ) value          : Value to send in subunits (or whole HNS, see warning above).

            ( ) smart          : Whether or not to choose smart coins, will also used unconfirmed transactions.

            ( ) blocks         : Number of blocks to use for fee estimation.

            ( ) max_fee        : Maximum fee you're willing to pay.

            ( ) subtract_fee   : Whether to subtract fee from outputs (evenly).

            ( ) subtract_index : Subtract only from specified output index.

            ( ) selection      : How to select coins.

            ( ) depth          : Number of confirmation for coins to spend.

            ( ) address        : Destination address for transaction.
        """

        _smart = ''
        _subtract_fee = ''

        if smart == True:
            _smart = '1'
        else:
            _smart = '0'

        if subtract_fee == True:
            _subtract_fee = '1'
        else:
            _subtract_fee = '0'

        outputs = '[{"address":"' + address + '", "value":' + str(value) + ', "smart":' + _smart + ', "blocks":' + str(blocks) + \
                 ', "maxFee":' + str(max_fee) + ', "_subtract_fee":' + _subtract_fee + ', "subtractIndex":' + str(subtract_index) + \
                 ', "selection":"' + selection + '", "depth":' + str(depth) + '}]'
        
        print(outputs)

        endpoint = '/wallet/' + id + "/create"

        message = '{"passphrase":"' + passphrase + '", "rate":' + str(rate) + ', "outputs": [' + outputs + ']}'

        response = self.post(endpoint, message)
        return response
    ### END METHOD ################################### createTransaction(self, id:str, passphrase:str, rate:int, value:float=None, smart:bool=False, blocks:int=None, max_fee:int=None, subtract_fee:bool=False,
    #                                                                        subtract_index:int=None, selection:str='all', depth:int=None, address:str=''):

    def zapTransactions(self, account:str, id:str='primary', age:int=0):
        """
        DESCRIPTION:

            Remove all pending transactions older than a specified age.
        
        PARAMS:

            (*) Denotes required argument

            (*) id      : Wallet ID.

            ( ) account : Account to zap from.

            (*) age     : Age threshold to zap up to (seconds).
        """
        
        endpoint = '/wallet/' + id + '/zap'

        message = '{"account":"' + account + '", "age":"' + age + '"}'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to zap transaction for account " + account + "'}"
        return response
    ### END METHOD ################################### zapTransactions(self, account:str, id:str='primary', age:int=0)

    def lockWallet(self, id:str='primary'):
        """
        DESCRIPTION:

            If unlock was called, zero the derived AES key and revert to normal behavior.
        
        PARAMS:

            (*) Denotes required argument

            ( ) id : Name ID of wallet to lock.
        """
        
        endpoint = '/wallet/' + id + '/lock'

        message = ''
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to lock wallet "  + id + "'}"
        return response
    ### END METHOD ################################### lockWallet(self, id:str='primary')

    def importPublicKey(self, account:str, public_key:str, id:str='primary'):
        """
        DESCRIPTION:

            Import a standard (public) WIF key.

            A _rescan will be required to see any transaction history associated with the key.
            
            Note: Imported keys do not exist anywhere in the wallet's HD tree.They can be
                  associated with accounts but will not be properly backed up with only the
                  mnemonic. 
        
        PARAMS:

            (*) Denotes required argument

            (*) id         : ID of target wallet to import key into.

            ( ) public_key : Hex encoded public key.
        """
        
        endpoint = '/wallet/' + id + '/import'

        message = '{"account":"' + account + '", "publicKey":"' + public_key + '"}'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to import public key for account " + account + "'}"
        return response
    ### END METHOD ################################### importPublicKey(self, account:str, public_key:str, id:str='primary')

    def importPrivateKey(self, account:str, private_key:str, id:str='primary'):
        """
        DESCRIPTION:

            Import a standard (private) WIF key.

            A _rescan will be required to see any transaction history associated with the key.
            
            Note: Imported keys do not exist anywhere in the wallet's HD tree.They can be
                  associated with accounts but will not be properly backed up with only the
                  mnemonic. 
        
        PARAMS:

            (*) Denotes required argument

            (*) id          : ID of target wallet to import key into.

            ( ) private_key : Hex encoded public key.
        """
        
        endpoint = '/wallet/' + id + '/import'

        message = '{"account":"' + account + '", "privateKey":"' + private_key + '"}'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to import private key for account " + account + "'}"
        return response
    ### END METHOD ################################### importPrivateKey(self, account:str, private_key:str, id:str='primary')

    def importAddress(self, account:str, address:str):
        """
        Description:

            Import a Bech32 encoded address. Addresses (like public keys)
            can only be imported into watch-only wallets

            The HTTP endpoint is the same as for key imports.
        
        Params:

            (*) Denotes required argument

            (*) account : Wallet ID.

            ( ) address : Hex encoded public key.
        """
        
        endpoint = '/wallet/watchonly1/import'

        message = '{"account":"' + account + '", "address":"' + address + '"}'

        response = self.post(endpoint, message)
        return response
    ### END METHOD ################################### importAddress(self, account:str, address:str)

    def getBlocksWithWalletTX(self, id:str='primary'):
        """
        DESCRIPTION:

            List all block heights which contain any wallet transactions. Returns an array of block heights.
        
        PARAMS:

            (*) Denotes required argument

            (*) id : Name of the wallet.
        """
        
        endpoint = '/wallet/' + id + '/block'
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get blocks with existing wallet transactions'}"
        return response
    ### END METHOD ################################### getBlocksWithWalletTX(self, id:str='primary')

    def getWalletBlockByHeight(self, height:int, id:str='primary'):
        """
        DESCRIPTION:

            Get block info by height.
        
        PARAMS:

            (*) Denotes required argument

            (*) height : Height of block being queried.

            ( ) id     : Name of the wallet.
        """
        
        endpoint = '/wallet/' + id + '/block/' + str(height)
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get wallet block at height " + height + "'}"
        return response
    ### END METHOD ################################### getWalletBlockByHeight(self, height:int, id:str='primary')

    def addXPubKey(self, account_key:str, account:str='default'):
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

            (*) account_key : xpubkey to add to the multisig wallet.

            ( ) account     : Multisig account to add the xpubkey to (default='default').
        """

        endpoint = '/wallet/multisig3/shared-key/'

        message = '{"accountKey":"' + account_key + '", "account":"' + account + '"}'
        try:
            response = self.put(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to add xpubkey " + account_key + " for account " + account + "'}"
        return response
    ### END METHOD ################################### addXPubKey(self, account_key:str, account:str='default')

    def removeXPubKey(self, account_key:str, account:str='default'):
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

            (*) account_key : xpubkey to add to the multisig wallet.

            ( ) account     : Multisig account to remove the xpubkey from (default='default').
        """

        endpoint = '/wallet/multisig3/shared-key/'

        message = '{"accountKey":"' + account_key + '", "account":"' + account + '"}'
        try:
            response = self.delete(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to remove xpubkey "' + account_key + '" for account " + account + "'}"
        return response
    ### END METHOD ################################### removeXPubKey(self, account_key:str, account:str='default')

    def getPublicKeyByAddress(self, address:str, id:str='primary'):
        """
        DESCRIPTION:

            Get wallet key by address. Returns wallet information with address and public key.
        
        PARAMS:

            (*) Denotes required argument

            (*) address : Bech32 encoded address to get corresponding public key for.

            ( ) id      : Name of wallet.
        """
        
        endpoint = '/wallet/' + id + '/key/' + address
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get public key for address " + address + "'}"
        return response
    ### END METHOD ################################### getPublicKeyByAddress(self, address:str, id:str='primary')

    def getPrivateKeyByAddress(self, address:str, passphrase:str, id:str='primary'):
        """
        DESCRIPTION:

            Get wallet private key (WIF format) by address. Returns just the private key.
        
        PARAMS:

            (*) Denotes required argument

            (*) address    : Address to get corresponding private key for.

            (*) passphrase : Passphrase of wallet.

            ( ) id         : Name of wallet.
        """
        
        endpoint = '/wallet/' + id + '/wif/' + address + '?passphrase=' + passphrase
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get private key for address " + address + "'}"
        return response
    ### END METHOD ################################### getPrivateKeyByAddress(self, address:str, passphrase:str, id:str='primary')

    def generateReceivingAddress(self, account:str, id:str='primary'):
        """
        DESCRIPTION:

            Derive new receiving address for account.
        
        PARAMS:

            (*) Denotes required argument

            (*) id       : Name of wallet.

            ( ) account  : BIP44 account to generate address from.
        """
        
        endpoint = '/wallet/' + id + '/address'

        message = '{"account":"' + account + '"}'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to generate receiving address for account " + account + "'}"
        return response
    ### END METHOD ################################### generateReceivingAddress(self, account:str, id:str='primary')

    def generateChangeAddress(self, account:str='default', id:str='primary'):
        """
        DESCRIPTION:

            Derive new change address for account.
        
        PARAMS:

            (*) Denotes required argument

            ( ) id       : Name of wallet.

            ( ) account  : BIP44 account to generate address from. Default = 'defualt'
        """
        
        endpoint = '/wallet/' + id + '/change'

        message = '{"account":"' + account + '"}'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to generate change address for account " + account + "'}"
        return response
    ### END METHOD ################################### generateChangeAddress(self, account:str='default', id:str='primary')

    def getBalance(self, account:str='', id:str='primary'):
        """
        DESCRIPTION:

            Get wallet or account balance. If no account option is passed,
            the call defaults to wallet balance (with account index of -1).
            Balance values for `unconfirmed` and `confirmed` are expressed in
            subunits.
        
        PARAMS:

            (*) Denotes required argument

            (*) account    : Address to get corresponding private key for.

            ( ) id         : Wallet ID.
        """
        
        endpoint = '/wallet/' + id + '/balance?account=' + account
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get balance for account " + account + "'}"
        return response
    ### END METHOD ################################### getBalance(self, account:str='', id:str='primary')

    def listCoins(self, id:str='primary'):
        """
        DESCRIPTION:

            List all wallet coins available.
        
        PARAMS:

            (*) Denotes required argument

            ( ) id : Wallet ID.
        """
        
        endpoint = '/wallet/' + id + '/coin'
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to list coins for wallet ID " + id + "'}"
        return response
    ### END METHOD ################################### listCoins(self, id:str='primary')

    def lockCoinOutpoints(self, tx_hash:str, index:str='0', id:str='primary'):
        """
        DESCRIPTION:

            Lock outpoints.
        
        PARAMS:

            (*) Denotes required argument

            (*) tx_hash : Hash of transaction that created the outpoint.

            ( ) index   : Index of the output in the transaction being referenced. Default = '0'

            ( ) id      : ID of wallet that contains the outpoint. Default = 'primary'
        """

        endpoint = '/wallet/' + id + '/locked/' + tx_hash + '/' + index
        try:
            response = self.put(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to lock coin outpoint for transaction " + tx_hash + " at index " + index + "'}"
        return response
    ### END METHOD ################################### lockCoinOutpoints(self, tx_hash:str, index:str='0', id:str='primary')

    def unlockCoinOutpoints(self, tx_hash:str, index:str='0', id:str='primary'):
        """
        DESCRIPTION:

            Unlock outpoints.
        
        PARAMS:

            (*) Denotes required argument

            (*) tx_hash : Hash of transaction that created the outpoint.

            ( ) index   : Index of the output in the transaction being referenced. Default = '0'

            ( ) id      : ID of wallet that contains the outpoint. Default = 'primary'
        """

        endpoint = '/wallet/' + id + '/locked/' + tx_hash + '/' + index

        response = self.delete(endpoint)
        return response
    ### END METHOD ################################### unlockCoinOutpoints(self, tx_hash:str, index:str='0', id:str='primary')

    def getLockedOutpoints(self, id:str='primary'):
        """
        DESCRIPTION:

            Get all locked outpoints.
        
        PARAMS:

            (*) Denotes required argument

            ( ) id : ID of wallet to check for outpoints.
        """
        
        endpoint = '/wallet/' + id + '/locked'
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get list of locked outpoints'}"
        return response
    ### END METHOD ################################### getLockedOutpoints(self, id:str='primary')

    def getWalletCoin(self, tx_hash:str, index:str='0', id:str='primary'):
        """
        DESCRIPTION:

            Get wallet coin.
        
        PARAMS:

            (*) Denotes required argument

            (*) tx_hash : ID of wallet that contains the outpoint.

            ( ) index   : Hash of transaction that created the outpoint.

            ( ) id      : Index of the output in the transaction being referenced.
        """
        
        endpoint = '/wallet/' + id + '/coin/' + tx_hash + '/' + index
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get coin for transaction hash " + tx_hash + " at index " + index + "'}"
        return response
    ### END METHOD ################################### getWalletCoin(self, tx_hash:str, index:str='0', id:str='primary')

    def walletRescan(self, height:int):
        """
        DESCRIPTION:

            Initiates a blockchain _rescan for the walletdb. Wallets will
            be rolled back to the specified height (transactions above
            this height will be unconfirmed).
        
        PARAMS:

            (*) Denotes required argument

            (*) height : Name of wallet.
        """
        
        endpoint = '/_rescan/'

        message = '{"height": ' + str(height) + ' }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to _rescan wallet'}"
        return response
    ### END METHOD ################################### walletRescan(self, height:int)

    def walletResend(self):
        """
        DESCRIPTION:

            Rebroadcast all pending transactions in all wallets.
        
        PARAMS:

            None.
        """
        
        endpoint = '/resend/'
        try:
            response = self.post(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Faild to rebroadcast transactions'}"
        return response
    ### END METHOD ################################### walletResend(self)

    def walletBackup(self, path:str=''):
        """
        DESCRIPTION:

            Safely backup the wallet database to specified path (creates a clone of the database).
        
        PARAMS:

            (*) Denotes required argument

            (*) path : Local directory to save backup.
        """
        
        endpoint = '/backup?path=' + path

        try:
            response = self.post(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to back up wallet'}"
        return response
    ### END METHOD ################################### walletBackup(self, path:str='')

    def walletMasterHDKeyBackup(self, id:str='primary'):
        """
        DESCRIPTION:

            Export the wallet's master hd private key. This is normally
            censored in the wallet info route. The provided API key must
            have admin access.
            
            Note: Once a passphrase has been set for a wallet, the API
            will not reveal the unencrypted master hd private key or seed
            phrase. Be sure you back it up right away! 
        
        PARAMS:

            (*) Denotes required argument

            ( ) id : Wallet ID. Default = 'primary'
        """
        
        endpoint = '/wallet/' + id + '/master'
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to back up master HD private key'}"
        return response
    ### END METHOD ################################### walletMasterHDKeyBackup(self, id:str='primary')

    def listWallets(self):
        """
        DESCRIPTION:

            List all wallet IDs. Returns an array of strings. 
        
        PARAMS:

            None.
        """
        
        endpoint = '/wallet/'
        
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Cannot fetch list of wallets'}"
        return response
    ### END METHOD ################################### listWallets(self)

    def getWalletAccountList(self, id:str='primary'):
        """
        DESCRIPTION:

            List all account names (array indices map directly to bip44
            account indices) associated with a specific wallet id.
        
        PARAMS:

            (*) Denotes required argument

            ( ) id : ID of wallet you would like to retrieve the account list for. Default = 'primary'
        """
        
        endpoint = '/wallet/' + id + '/account'
        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Cannot get account list'}"
        return response
    ### END METHOD ################################### getWalletAccountList(self, id:str='primary')

    def getAccountInfo(self, id:str='primary', account:str='default'):
        """
        DESCRIPTION:

            Get account info.
        
        PARAMS:

            (*) Denotes required argument

            ( ) id : ID of wallet you would like to query. Default = 'primary'
            ( ) account : ID of account you would to retrieve information for. Default = 'default'
        """
        
        endpoint = '/wallet/' + id + '/account/' + account

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Cannot get account info'}"
        return response
    ### END METHOD ################################### getAccountInfo(self, id:str='primary', account:str='default')

    def createAccount(self, passphrase:str, id:str, account:str, account_key:str='', type:str='pubkeyhash', m:int=1, n:int=1):
        """
        DESCRIPTION:

            Create account with specified account name.
        
        PARAMS:

            (*) Denotes required argument

            (*) id          : Wallet ID (used for storage).

            (*) passphrase  : A strong passphrase used to encrypt the wallet.

            (*) account     : Name to give the account.

            ( ) account_key : The extended public key for the account. This is ignored for
                              non watch only wallets. Watch only accounts can't accept private
                              keys for import (or sign transactions).

            ( ) type        : Type of wallet (pubkeyhash, multisig). Default is 'pubkeyhash'

            ( ) m           : 'm' value for multisig (m-of-n).

            ( ) n           : 'n' value for multisig (m-of-n)
        """
        
        endpoint = '/wallet/' + id + '/account/' + account

        message = '{"type":"' + type + '", "passphrase":"' + passphrase + '", "accountKey":"' + account_key + '", "m": ' + str(m) + ', "n": ' + str(n) + '}'
        try:
            response = self.put(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to create account '" + account + "'}"
        return response
    ### END METHOD ################################### createAccount(self, passphrase:str, id:str, account:str,
    #                                                                      account_key:str='', type:str='pubkeyhash',
    #                                                                      m:int=1, n:int=1)

    def getWalletTxDetails(self, id:str='primary', tx_hash:str=''):
        """
        DESCRIPTION:

            Get wallet transaction details.
        
        PARAMS:

            (*) Denotes required argument

            ( ) id      : ID of wallet that handled the transaction. Default = 'primary'
            (*) tx_hash : ID of account you would to retrieve information for.
        """
        
        endpoint = '/wallet/' + id + '/tx/' + tx_hash

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Cannot get transaction details for the wallet '" + id + "'}"
        return response
    ### END METHOD ################################### getWalletTxDetails(self, id:str='primary', tx_hash:str='')

    def deleteTransaction(self, id:str='primary', tx_hash:str=''):
        """
        DESCRIPTION:

            Abandon single pending transaction. Confirmed transactions
            will throw an error. `TX not eligible`
        
        PARAMS:

            (*) Denotes required argument

            ( ) id      : ID of wallet where the transaction is that you want to remove.

            (*) tx_hash : Hash of transaction you would like to remove.
        """

        endpoint = '/wallet/' + id + '/tx/' + tx_hash
        try:
            response = self.delete(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to delete transaction in '" + id + "'}"
        return response
    ### END METHOD ################################### deleteTransaction(self, id:str='primary', tx_hash:str='')

    def getWalletTxHistory(self, id:str='primary'):
        """
        DESCRIPTION:

            Get wallet TX history. Returns array of tx details.
        
        PARAMS:

            (*) Denotes required argument

            ( ) id : ID of wallet to get history of. Default = 'primary'
        """
        
        endpoint = '/wallet/' + id + '/tx/history'

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get transaction history for '" + id + "'}"
        return response
    ### END METHOD ################################### getWalletTxHistory(self, id:str='primary')

    def getPendingTransactions(self, id:str='primary'):
        """
        DESCRIPTION:

            Get pending wallet transactions. Returns array of tx details.
        
        PARAMS:

            (*) Denotes required argument

            ( ) id : ID of wallet to get pending/unconfirmed transactions. Default = 'primary'
        """
        
        endpoint = '/wallet/' + id + '/tx/unconfirmed'

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get pending transactions for '" + id + "'}"
        return response
    ### END METHOD ################################### getPendingTransactions(self, id:str='primary')

    def getRangeOfTransactions(self, start:int=0, end:int=0, id:str='primary'):
        """
        DESCRIPTION:

            Get range of wallet transactions by timestamp. Returns array of tx details.

            Note: If no `start` or `end` timestamps are give, all transactions will be returned.
        
        PARAMS:

            (*) Denotes required argument

            ( ) start   : Start time to get range from. Default = 0

            ( ) end     : End time to get range from. Default = 0

            ( ) id      : ID of wallet to get transactions from. Default = 'primary'
        """
        
        endpoint = '/wallet/' + id + '/tx/range?start=' + start + '&end=' + end

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get transaction range for '" + id + "'}"
        return response
    ### END METHOD ################################### getRangeOfTransactions(self, start:int, end:int, id:str='primary')

    def getWalletNames(self, id:str='primary'):
        """
        DESCRIPTION:

            List the states of all names known to the wallet.

            Note: If no wallet ID is given, the names of the `primary` wallet
                  will be returned.
        
        PARAMS:

            (*) Denotes required argument

            ( ) id : ID of wallet to get transactions from. Default = 'primary'
        """
        
        endpoint = '/wallet/' + id + '/name'

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get list of wallet names for '" + id + "'}"
        return response
    ### END METHOD ################################### getWalletNames(self, id:str='primary')

    def getWalletName(self, name:str='', id:str='primary'):
        """
        DESCRIPTION:

            List the status of a single name known to the wallet.
        
        PARAMS:

            (*) Denotes required argument

            (*) name : Name of wallet.

            (*) id   : ID of wallet. Default = 'primary'
        """
        
        endpoint = '/wallet/' + id + '/name/' + name

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get status of wallet named '" + name + "'}"
        return response
    ### END METHOD ################################### getWalletName(self, name:str='', id:str='primary')

    def getWalletAuctions(self, id:str='primary'):
        """
        DESCRIPTION:

            List the states of all auctions known to the wallet.

            Note: If no wallet is specified, all auctions for the
                  `primary` wallet will be returned by default.
        
        PARAMS:

            (*) Denotes required argument

            ( ) id : ID of wallet. Default = 'primary'
        """
        
        endpoint = '/wallet/' + id + '/auction'

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get auctions for '" + id + "' wallet.'}"
        return response
    ### END METHOD ################################### getWalletAuctions(self, id:str='primary')

    def getWalletAuctionByName(self, name:str='', id:str='primary'):
        """
        DESCRIPTION:

            List the states of all auctions known to the wallet.
        
        PARAMS:

            (*) Denotes required argument

            (*) name : Name of wallet.

            ( ) id   : ID of wallet. Default = 'primary'
        """
        
        endpoint = '/wallet/' + id + '/auction/' + name

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get auctions for the wallet '" + name + "'}"
        return response
    ### END METHOD ################################### getWalletAuctionByName(self, name:str='', id:str='primary')

    def getWalletBids(self, id:str='primary', own:bool=True):
        """
        DESCRIPTION:

            List all bids for all names known to the wallet.

            Note: If no wallet is specified bids for the `primary`
                  wallet will be returned.
        
        PARAMS:

            (*) Denotes required argument

            ( ) id  : ID of wallet. Default = 'primary'

            ( ) own : Whether to only show bids from this wallet. Default = True
        """
        _own = ''

        if own == True:
            _own = '1'
        else:
            _own = '0'
        
        endpoint = '/wallet/' + id + '/bid?own=' + _own

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get bids for the wallet '" + id + "'}"
        return response
    ### END METHOD ################################### getWalletBids(self, id:str='primary', own:bool=True)

    def getWalletBidsByName(self, name:str='', id:str='primary', own:bool=False):
        """
        DESCRIPTION:

            List all bids for all names known to the wallet.
        
        PARAMS:

            (*) Denotes required argument

            (*) name : Name of domain to display bids for.

            ( ) id   : ID of wallet. Default = 'primary'

            ( ) own  : Whether to only show bids from this wallet. Default = False
        """
        _own = ''

        if own == True:
            _own = '1'
        else:
            _own = '0'
        
        endpoint = '/wallet/' + id + '/bid/' + name + '?own=' + _own

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get bids for the domain '" + name + "'}"
        return response
    ### END METHOD ################################### getWalletBidsByName(self, name:str='', id:str='primary', own:bool=False)

    def getWalletReveals(self, id:str='primary', own:bool=False):
        """
        DESCRIPTION:

            List all reveals for all names known to the wallet.
        
        PARAMS:

            (*) Denotes required argument

            ( ) id  : ID of wallet. Default = 'primary'

            ( ) own : Whether to only show reveals from this wallet. Default = False
        """
        _own = ''

        if own == True:
            _own = '1'
        else:
            _own = '0'
        
        endpoint = '/wallet/' + id + '/reveal?own=' + _own

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get reveals known to the wallet '" + id + "'}"
        return response
    ### END METHOD ################################### getWalletReveals(self, id:str='primary', own:bool=False)

    def getWalletRevealsByName(self, name:str, id:str='primary', own:bool=False):
        """
        DESCRIPTION:

            List all reveals for all names known to the wallet.
        
        PARAMS:

            (*) Denotes required argument

            (*) name : Name of domain to get reveals for.

            ( ) id   : ID of wallet. Default = 'primary'

            ( ) own  : Whether to only show reveals from this wallet. Default = False
        """
        _own = ''

        if own == True:
            _own = '1'
        else:
            _own = '0'
        
        endpoint = '/wallet/' + id + '/reveal/' + name + '?own=' + _own

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get reveals for the domain '" + name + "'}"
        return response
    ### END METHOD ################################### getWalletRevealsByName(self, name:str='', id:str='primary', own:bool=False)

    def getWalletResourceByName(self, name:str, id:str='primary'):
        """
        DESCRIPTION:

            Get the data resource associated with a name.
        
        PARAMS:

            (*) Denotes required argument

            (*) name : Name of domain.

            ( ) id   : ID of wallet. Default = 'primary'
        """

        endpoint = '/wallet/' + id + '/resource'

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to get data resources associated with the domain '" + name + "'}"
        return response
    ### END METHOD ################################### getWalletResourceByName(self, name:str='', id:str='primary')

    def getNonceForBid(self, bid:float, name:str, address:str, id:str='primary'):
        """
        DESCRIPTION:

            Deterministically generate a nonce to blind a bid.

            Note: This command involves entering HNS values, be careful
                  with different formats of values for different APIs. 
        
        PARAMS:

            (*) Denotes required argument

            (*) bid     : Value of bid to blind.

            (*) name    : Name of domain.

            (*) address : Address controlling bid.

            ( ) id      : ID of wallet. Default = 'primary'
        """

        endpoint = '/wallet/' + id + '/nounce/' + name + '?address=' + address + '&bid=' + str(bid)

        try:
            response = self.get(endpoint)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to generate nonce for blind bid on '" + name + "'}"
        return response
    ### END METHOD ################################### getNonceForBid(self, bid:float, name:str, address:str, id:str='primary')

    def sendOPEN(self, id:str, passphrase:str, name:str, sign:bool=True, broadcast:bool=True):
        """
        DESCRIPTION:

            Create, sign, and send a name OPEN.
        
        PARAMS:

            (*) Denotes required argument

            (*) id         : Wallet ID.

            (*) passphrase : Passphrase to unlock the wallet.

            (*) name       : Name to OPEN.

            ( ) sign       : Whether to sign the transaction. Default = True

            ( ) broadcast  : Whether to broadcast the transaction (must sign if true). Default = True
        """

        _sign = ''
        _broadcast = ''

        if sign == True:
            _sign = '1'
        else:
            _sign = '0'

        if broadcast == True:
            _broadcast = '1'
        else:
            _broadcast = '0'
        
        endpoint = '/wallet/' + id + '/open'

        message = '{ "passphrase":"' + passphrase + '", "name":"' + name + '", "broadcast":' + str(_broadcast) + ', "sign":' + str(_sign) + ' }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to OPEN auction for '" + name + "'}"
        return response
    ### END METHOD ################################### sendOPEN(self, id:str, passphrase:str, name:str, sign:bool=True, broadcast:bool=True)

    def sendBID(self, id:str, passphrase:str, name:str, bid:int, lockup:int, sign:bool=True, broadcast:bool=True):
        """
        DESCRIPTION:

            Create, sign, and send a name BID.
        
        PARAMS:

            (*) Denotes required argument

            (*) id         : Wallet ID.

            (*) passphrase : Passphrase to unlock the wallet.

            (*) name       : Name to BID on.

            (*) bid        : Value (in dollarydoos) to bid for name.

            (*) lockup     : Value (in dollarydoos) to actually send in the transaction, blinding the actual bid value.

            ( ) sign       : Whether to sign the transaction. Default = True

            ( ) broadcast  : Whether to broadcast the transaction (must sign if true). Default = True
        """

        _sign = ''
        _broadcast = ''

        if sign == True:
            _sign = '1'
        else:
            _sign = '0'

        if broadcast == True:
            _broadcast = '1'
        else:
            _broadcast = '0'
        
        endpoint = '/wallet/' + id + '/bid'

        message = '{ "passphrase":"' + passphrase + '", "name":"' + name + '", "broadcast":' + str(_broadcast) + \
                   ', "sign":' + str(_sign) + ', "bid":' + str(bid) + ', "lockup":' + str(lockup) + ' }'
        
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to send BID for '" + name + "'}"
        return response
    ### END METHOD ################################### sendBID(self, id:str, passphrase:str, name:str, bid:int, lockup:int, sign:bool=True, broadcast:bool=True)

    def sendREVEAL(self, id:str, passphrase:str, name:str='', sign:bool=True, broadcast:bool=True):
        """
        DESCRIPTION:

            Create, sign, and send a name REVEAL. If multiple bids were placed on a name,
            all bids will be revealed by this transaction. If no value is passed in for
            `name`, all reveals for all names in the wallet will be sent.
        
        PARAMS:

            (*) Denotes required argument

            (*) id         : Wallet ID.

            (*) passphrase : Passphrase to unlock the wallet.

            ( ) name       : Name to REVEAL bids for (or `null` for all names).

            ( ) sign       : Whether to sign the transaction. Default = True

            ( ) broadcast  : Whether to broadcast the transaction (must sign if true). Default = True
        """

        _sign = ''
        _broadcast = ''

        if sign == True:
            _sign = '1'
        else:
            _sign = '0'

        if broadcast == True:
            _broadcast = '1'
        else:
            _broadcast = '0'
        
        endpoint = '/wallet/' + id + '/reveal'

        message = '{ "passphrase":"' + passphrase + '", "name":"' + name + '", "broadcast":' + str(_broadcast) + ', "sign":' + str(_sign) + ' }'
        
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to send name REVEAL for '" + name + "'}"
        return response
    ### END METHOD ################################### sendREVEAL(self, id:str, passphrase:str, name:str='', sign:bool=True, broadcast:bool=True)

    def sendREDEEM(self, id:str, passphrase:str, name:str='', sign:bool=True, broadcast:bool=True):
        """
        DESCRIPTION:

            Create, sign, and send a REDEEM. This transaction sweeps the value
            from losing bids back into the wallet. If multiple bids (and reveals)
            were placed on a name, all losing bids will be redeemed by this 
            ransaction. If no value is passed in for `name`, all qualifying bids
            are redeemed.
        
        PARAMS:

            (*) Denotes required argument

            (*) id         : Wallet ID.

            (*) passphrase : Passphrase to unlock the wallet.

            ( ) name       : Name to REDEEM bids for (or null for all names).

            ( ) sign       : Whether to sign the transaction. Default = True

            ( ) broadcast  : Whether to broadcast the transaction (must sign if true). Default = True
        """

        _sign = ''
        _broadcast = ''

        if sign == True:
            _sign = '1'
        else:
            _sign = '0'

        if broadcast == True:
            _broadcast = '1'
        else:
            _broadcast = '0'
        
        endpoint = '/wallet/' + id + '/redeem'

        message = '{ "passphrase":"' + passphrase + '", "name":"' + name + '", "broadcast":' + str(_broadcast) + ', "sign":' + str(_sign) + ' }'
        
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to REDEEM bids for '" + name + "'}"
        return response
    ### END METHOD ################################### sendREDEEM(self, id:str, passphrase:str, name:str='', sign:bool=True, broadcast:bool=True)

    def sendUPDATE(self, id:str, passphrase:str, name:str, data:str, sign:bool=True, broadcast:bool=True):
        """
        DESCRIPTION:

            Create, sign, and send an UPDATE. This transaction updates 
            the resource data associated with a given name.

            Note: Due to behavior of some shells like bash, if your TXT
                  value contains spaces you may need to add additional
                  quotes like this: "'"$value"'"
        
        PARAMS:

            (*) Denotes required argument

            (*) id         : Wallet ID.

            (*) passphrase : Passphrase to unlock the wallet.

            ( ) name       : Name to UPDATE.

            ( ) data       : JSON object containing an array of DNS records (resource object).
                              See https://hsd-dev.org/api-docs/#resource-object for more information.

            ( ) sign       : Whether to sign the transaction. Default = True

            ( ) broadcast  : Whether to broadcast the transaction (must sign if true). Default = True
        """

        _sign = ''
        _broadcast = ''

        if sign == True:
            _sign = '1'
        else:
            _sign = '0'

        if broadcast == True:
            _broadcast = '1'
        else:
            _broadcast = '0'
        
        endpoint = '/wallet/' + id + '/update'

        message = '{ "passphrase":"' + passphrase + '", "name":"' + name + '", "broadcast":' + str(_broadcast) + ', "sign":' + str(_sign) + ', "data":' + data + ' }'
        
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to UPDATE resource data for '" + name + "'}"
        return response
    ### END METHOD ################################### sendUPDATE(self, id:str, passphrase:str, name:str, data:str, sign:bool=True, broadcast:bool=True)

    def sendRENEW(self, id:str, passphrase:str, name:str, sign:bool=True, broadcast:bool=True):
        """
        DESCRIPTION:

            Create, sign, and send a RENEW.
        
        PARAMS:

            (*) Denotes required argument

            (*) id         : Wallet ID.

            (*) passphrase : Passphrase to unlock the wallet.

            ( ) name       : Name to RENEW.

            ( ) sign       : Whether to sign the transaction. Default = True

            ( ) broadcast  : Whether to broadcast the transaction (must sign if true). Default = True
        """

        _sign = ''
        _broadcast = ''

        if sign == True:
            _sign = '1'
        else:
            _sign = '0'

        if broadcast == True:
            _broadcast = '1'
        else:
            _broadcast = '0'
        
        endpoint = '/wallet/' + id + '/renewal'

        message = '{ "passphrase":"' + passphrase + '", "name":"' + name + '", "broadcast":' + str(_broadcast) + ', "sign":' + str(_sign) + ' }'
        
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to RENEW domain '" + name + "'}"
        return response
    ### END METHOD ################################### sendRENEW(self, id:str, passphrase:str, name:str, sign:bool=True, broadcast:bool=True)

    def sendTRANSFER(self, id:str, passphrase:str, name:str, address:str, sign:bool=True, broadcast:bool=True):
        """
        DESCRIPTION:

            Create, sign, and send a TRANSFER.
        
        PARAMS:

            (*) Denotes required argument

            (*) id         : Wallet ID.

            (*) passphrase : Passphrase to unlock the wallet.

            ( ) name       : Name to TRANSFER.

            ( ) address    : Address to transfer name ownership to.

            ( ) sign       : Whether to sign the transaction. Default = True

            ( ) broadcast  : Whether to broadcast the transaction (must sign if true). Default = True
        """

        _sign = ''
        _broadcast = ''

        if sign == True:
            _sign = '1'
        else:
            _sign = '0'

        if broadcast == True:
            _broadcast = '1'
        else:
            _broadcast = '0'
        
        endpoint = '/wallet/' + id + '/transfer'

        message = '{ "passphrase":"' + passphrase + '", "name":"' + name + '", "broadcast":' + str(_broadcast) + ', "sign":' + str(_sign) + ', "address": "' + address + '" }'
        
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to TRANSFER domain '" + name + "'}"
        return response
    ### END METHOD ################################### sendTRANSFER(self, id:str, passphrase:str, name:str, address:str, sign:bool=True, broadcast:bool=True)

    def cancelTRANSFER(self, id:str, passphrase:str, name:str, sign:bool=True, broadcast:bool=True):
        """
        DESCRIPTION:

            Create, sign, and send a transaction that cancels a TRANSFER.

            This transaction is not a unique covenant type, but spends from
            a TRANSFER to an UPDATE covenant (with an empty resource object)
            in order to cancel a transfer already in progress.
        
        PARAMS:

            (*) Denotes required argument

            (*) id         : Wallet ID.

            (*) passphrase : Passphrase to unlock the wallet.

            (*) name       : Name in transferred state to cancel transfer for.

            ( ) sign       : Whether to sign the transaction. Default = True

            ( ) broadcast  : Whether to broadcast the transaction (must sign if true). Default = True
        """

        _sign = ''
        _broadcast = ''

        if sign == True:
            _sign = '1'
        else:
            _sign = '0'

        if broadcast == True:
            _broadcast = '1'
        else:
            _broadcast = '0'
        
        endpoint = '/wallet/' + id + '/cancel'

        message = '{ "passphrase":"' + passphrase + '", "name":"' + name + '", "broadcast":' + str(_broadcast) + ', "sign":' + str(_sign) + '" }'
        
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to cancel transfer of '" + name + "'}"
        return response
    ### END METHOD ################################### cancelTRANSFER(self, id:str, passphrase:str, name:str, sign:bool=True, broadcast:bool=True)

    def sendFINALIZE(self, id:str, passphrase:str, name:str, sign:bool=True, broadcast:bool=True):
        """
        DESCRIPTION:

            Create, sign, and send a FINALIZE.
        
        PARAMS:

            (*) Denotes required argument

            (*) id         : Wallet ID.

            (*) passphrase : Passphrase to unlock the wallet.

            (*) name       : Name in transferred state to finalize transfer for.

            ( ) sign       : Whether to sign the transaction. Default = True

            ( ) broadcast  : Whether to broadcast the transaction (must sign if true). Default = True
        """

        _sign = ''
        _broadcast = ''

        if sign == True:
            _sign = '1'
        else:
            _sign = '0'

        if broadcast == True:
            _broadcast = '1'
        else:
            _broadcast = '0'
        
        endpoint = '/wallet/' + id + '/finalize'

        message = '{ "passphrase":"' + passphrase + '", "name":"' + name + '", "broadcast":' + str(_broadcast) + ', "sign":' + str(_sign) + '" }'
        
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to FINALIZE transfer of '" + name + "'}"
        return response
    ### END METHOD ################################### sendFINALIZE(self, id:str, passphrase:str, name:str, sign:bool=True, broadcast:bool=True)

    def sendREVOKE(self, id:str, passphrase:str, name:str, sign:bool=True, broadcast:bool=True):
        """
        DESCRIPTION:

            Create, sign, and send a REVOKE.

            This method is a fail-safe for name owners whose keys
            are compromised and lose control of their name. Before
            the transfer is finalized, a REVOKE can be sent that not
            only cancels the transfer, but burns the name preventing
            any further updates or transfers. The name can be
            reopened with a new auction after a set time.
        
        PARAMS:

            (*) Denotes required argument

            (*) id         : Wallet ID.

            (*) passphrase : Passphrase to unlock the wallet.

            (*) name       : Name in transferred state to REVOKE transfer for.

            ( ) sign       : Whether to sign the transaction. Default = True

            ( ) broadcast  : Whether to broadcast the transaction (must sign if true). Default = True
        """

        _sign = ''
        _broadcast = ''

        if sign == True:
            _sign = '1'
        else:
            _sign = '0'

        if broadcast == True:
            _broadcast = '1'
        else:
            _broadcast = '0'
        
        endpoint = '/wallet/' + id + '/revoke'

        message = '{ "passphrase":"' + passphrase + '", "name":"' + name + '", "broadcast":' + str(_broadcast) + ', "sign":' + str(_sign) + '" }'
        
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'Failed to REVOKE transfer of '" + name + "'}"
        return response
    ### END METHOD ################################### sendREVOKE(self, id:str, passphrase:str, name:str, sign:bool=True, broadcast:bool=True)

    def rpc_getNames(self):
        """
        DESCRIPTION:

            Returns the domain names associated with your wallet. 
        
        PARAMS:

            None.
        """
        
        endpoint = '/'
        message = '{ "method": "getnames", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get domain names in wallet'}"
        return response
    ### END METHOD ################################### rpc_getNames(self)

    def rpc_getAuctionInfo(self, name:str):
        """
        DESCRIPTION:

            Returns information on auction. 
        
        PARAMS:
            (*) Denotes required argument
        
            (*) name : Name to get auction information for.
        """
        
        endpoint = '/'
        message = '{ "method": "getauctioninfo", "params": [ "' + name + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to find auction information for `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_getAuctionInfo(self, name:str)

    def rpc_getBIDS(self):
        """
        DESCRIPTION:

            Returns list of `BID`s placed by your wallet. 
        
        PARAMS:
        
            None.
        """
        
        endpoint = '/'
        message = '{ "method": "getbids", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to find BIDs places with your wallet'}"
        return response
    ### END METHOD ################################### rpc_getBIDS(self)

    def rpc_getREVEALS(self):
        """
        DESCRIPTION:

            Returns all the `REVEAL` transactions sent by the wallet.
        
        PARAMS:
        
            None.
        """
        
        endpoint = '/'
        message = '{ "method": "getreveals", "params": [] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to find any REVEAL transactions sent by your wallet'}"
        return response
    ### END METHOD ################################### rpc_getREVEALS(self)

    def rpc_sendOPEN(self, name:str):
        """
        DESCRIPTION:

            Once a name is available, a sendopen transaction starts the opening phase.
        
        PARAMS:

            (*) Denotes required argument

            (*) name : Domain name to send `OPEN` transaction for.
        """
        
        endpoint = '/'
        message = '{ "method": "sendopen", "params": [ "' + name + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to start OPEN phase of auction for the domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_sendOPEN(self, name:str)

    def rpc_sendBID(self, name:str, bid_amount:float, lockup_blind:float, account:str='default'):
        """
        DESCRIPTION:

            The `OPEN` period is followed by the `BID` period. Use `rpc_sendBID` to place a bid.

            Note: This command involves entering HNS values, be careful with different formats
                  of values for different APIs. See https://hsd-dev.org/api-docs/?shell--curl#values
                  to learn more.

        
        PARAMS:

            (*) Denotes required argument

            (*) name        : Domain name to to bid on.

            (*) bid_amount   : Amount to bid (in HNS).

            (*) lockup_blind : Amount to lock up to blind your bid (must be greater than bid amount).

            ( ) account     : Wallet account to use. Default = 'default'
        """
        
        endpoint = '/'
        message = '{ "method": "sendbid", "params": [ "' + name + '", ' + str(bid_amount) + ', ' + str(lockup_blind) + ', "' + account + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to to place BID for the domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_sendBID(self, name:str, bid_amount:float, lockup_blind:float, account:str='default')

    def rpc_sendREVEAL(self, name:str=''):
        """
        DESCRIPTION:

            The `BID` period is followed by the `REVEAL` period, during which bidders
            must reveal their bids.

            Note: If not domain name is specified then a `REVEAL` will be sent to all names.
        
        PARAMS:

            (*) Denotes required argument

            ( ) name : Domain name to `REVEAL` bid for (`null` for all names).
        """
        
        endpoint = '/'
        message = '{ "method": "sendreveal", "params": [ "' + name + '" ] }'

        if name == '':
            name = '[ALL]'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to start REVEAL phase of auction for the domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_sendREVEAL(self, name:str='')

    def rpc_sendREDEEM(self, name:str=''):
        """
        DESCRIPTION:

            After the `REVEAL` period, the auction is `CLOSED`. The value locked
            up by losing bids can be spent using a `REDEEM` covenant like any
            other coin. The winning bid can not be redeemed.
        
        PARAMS:

            (*) Denotes required argument

            ( ) name : Domain name to `REDEEM` bid for (`null` for all names).
        """
        
        endpoint = '/'
        message = '{ "method": "sendredeem", "params": [ "' + name + '" ] }'

        if name == '':
            name = '[ALL]'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to start REDEEM the domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_sendREDEEM(self, name:str='')

    def rpc_sendUPDATE(self, name:str, data:json):
        """
        DESCRIPTION:

            After the `REVEAL` period, the auction is `CLOSED`. The value
            locked up by the winning bid is locked forever, although
            the name owner and the name state can still change. The
            winning bidder can update the data resource associated with
            their name by sending an `UPDATE`.
        
        PARAMS:

            (*) Denotes required argument

            (*) name       : Domain name to `UPDATE`.

            (*) data       : JSON-encoded resource object.
                              See https://hsd-dev.org/api-docs/#resource-object for more information.
        """

        data = json.dumps(data)
        endpoint = '/'
        message = '{ "method": "sendupdate", "params": [ "' + name + '", ' + data + ' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to UPDATE the domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_sendUPDATE(self, name:str, data:str)

    def rpc_sendRENEWAL(self, name:str):
        """
        DESCRIPTION:

            On mainnet, name ownership expires after two years. If the name
            owner does not `RENEW` the name, it can be re-opened by any user.
            `RENEW` covenants commit to a a recent block hash to prevent
            pre-signing and prove physical ownership of controlling keys.
            There is no cost besides the miner fee.
        
        PARAMS:

            (*) Denotes required argument

            (*) name : Domain name to `RENEW` ownership of.
        """
        
        endpoint = '/'
        message = '{ "method": "sendrenewal", "params": [ "' + name + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to RENEW the domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_sendRENEWAL(self, name:str)

    def rpc_sendTRANSFER(self, name:str, address:str):
        """
        DESCRIPTION:

            `TRANSFER` a name to a new address. Note that the output value
            of the UTXO still does not change. On mainnet, the `TRANSFER`
            period lasts two days, after which the original owner can
            `FINALIZE` the transfer. Any time before it is final, the
            original owner can still `CANCEL` or `REVOKE` the transfer.
        
        PARAMS:

            (*) Denotes required argument

            (*) name    : Domain name to `TRANSFER`.

            (*) address : Address to `TRANSFER` name ownership to.
        """
        
        endpoint = '/'
        message = '{ "method": "sendtransfer", "params": [ "' + name + '", "' + address + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to TRANSFER the domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_sendTRANSFER(self, name:str, address:str)

    def rpc_sendFINALIZE(self, name:str):
        """
        DESCRIPTION:

            About 48 hours after a TRANSFER, the original owner can send a
            `FINALIZE` transaction, completing the transfer to a new address.
            The output address of the `FINALIZE` is the new owner's address.
        
        PARAMS:

            (*) Denotes required argument

            (*) name : Domain name to `FINALIZE`.
        """
        
        endpoint = '/'
        message = '{ "method": "sendfinalize", "params": [ "' + name + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to FINALIZE the domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_sendFINALIZE(self, name:str)

    def rpc_sendCANCEL(self, name:str):
        """
        DESCRIPTION:

            After sending a `TRANSFER` but before sending a `FINALIZE`,
            the original owner can `CANCEL` the transfer. The owner will
            retain control of the name. This is the recommended means
            of canceling a transfer. Not to be confused with a `REVOKE`,
            which is only to be used in the case of a stolen key. There
            is no `CANCEL` covenant -- this transaction actually sends
            an `UPDATE`.
        
        PARAMS:

            (*) Denotes required argument

            (*) name : Domain name to `CANCEL` the in-progress transfer of.
        """
        
        endpoint = '/'
        message = '{ "method": "sendcancel", "params": [ "' + name + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to CANCEL the transfer of `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_sendCANCEL(self, name:str)

    def rpc_sendREVOKE(self, name:str):
        """
        DESCRIPTION:

            After sending a `TRANSFER` but before sending a `FINALIZE`,
            the original owner can `REVOKE` the name transfer. This
            renders the name's output forever unspendable, and puts the
            name back up for bidding. This is intended as an action of
            last resort in the case that the owner's key has been
            compromised, leading to a grief battle between an attacker
            and the owner.
        
        PARAMS:

            (*) Denotes required argument

            (*) name : Domain name to `REVOKE` the in-progress transfer of.
        """
        
        endpoint = '/'
        message = '{ "method": "sendrevoke", "params": [ "' + name + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to REVOKE the in-progress transfer of `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_sendREVOKE(self, name:str)

    def rpc_importNONCE(self, name:str, address:str, _bidValue:float):
        """
        DESCRIPTION:

            Deterministically regenerate the nonce for a bid.

            Note: This command involves entering HNS values, be careful with different formats
                  of values for different APIs. See https://hsd-dev.org/api-docs/?shell--curl#values
                  to learn more.
        
        PARAMS:

            (*) Denotes required argument

            (*) name     : Domain name bid on.

            (*) address  : Address submitting the bid.

            (*) _bidValue : Value of the bid (in HNS).
        """
        
        endpoint = '/'
        message = '{ "method": "importnonce", "params": [ "' + name + '", "' + address + '", ' + str(_bidValue) + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to regenerate NONCE for `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_importNONCE(self, name:str, address:str, _bidValue:float)

    def rpc_createOPEN(self, name:str, force:bool, account:str):
        """
        DESCRIPTION:

            Creates `OPEN` transaction without signing or broadcasting it.
        
        PARAMS:

            (*) Denotes required argument

            (*) name    : Domain name to `OPEN` bidding on.

            (*) force   : Currently ignored but required if additional parameters are passed.

            (*) account : Account to use.
        """
        
        _force = ''

        if force == True:
            _force = '1'
        else:
            _force = '0'

        endpoint = '/'
        message = '{ "method": "createopen", "params": [ "' + name + '", ' + str(_force) + ', "' + account + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to unsigned OPEN transaction for `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_createOPEN(self, name:str, force:bool, account:str)

    def rpc_createBID(self, name:str, bid_amount:float, lockup_blind:float, account:str):
        """
        DESCRIPTION:

            Create `BID` transaction without signing or broadcasting it.

            Note: This command involves entering HNS values, be careful with different formats
                  of values for different APIs. See https://hsd-dev.org/api-docs/?shell--curl#values
                  to learn more.
        
        PARAMS:

            (*) Denotes required argument

            (*) name        : Domain name bid on.

            (*) bid_amount   : Amount to bid (in HNS).

            (*) lockup_blind : Amount to lock up to blind your bid, must be greater than `bid_amount`).

            (*) address     : Address submitting the bid.
        """
        
        endpoint = '/'
        message = '{ "method": "createbid", "params": [ "' + name + '", ' + str(bid_amount) + ', ' + str(lockup_blind) + ', "' + account + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to create BID for `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_createBID(self, name:str, bid_amount:float, lockup_blind:float, account:str)

    def rpc_createREVEAL(self, name:str='', account:str=''):
        """
        DESCRIPTION:

            Create `REVEAL` transaction without signing or broadcasting it.

            Note: If no name is specified a `REVEAL` transaction will be
                  created for all names.
        
        PARAMS:

            (*) Denotes required argument

            ( ) name    : Domain name to `REVEAL` bid for (`null` for all names).

            ( ) account : Account to use.
        """
        
        endpoint = '/'
        message = '{ "method": "createreveal", "params": [ "' + name + '", "' + account + '" ] }'

        if name == '':
            name = '[ALL]'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to create a REVEAL transaction for domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_createREVEAL(self, name:str='', account:str='')

    def rpc_createREDEEM(self, name:str='', account:str=''):
        """
        DESCRIPTION:

            Create `REDEEM` transaction without signing or broadcasting it.

            Note: If no name is specified all names will have their loosing
                  bids redeemed.
        
        PARAMS:

            (*) Denotes required argument

            ( ) name    : Domain name to `REDEEM` a losing bid for (null for all names).

            ( ) account : Account to use.
        """
        
        endpoint = '/'
        message = '{ "method": "createredeem", "params": [ "' + name + '", "' + account + '" ] }'

        if name == '':
            name = '[ALL]'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to create a REDEEM transaction for domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_createREDEEM(self, name:str='', account:str='')

    def rpc_createUPDATE(self, name:str, data:json, account:str=''):
        """
        DESCRIPTION:

            Create `UPDATE` transaction without signing or broadcasting it.
        
        PARAMS:

            (*) Denotes required argument

            (*) name    : Domain name to `UPDATE` the data for.

            (*) data    : JSON-encoded resource object.
                           See https://hsd-dev.org/api-docs/#resource-object for more information.

            ( ) account : Account to use.
        """
        
        data = json.dumps(data)
        endpoint = '/'
        message = '{ "method": "createupdate", "params": [ "' + name + '", ' + data + ', "' + account + '" ] }'

        if name == '':
            name = '[ALL]'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to create UPDATE for `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_createUPDATE(self, name:str, data:json, account:str='')

    def rpc_createRENEWAL(self, name:str, account:str=''):
        """
        DESCRIPTION:

            Create `RENEW` transaction without signing or broadcasting it.
        
        PARAMS:

            (*) Denotes required argument

            (*) name    : Domain name to `RENEW` ownership of.

            ( ) account : Account to use.
        """
        
        endpoint = '/'
        message = '{ "method": "createrenewal", "params": [ "' + name + '", "' + account + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to create RENEW transaction for domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_createRENEWAL(self, name:str, account:str='')

    def rpc_createTRANSFER(self, name:str, address:str, account:str=''):
        """
        DESCRIPTION:

            Create `TRANSFER` transaction without signing or broadcasting it.
        
        PARAMS:

            (*) Denotes required argument

            (*) name    : Domain name to `TRANSFER` ownership of.

            (*) address : Address to transfer name ownership to.

            ( ) account : Account to use.
        """
        
        endpoint = '/'
        message = '{ "method": "createtransfer", "params": [ "' + name + '", "' + address + '", "' + account + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to create TRANSFER transaction for domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_createTRANSFER(self, name:str, address:str, account:str='')

    def rpc_createFINALIZE(self, name:str, account:str=''):
        """
        DESCRIPTION:

            Create `FINALIZE` transaction without signing or broadcasting it.
        
        PARAMS:

            (*) Denotes required argument

            (*) name    : Domain name to `FINALIZE`.

            ( ) account : Account to use.
        """
        
        endpoint = '/'
        message = '{ "method": "createfinalize", "params": [ "' + name + '", "' + account + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to create a FINALIZE transaction for domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_createFINALIZE(self, name:str, account:str='')

    def rpc_createCANCEL(self, name:str, account:str=''):
        """
        DESCRIPTION:

            Create `CANCEL` transaction without signing or broadcasting it.
        
        PARAMS:

            (*) Denotes required argument

            (*) name    : Domain name to `CANCEL` the in-progress transfer of.

            ( ) account : Account to use.
        """
        
        endpoint = '/'
        message = '{ "method": "createcancel", "params": [ "' + name + '", "' + account + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to create a CANCEL transaction for domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_createCANCEL(self, name:str, account:str='')

    def rpc_createREVOKE(self, name:str, account:str=''):
        """
        DESCRIPTION:

            Create `REVOKE` transaction without signing or broadcasting it.
        
        PARAMS:

            (*) Denotes required argument

            (*) name    : Domain name to `REVOKE` the in-progress transfer of.

            ( ) account : Account to use.
        """
        
        endpoint = '/'
        message = '{ "method": "createrevoke", "params": [ "' + name + '", "' + account + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to create a REVOKE transaction for domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_createREVOKE(self, name:str, account:str='')

    def rpc_importName(self, name:str, rescan_height:int=None):
        """
        DESCRIPTION:

            Add a name to the wallet "watchlist" without sending a transaction. Optionally
            _rescan the blockchain to recover `OPEN` and `BID`s for the name. This action will
            fail if the name already exists in the wallet.

            The purpose of this action is to "subscribe" to `BID`s for a name auction before
            participating in that auction. If a user is interested in `BID`s that have already
            been placed on a name they are interested in bidding on themselves, they may
            execute this RPC call and include a `height` parameter, which should be any block
            before the OPEN for the name was confirmed. The `OPEN` transaction must be included
            in the _rescan or the wallet will not track `BID`s on the name.

            Once the auction is rescanned, `rpc_getBIDS` can be used to return all current BIDs
            on a name, even if the wallet has not placed any BIDs itself.
        
        PARAMS:

            (*) Denotes required argument

            (*) name         : Domain name to import.

            ( ) rescan_height : If present, perform a wallet _rescan from specified height.
        """
        
        endpoint = '/'
        
        if rescan_height == None:
            message = '{ "method": "importname", "params": [ "' + name + '" ] }'
        else:
            message = '{ "method": "importname", "params": [ "' + name + '", ' + str(rescan_height) + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to import domain `" + name + "`'}"
        return response
    ### END METHOD ################################### rpc_importName(self, name:str, rescan_height:int=None)

    def rpc_selectWallet(self, wallet_id:str):
        """
        DESCRIPTION:

            Switch target wallet for all future RPC calls.
        
        PARAMS:

            (*) Denotes required argument

            (*) wallet_id : ID of selected wallet.
        """
        
        endpoint = '/'
        message = '{ "method": "selectwallet", "params": [ "' + wallet_id + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to select wallet named `" + wallet_id + "`'}"
        return response
    ### END METHOD ################################### rpc_selectWallet(self, wallet_id:str)

    def rpc_getWalletInfo(self):
        """
        DESCRIPTION:

            Get basic wallet details.
        
        PARAMS:

            None.
        """
        
        endpoint = '/'
        message = '{ "method": "getwalletinfo" }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get wallet info'}"
        return response
    ### END METHOD ################################### rpc_getWalletInfo(self)

    def rpc_fundRawTransaction(self, tx_hex:str, fee_rate:float=None, change_address:str=None):
        """
        DESCRIPTION:

            Add inputs to a transaction until it has enough in value to meet its out value.
        
        PARAMS:

            (*) Denotes required argument

            (*) tx_hex         : Raw transaction (hex).

            ( ) fee_rate       : Sets fee rate for transaction in HNS/kb.

            ( ) change_address : Handshake address for change output of transaction.
        """
        
        endpoint = '/'

        options = {}
        
        if fee_rate != None:
            options['feeRate'] = fee_rate

        if change_address != None:
            options['changeAddress'] = change_address


        if fee_rate == None and change_address == None:
            message = '{ "method": "fundrawtransaction", "params": [ "' + tx_hex + '" ] }'
        else:
            #options = '{"changeAddress": "' +  change_address + '", "feeRate": ' + str(fee_rate) + '}'
            message = '{ "method": "fundrawtransaction", "params": [ "' + tx_hex + '", ' + json.dumps(options) + '] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to fund raw transaction'}"
        return response
    ### END METHOD ################################### rpc_fundRawTransaction(self, tx_hex:str, fee_rate:float=None, change_address:str=None)

    def rpc_resendWalletTransactions(self):
        """
        DESCRIPTION:

            Re-broadcasts all unconfirmed transactions to the network.
        
        PARAMS:

            None.
        """
        
        endpoint = '/'
        message = '{ "method": "resendwallettransactions" }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed resend wallet transactions'}"
        return response
    ### END METHOD ################################### rpc_resendWalletTransactions(self)

    def rpc_abandonTransaction(self, tx_id:str):
        """
        DESCRIPTION:

            Remove transaction from the database. This allows "stuck" coins to be respent.
        
        PARAMS:

            (*) Denotes required argument

            (*) tx_id : Transaction ID to remove.
        """
        
        endpoint = '/'
        message = '{ "method": "abandontransaction", "params": [ "' + tx_id + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to abandon transaction'}"
        return response
    ### END METHOD ################################### rpc_abandonTransaction(self, tx_id:str)

    def rpc_backupWallet(self, path:str):
        """
        DESCRIPTION:

            Back up wallet database and files to directory created at specified path.
        
        PARAMS:

            (*) Denotes required argument

            (*) path : Absolute path (including directories and filename) to write backup file.
        """
        
        endpoint = '/'
        message = '{ "method": "backupwallet", "params": [ "' + path + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed backup wallet'}"
        return response
    ### END METHOD ################################### rpc_backupWallet(self, path:str)

    def rpc_dumpPrivKey(self, address:str):
        """
        DESCRIPTION:

            Get the private key (WIF format) corresponding to specified
            address. Also see `hsw.rpc_importPrivKey`.
        
        PARAMS:

            (*) Denotes required argument

            (*) address : Reveal the private key for this Handshake address.
        """
        
        endpoint = '/'
        message = '{ "method": "dumpprivkey", "params": [ "' + address + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to dump private keys'}"
        return response
    ### END METHOD ################################### rpc_dumpPrivKey(self, address:str)

    def rpc_dumpWallet(self, path:str):
        """
        DESCRIPTION:

            Creates a new human-readable file at specified path with
            all wallet private keys in Wallet Import Format (base58).
        
        PARAMS:

            (*) Denotes required argument

            (*) path : Absolute path (including directories and filename) to write backup file.
        """
        
        endpoint = '/'
        message = '{ "method": "dumpwallet", "params": [ "' + path + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to dump wallet to `" + path + "`'}"
        return response
    ### END METHOD ################################### rpc_dumpWallet(self, path:str)

    def rpc_encryptWallet(self, passphrase:str):
        """
        DESCRIPTION:

            Encrypts wallet with provided passphrase. This action
            can only be done once on an unencrypted wallet. See
            `hsw.rpc_walletPasswordChange()` or `hsw.changePassword()`
            if wallet has already been encrypted.
        
        PARAMS:

            (*) Denotes required argument

            (*) passphrase : Absolute path (including directories and filename) to write backup file.
        """
        
        endpoint = '/'
        message = '{ "method": "encryptwallet", "params": [ "' + passphrase + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to encrypt wallet'}"
        return response
    ### END METHOD ################################### rpc_encryptWallet(self, passphrase:str)

    def rpc_getAccountAddress(self, account:str='default'):
        """
        DESCRIPTION:

            Get the current receiving address for specified account.

            Note: If no account is specified, the receiving address
                  for the account `default` will be returned.
        
        PARAMS:

            (*) Denotes required argument

            ( ) account : Account to retrieve address from.
        """
        
        endpoint = '/'
        message = '{ "method": "getaccountaddress", "params": [ "' + account + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get account address for `" + account + "`'}"
        return response
    ### END METHOD ################################### rpc_getAccountAddress(self, account:str)

    def rpc_getAccount(self, address:str):
        """
        DESCRIPTION:

            Get the account associated with a specified address.
        
        PARAMS:

            (*) Denotes required argument

            (*) address : Address to search for.
        """
        
        endpoint = '/'
        message = '{ "method": "getaccount", "params": [ "' + address + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get account for the address `" + address + "`'}"
        return response
    ### END METHOD ################################### rpc_getAccount(self, address:str)

    def rpc_getAddressesByAccount(self, account:str='default'):
        """
        DESCRIPTION:

            Get all addresses for a specified account.

            Note: If no account is specified, then the addresses
                  for the account `default` will be returned.
        
        PARAMS:

            (*) Denotes required argument

            ( ) account : Account to retrieve addresses from.
        """
        
        endpoint = '/'
        message = '{ "method": "getaddressesbyaccount", "params": [ "' + account + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get all addresses for the account `" + account + "`'}"
        return response
    ### END METHOD ################################### rpc_getAddressesByAccount(self, account:str='default')

    def rpc_getBalance(self, account:str=None):
        """
        DESCRIPTION:

            Get total balance for entire wallet or a single, specified account.

            Note: If no account is specified, then the balance of
                  the entire wallet will be returned
        
        PARAMS:

            (*) Denotes required argument

            ( ) account : Account to return balance of.
        """
        
        endpoint = '/'

        if account == None:
            account = '[ALL]'
            message = '{ "method": "getbalance" }'
        else:
            message = '{ "method": "getbalance", "params": [ "' + account + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get balance for `" + account + "`'}"
        return response
    ### END METHOD ################################### rpc_getBalance(self, account:str=None)

    def rpc_getNewAddress(self, account:str=''):
        """
        DESCRIPTION:

            Get the next receiving address from specified account, or default account.
        
        PARAMS:

            (*) Denotes required argument

            ( ) account : Account name. Default = 'defualt'
        """
        
        endpoint = '/'

        message = '{ "method": "getnewaddress", "params": [ "' + account +'" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get new receiving address'}"
        return response
    ### END METHOD ################################### rpc_getNewAddress(self, account:str='')

    def rpc_getRawChangeAddress(self):
        """
        DESCRIPTION:

            Get the next change address from specified account.
        
        PARAMS:

            None.
        """
        
        endpoint = '/'
        message = '{ "method": "getrawchangeaddress" }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed get next change address'}"
        return response
    ### END METHOD ################################### rpc_getRawChangeAddress(self)

    def rpc_getReceivedByAccount(self, account:str, min_confirm:int=None):
        """
        DESCRIPTION:

            Get total amount received by specified account. Optionally
            only count transactions with `min_confirm` number of confirmations.
        
        PARAMS:

            (*) Denotes required argument

            (*) account    : Account name.

            ( ) min_confirm : Only include transactions with this many confirmations.
        """
        
        endpoint = '/'

        if min_confirm == None:
            message = '{ "method": "getreceivedbyaccount", "params": [ "' + account + '" ] }'
        else:
            message = '{ "method": "getreceivedbyaccount", "params": [ "' + account + '", ' + str(min_confirm) + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get amount received for the `" + account + "` account'}"
        return response
    ### END METHOD ################################### rpc_getReceivedByAccount(self, account:str, min_confirm:int=None)

    def rpc_getReceivedByAddress(self, address:str, min_confirm:int=None):
        """
        DESCRIPTION:

            Get total amount received by specified address. Optionally
            only count transactions with `min_confirm` number of confirmations.
        
        PARAMS:

            (*) Denotes required argument

            (*) address    : Address to request balance of.

            ( ) min_confirm : Only include transactions with this many confirmations.
        """
        
        endpoint = '/'

        if min_confirm == None:
            message = '{ "method": "getreceivedbyaddress", "params": [ "' + address + '" ] }'
        else:
            message = '{ "method": "getreceivedbyaddress", "params": [ "' + address + '", ' + str(min_confirm) + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get amount received for address `" + address + "` account'}"
        return response
    ### END METHOD ################################### rpc_getReceivedByAddress(self, account:str, min_confirm:int=None)

    def rpc_getTransaction(self, tx_id:str, watch_only:bool=None):
        """
        DESCRIPTION:

            Get details about a transaction in the wallet.
        
        PARAMS:

            (*) Denotes required argument

            (*) tx_id      : ID of transaction to fetch.

            ( ) watch_only : (bool) Whether to include watch-only addresses in balance details.
        """
        
        endpoint = '/'

        if watch_only == None:
            message = '{ "method": "gettransaction", "params": [ "' + tx_id + '" ] }'
        else:
            _watch_only = ''

            if watch_only == True:
                _watch_only = '1'
            else:
                _watch_only = '0'

            message = '{ "method": "gettransaction", "params": [ "' + tx_id + '", ' + _watch_only + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get transaction details'}"
        return response
    ### END METHOD ################################### rpc_getTransaction(self, tx_id:str, watch_only:bool=None)

    def rpc_getUnconfirmedBalance(self):
        """
        DESCRIPTION:

            Get the unconfirmed balance from the wallet.
        
        PARAMS:

            None.
        """
        
        endpoint = '/'
        message = '{ "method": "getunconfirmedbalance" }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed get balance of unconfirmed'}"
        return response
    ### END METHOD ################################### rpc_getUnconfirmedBalance(self)

    def rpc_importPrivKey(self, private_key:str, label:str=None, rescan:bool=None):
        """
        DESCRIPTION:

            Import a private key into wallet. Also see `hsw.rpc_dumpPrivKey`.
        
        PARAMS:

            (*) Denotes required argument

            (*) private_key : Private key to import (WIF format).

            ( ) label   : Ignored but required if additional parameters are passed.

            ( ) rescan  : (bool) Whether to _rescan wallet after importing.
        """
        
        endpoint = '/'

        if label == None and rescan == None:
            message = '{ "method": "importprivkey", "params": [ "' + private_key + '" ] }'
        elif rescan != None:
            _rescan = ''

            if rescan == True:
                _rescan = '1'
            else:
                _rescan = '0'

            if label == None:
                label = 'Unlabeled'

            message = '{ "method": "importprivkey", "params": [ "' + private_key + '", "' + label + '", ' + _rescan + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to import private key'}"
        return response
    ### END METHOD ################################### rpc_importPrivKey(self, private_key:str, label:str=None, rescan:bool=None)

    def rpc_importWallet(self, wallet_file:str, rescan:bool=False):
        """
        DESCRIPTION:

            Import all keys from a wallet backup file. Also see `hsw.rpc_dumpWallet`.
        
        PARAMS:

            (*) Denotes required argument

            (*) wallet_file : Path to wallet file.

            ( ) rescan  : (bool) Whether to _rescan wallet after importing.
        """
        _rescan = ''

        if rescan == True:
            _rescan = '1'
        else:
            _rescan = '0'
        
        endpoint = '/'

        message = '{ "method": "importwallet", "params": [ "' + wallet_file + '", ' + _rescan + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to import wallet `" + wallet_file + "`'}"
        return response
    ### END METHOD ################################### rpc_importWallet(self, wallet_file:str, rescan:bool=False)

    def rpc_importAddress(self, address:str, label:str=None, rescan:bool=None, p2sh:bool=None):
        """
        DESCRIPTION:

            Import address to a watch-only wallet. May also import a
            Handshake output script (in hex) as pay-to-script-hash
            (P2WSH) address.
        
        PARAMS:

            (*) Denotes required argument

            (*) address : Address to watch in wallet.

            ( ) label   : Ignored but required if additional parameters are passed.

            ( ) rescan  : (bool) Whether to _rescan wallet after importing.

            ( ) p2sh    : (bool) Whether to generate P2SH address from given script.
        """
        
        endpoint = '/'

        if rescan == None and p2sh == None:
            message = '{ "method": "importaddress", "params": [ "' + address + '" ] }'
        else:
            _rescan = ''
            _p2sh = ''

            if rescan == True:
                _rescan = '1'
            else:
                _rescan = '0'

            if p2sh == True:
                _p2sh = '1'
            else:
                _p2sh = '0'
        

            if label == None:
                label = 'Unlabeled'

            message = '{ "method": "importwallet", "params": [ "' + address + '", "' + label + '", ' + str(_rescan) + ', ' + str(_p2sh) + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to import address `" + address + "`'}"
        return response
    ### END METHOD ################################### rpc_importAddress(self, address:str, label:str=None, rescan:bool=None, p2sh:bool=None)

    def rpc_importPrunedFunds(self, tx_hex:str, tx_out_proof:str):
        """
        DESCRIPTION:

            Imports funds (without _rescan) into pruned wallets.
            Corresponding address or script must previously be
            included in wallet. Does NOT check if imported coins
            are already spent, _rescan may be required after the
            point in time in which the specified transaciton was
            included in the blockchain. See `hsd.rpc_getTxOutProof` and
            `hsw.rpc_removePrunedFunds`.
        
        PARAMS:

            (*) Denotes required argument

            (*) tx_hex : Raw transaction in hex that funds an address already in the wallet.

            (*) tx_out_proof : Hex output from `hsd.rpc_getTxOutProof` containing the tx.
        """
        
        endpoint = '/'
        message = '{ "method": "importprunedfunds", "params": [ "' + tx_hex + '", "' + tx_out_proof + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to import pruned funds'}"
        return response
    ### END METHOD ################################### rpc_importPrunedFunds(self, tx_hex:str, tx_out_proof:str)

    def rpc_importPubKey(self, public_hex_key:str, label:str=None, rescan:bool=None):
        """
        DESCRIPTION:

            Import public key to a watch-only wallet.
        
        PARAMS:

            (*) Denotes required argument

            (*) public_hex_key : Hex-encoded public key.

            ( ) label   : Ignored but required if additional parameters are passed.

            ( ) rescan  : (bool) Whether to _rescan wallet after importing.
        """
        
        endpoint = '/'

        if rescan == None:
            message = '{ "method": "importpubkey", "params": [ "' + public_hex_key + '" ] }'
        else:
            _rescan = ''

            if rescan == True:
                _rescan = '1'
            else:
                _rescan = '0'

            if label == None:
                label = 'Unlabeled'

            message = '{ "method": "importpubkey", "params": [ "' + public_hex_key + '", "' + label + '", ' + str(_rescan) + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to public key'}"
        return response
    ### END METHOD ################################### rpc_importPubKey(self, public_hex_key:str, label:str=None, rescan:bool=None)

    def rpc_listAccounts(self, min_confirm:int=None, watch_only:bool=None):
        """
        DESCRIPTION:

            Get list of account names and balances.
        
        PARAMS:

            (*) Denotes required argument

            ( ) min_confirm : Minimum confirmations for transaction to be included in balance.

            ( ) watch_only  : (bool) Include watch-only addresses.
        """
        
        endpoint = '/'

        if min_confirm == None and watch_only == None:
            message = '{ "method": "listaccounts", "params": [] }'
        else:
            _watch_only = ''

            if watch_only == None:
                watch_only = False

            if watch_only == True:
                _watch_only = '1'
            else:
                _watch_only = '0'

            if min_confirm == None:
                min_confirm = 0

            message = '{ "method": "listaccounts", "params": [ ' + str(min_confirm) + ', ' + str(_watch_only) + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get list of wallet accounts and balances'}"
        return response
    ### END METHOD ################################### rpc_listAccounts(self, min_confirm:int=None, watch_only:bool=None)

    def rpc_lockUnspent(self, lock:bool=True, outputs:json=None):
        """
        DESCRIPTION:

            Lock or unlock specified transaction outputs. If no outputs are
            specified, ALL coins will be unlocked (`unlock` only).

            Note: If no paramaters are passed `lock` will default to `True`
        
        PARAMS:

            (*) Denotes required argument

            ( ) lock : (bool) `True` = lock coins, `False` = unlock coins. Default = `True`.

            ( ) outputs  : (bool) Array of outputs to lock or unlock.
        """
        
        endpoint = '/'

        _lock = ''

        if lock == True:
            _lock = '0'
        else:
            _lock = '1'

        if outputs == None:
            message = '{ "method": "lockunspent", "params": [ ' + _lock + ' ] }'
        else:
            message = '{ "method": "lockunspent", "params": [ ' + _lock + ', [' + json.dumps(outputs) + '] ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed lock/unlock unspent coins'}"
        return response
    ### END METHOD ################################### rpc_lockUnspent(self, lock:bool=True, outputs:json=None)

    def rpc_listLockUnspent(self):
        """
        DESCRIPTION:

            Get list of currently locked (unspendable) outputs.
            See `hsw.rpc_lockUnspent` and `hsw.lockCoinOutpoints`.
        
        PARAMS:

            None.
        """
        
        endpoint = '/'
        message = '{ "method": "listlockunspent" }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to list locked unspendable outputs'}"
        return response
    ### END METHOD ################################### rpc_listLockUnspent(self)

    def rpc_listReceivedByAccount(self, min_confirm:int=None, include_empty:bool=None, watch_only:bool=None):
        """
        DESCRIPTION:

            Get balances for all accounts in wallet.
        
        PARAMS:

            (*) Denotes required argument

            ( ) min_confirm   : Minimum confirmations required to count a transaction.

            ( ) include_empty : (bool) Whether to include accounts with zero balance. Default = `False`.

            ( ) watch_only    : (bool) Whether to include watch-only addresses. Default = `False`.
        """
        
        endpoint = '/'

        if min_confirm == None and include_empty == None and watch_only == None:
            message = '{ "method": "listreceivedbyaccount", "params": [] }'
        else:
            _include_empty = ''
            _watch_only = ''

            if include_empty == None:
                include_empty = False

            if include_empty == True:
                _include_empty = '1'
            else:
                _include_empty = '0'

            if watch_only == None:
                watch_only = False

            if watch_only == True:
                _watch_only = '1'
            else:
                _watch_only = '0'

            if min_confirm == None:
                    min_confirm = 0

            message = '{ "method": "listreceivedbyaccount", "params": [ ' + str(min_confirm) + ', ' + str(_include_empty) + ', ' + str(_watch_only) + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get list account balances'}"
        return response
    ### END METHOD ################################### rpc_listReceivedByAccount(self, min_confirm:int=None, include_empty:bool=None, watch_only:bool=None)

    def rpc_listReceivedByAddress(self, min_confirm:int=None, include_empty:bool=None, watch_only:bool=None):
        """
        DESCRIPTION:

            Get balances for all addresses in wallet.
        
        PARAMS:

            (*) Denotes required argument

            ( ) min_confirm   : Minimum confirmations required to count a transaction.

            ( ) include_empty : (bool) Whether to include addresses with zero balance. Default = `False`.

            ( ) watch_only    : (bool) Whether to include watch-only addresses. Default = `False`.
        """
        
        endpoint = '/'

        if min_confirm == None and include_empty == None and watch_only == None:
            message = '{ "method": "listreceivedbyaddress", "params": [] }'
        else:
            _include_empty = ''
            _watch_only = ''

            if include_empty == None:
                include_empty = False

            if include_empty == True:
                _include_empty = '1'
            else:
                _include_empty = '0'

            if watch_only == None:
                watch_only = False

            if watch_only == True:
                _watch_only = '1'
            else:
                _watch_only = '0'

            if min_confirm == None:
                    min_confirm = 0

            message = '{ "method": "listreceivedbyaddress", "params": [ ' + str(min_confirm) + ', ' + str(_include_empty) + ', ' + str(_watch_only) + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get list address balances'}"
        return response
    ### END METHOD ################################### rpc_listReceivedByAddress(self, min_confirm:int=None, include_empty:bool=None, watch_only:bool=None)

    def rpc_listSinceBlock(self, block_hash:str=None, min_confirm:int=None, watch_only:bool=None):
        """
        DESCRIPTION:

            Get all transactions in blocks since a block specified by
            hash, or all transactions if no block is specifiied.
        
        PARAMS:

            (*) Denotes required argument

            ( ) block_hash    : Hash of earliest block to start listing from.

            ( ) min_confirm   : Minimum confirmations required to count a transaction.

            ( ) watch_only    : (bool) Whether to include watch-only addresses. Default = `False`.
        """
        
        endpoint = '/'

        if block_hash == None and min_confirm == None and watch_only == None:
            message = '{ "method": "listsinceblock", "params": [] }'
        else:
            _watch_only = ''

            if watch_only == None:
                watch_only = False

            if watch_only == True:
                _watch_only = '1'
            else:
                _watch_only = '0'

            if min_confirm == None:
                    min_confirm = 0

            message = '{ "method": "listsinceblock", "params": [ "' + block_hash + '", ' + str(min_confirm) + ', ' + str(_watch_only) + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get list transactions since block `" + block_hash + "`'}"
        return response
    ### END METHOD ################################### rpc_listSinceBlock(self, block_hash:str=None, min_confirm:int=None, watch_only:bool=None)

    def rpc_listTransactions(self, account:str='', count:int=0, start_from:int=0, watch_only:bool=None):
        """
        DESCRIPTION:

            Get all recent transactions for specified account up
            to a limit, starting from a specified index.
        
        PARAMS:

            (*) Denotes required argument

            ( ) account    : Account name.

            ( ) count      : Max number of transactions to return.

            ( ) start_from : Number of oldest transactions to skip.

            ( ) watch_only : (bool) Whether to include watch-only addresses. Default = `False`.
        """
        
        endpoint = '/'

        if account == '' and count == 0 and start_from == 0 and watch_only == None:
            message = '{ "method": "listtransactions" }'
        else:
            _watch_only = ''

            if watch_only == None:
                watch_only = False

            if watch_only == True:
                _watch_only = '1'
            else:
                _watch_only = '0'

            message = '{ "method": "listtransactions", "params": [ "' + account + '", ' + str(count) + ', ' + str(start_from) + ', ' + str(_watch_only) + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get transactions for the account `" + account + "`'}"
        return response
    ### END METHOD ################################### rpc_listTransactions(self, account:str='', count:int=0, start_from:int=0, watch_only:bool=None)

    def rpc_listUnspent(self, min_confirm:int=None, max_confirm:int=None, addresses=None):
        """
        DESCRIPTION:

            Get unsepnt transaction outputs from all addreses,
            or a specific set of addresses.
        
        PARAMS:

            (*) Denotes required argument

            ( ) min_confirm : Minimum confirmations required to return tx.

            ( ) max_confirm : Maximum confirmations required to return tx.

            ( ) addresses   : Array of addresses to filter.
        """
        
        endpoint = '/'

        if min_confirm == None and max_confirm == None and addresses == None:
            message = '{ "method": "listunspent" }'
        else:

            if min_confirm == None:
                min_confirm = 0

            if max_confirm == None:
                min_confirm = 0
            
            if addresses == None:
                addresses = '[]'
            else:
                addressCount = 0
                addresses = '['

                for address in addresses:
                    addressCount += 1

                    if addressCount == 1:
                        addresses += '"' + address + '"'
                    else:
                        addresses += ', "' + address + '"'

                addresses += ']'

            message = '{ "method": "listunspent", "params": [ ' + str(min_confirm) + ', ' + str(max_confirm) + ', ' + addresses + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get unspent transaction outputs from addresses'}"
        return response
    ### END METHOD ################################### rpc_listUnspent(self, min_confirm:int=None, max_confirm:int=None, addresses=None)

    def rpc_sendFrom(self, from_account:str, to_address:str, amount:float, min_confirm:int=None):
        """
        DESCRIPTION:

            Send HNS from an account to an address.

            Note: This command involves entering HNS values, be careful with different formats
                  of values for different APIs. See https://hsd-dev.org/api-docs/?shell--curl#values
                  to learn more.
        
        PARAMS:

            (*) Denotes required argument

            (*) from_account : Wallet account to spend outputs from.

            (*) to_address   : Handshake address to send funds to.

            (*) amount       : Amount (in HNS) to send.

            ( ) min_confirm  : Minimum confirmations for output to be spent from.
        """
        
        endpoint = '/'

        if min_confirm == None:
            message = '{ "method": "sendfrom", "params": [ "' + from_account + '", "' + to_address + '", ' + str(amount) + ' ] }'
        else:
            message = '{ "method": "sendfrom", "params": [ "' + from_account + '", "' + to_address + '", ' + str(amount) + ', ' + str(min_confirm) + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to send HNS'}"
        return response
    ### END METHOD ################################### rpc_sendFrom(self, from_account:str, to_address:str, amount:float, min_confirm:int=None)

    def rpc_sendMany(self, from_account:str, outputs:json, min_confirm:int=None, subtract_fee:bool=None, label:str=None):
        """
        DESCRIPTION:

            Send different amounts of HNS from an account to multiple addresses.

            Note: This command involves entering HNS values, be careful with different formats
                  of values for different APIs. See https://hsd-dev.org/api-docs/?shell--curl#values
                  to learn more.
        
        PARAMS:

            (*) Denotes required argument

            (*) from_account : Wallet account to spend outputs from.

            (*) outputs      : (json) of Handshake addresses and amounts to send.

            ( ) min_confirm  : Minimum confirmations for output to be spent from.

            ( ) subtract_fee : (bool) Subtract the transaction fee equally from the output amounts.

            ( ) label        : Ignored but required if additional parameters are passed.
        """
        
        endpoint = '/'

        if min_confirm == None and label == None and subtract_fee == None:
            message = '{ "method": "sendmany", "params": [ "' + from_account + '", ' + json.dumps(outputs) + ' ] }'
        else:
            _subtract_fee = ''

            if min_confirm == None:
                min_confirm = 0

            if label == None:
                label = 'Unlabeled Transaction'
            
            if subtract_fee == True:
                _subtract_fee = '1'
            else:
                _subtract_fee = '0'

            message = '{ "method": "sendmany", "params": [ "' + from_account + '", ' + json.dumps(outputs) + ', ' + str(min_confirm) + ', "' + label + '", ' + _subtract_fee + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to send HNS to multiple addresses'}"
        return response
    ### END METHOD ################################### rpc_sendMany(self, from_account:str, outputs:json, min_confirm:int=None, subtract_fee:bool=None, label:str=None)

    def rpc_createSendToAddress(self, to_address:str, amount:float, subtract_fee:bool=None, comment:str=None, comment_to:str=None):
        """
        DESCRIPTION:

            Create transaction sending HNS to a given address without signing or broadcasting it.

            Note: This command involves entering HNS values, be careful with different formats
                  of values for different APIs. See https://hsd-dev.org/api-docs/?shell--curl#values
                  to learn more.
        
        PARAMS:

            (*) Denotes required argument

            (*) to_address   : Handshake address to send funds to.

            (*) amount       : Amount (in HNS) to send.

            ( ) subtract_fee : (bool) Subtract the transaction fee equally from the output amount.

            ( ) comment      : Ignored but required if additional parameters are passed.

            ( ) comment_to   : Ignored but required if additional parameters are passed.
        """
        
        endpoint = '/'

        if subtract_fee == None and comment == None and comment_to == None:
            message = '{ "method": "createsendtoaddress", "params": [ "' + to_address + '", ' + str(amount) + ' ] }'
        else:
            _subtract_fee = ''

            if comment == None:
                comment = 'No Comment.'

            if comment_to == None:
                comment_to = 'No Comment.'
            
            if subtract_fee == True:
                _subtract_fee = '1'
            else:
                _subtract_fee = '0'

            message = '{ "method": "createsendtoaddress", "params": [ "' + to_address + '", ' + str(amount) + ', "' + comment + '", "' + comment_to + '", ' + _subtract_fee + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to create HNS transaction to address'}"
        return response
    ### END METHOD ################################### rpc_createSendToAddress(self, to_address:str, amount:float, subtract_fee:bool=None, comment:str=None, comment_to:str=None)

    def rpc_sendToAddress(self, to_address:str, amount:float, subtract_fee:bool=None, comment:str=None, comment_to:str=None):
        """
        DESCRIPTION:

            Send HNS to an address.

            Note: This command involves entering HNS values, be careful with different formats
                  of values for different APIs. See https://hsd-dev.org/api-docs/?shell--curl#values
                  to learn more.
        
        PARAMS:

            (*) Denotes required argument

            (*) to_address   : Handshake address to send funds to.

            (*) amount       : Amount (in HNS) to send.

            ( ) subtract_fee : (bool) Subtract the transaction fee equally from the output amount.

            ( ) comment      : Ignored but required if additional parameters are passed.

            ( ) comment_to   : Ignored but required if additional parameters are passed.
        """
        
        endpoint = '/'

        if subtract_fee == None and comment == None and comment_to == None:
            message = '{ "method": "sendtoaddress", "params": [ "' + to_address + '", ' + str(amount) + ' ] }'
        else:
            _subtract_fee = ''

            if comment == None:
                comment = 'No Comment.'

            if comment_to == None:
                comment_to = 'No Comment.'
            
            if subtract_fee == True:
                _subtract_fee = '1'
            else:
                _subtract_fee = '0'

            message = '{ "method": "sendtoaddress", "params": [ "' + to_address + '", ' + str(amount) + ', "' + comment + '", "' + comment_to + '", ' + _subtract_fee + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to send HNS to address'}"
        return response
    ### END METHOD ################################### rpc_sendToAddress(self, to_address:str, amount:float, subtract_fee:bool=None, comment:str=None, comment_to:str=None)

    def rpc_setTxFee(self, tx_fee:float=0):
        """
        DESCRIPTION:

            Set the fee rate for all new transactions until the fee is changed
            again, or set to `0` (will return to automatic fee).

            Note: This command involves entering HNS values, be careful with different formats
                  of values for different APIs. See https://hsd-dev.org/api-docs/?shell--curl#values
                  to learn more.
        
        PARAMS:

            (*) Denotes required argument

            ( ) tx_fee : Fee rate in HNS/kB. Default = `0`
        """
        
        endpoint = '/'

        message = '{ "method": "settxfee", "params": [ ' + str(tx_fee) +' ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to set transaction fee'}"
        return response
    ### END METHOD ################################### rpc_setTxFee(self, tx_fee:float=0)

    def rpc_signMessage(self, address:str, message:str):
        """
        DESCRIPTION:

            Sign an arbitrary message with the private key corresponding to a
            specified Handshake address in the wallet.

            Note: Due to behavior of some shells like bash, if your message
            contains spaces you may need to add additional quotes like
            this: `"'"$message"'"`
        
        PARAMS:

            (*) Denotes required argument

            (*) address : Wallet address to use for signing.

            (*) message : The message to sign.
        """
        
        endpoint = '/'

        message = '{ "method": "signmessage", "params": [ "' + address + '", "' + message + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to sign message'}"
        return response
    ### END METHOD ################################### rpc_signMessage(self, address:str, message:str)

    def rpc_signMessageWithName(self, name:str, message:str):
        """
        DESCRIPTION:

            Sign an arbitrary message with the private key corresponding to
            a Handshake address that owns the specified name in the wallet.

            Note: Due to behavior of some shells like bash, if your message
            contains spaces you may need to add additional quotes like
            this: `"'"$message"'"`
        
        PARAMS:

            (*) Denotes required argument

            (*) name    : Domain name to use for signing.

            (*) message : The message to sign.
        """
        
        endpoint = '/'

        message = '{ "method": "signmessagewithname", "params": [ "' + name + '", "' + message + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to sign message with name'}"
        return response
    ### END METHOD ################################### rpc_signMessageWithName(self, name:str, message:str)

    def rpc_walletLock(self):
        """
        DESCRIPTION:

            Locks the wallet by removing the decryption key from memory.
            See `hsw.rpc_walletPassphrase`.
        
        PARAMS:

            None.
        """
        
        endpoint = '/'
        message = '{ "method": "walletlock" }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to lock wallet'}"
        return response
    ### END METHOD ################################### rpc_walletLock(self)

    def rpc_walletPasswordChange(self, old_passphrase:str, new_passphrase:str):
        """
        DESCRIPTION:

            Change the wallet encryption pasphrase.
        
        PARAMS:

            (*) Denotes required argument

            (*) old_passphrase : The current wallet passphrase.

            (*) new_passphrase : New passphrase.
        """
        
        endpoint = '/'
        message = '{ "method": "walletpassphrasechange", "params": [ "' + old_passphrase + '", "' + new_passphrase + '" ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to change wallet password'}"
        return response
    ### END METHOD ################################### rpc_walletPasswordChange(self, old_passphrase:str, new_passphrase:str)

    def rpc_walletPassphrase(self, passphrase:str, timeout:int=600):
        """
        DESCRIPTION:

            Store wallet decryption key in memory, unlocking the wallet keys.
        
        PARAMS:

            (*) Denotes required argument

            (*) passphrase : The current wallet passphrase.

            ( ) timeout    : Amount of time in seconds decryption key will stay in memory. Default = `600`
        """
        
        endpoint = '/'
        message = '{ "method": "walletpassphrase", "params": [ "' + passphrase + '", ' + str(timeout) + ' ] }'

        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to unlock wallet'}"
        return response
    ### END METHOD ################################### rpc_walletPassphrase(self, passphrase:str, timeout:int=600)

    def rpc_removePrunedFunds(self, tx_id:str):
        """
        DESCRIPTION:

            Deletes the specified transaction from the wallet database.
            See `hsw.rpc_importPrunedFunds`.
        
        PARAMS:

            (*) Denotes required argument

            (*) tx_id : ID of the transaction to remove.
        """
        
        endpoint = '/'

        message = '{ "method": "removeprunedfunds", "params": [ "' + tx_id + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to remove pruned funds'}"
        return response
    ### END METHOD ################################### rpc_removePrunedFunds(self, tx_id:str)

    def rpc_getMemoryInfo(self):
        """
        DESCRIPTION:

            Get information about memory usage. Identical to
            node RPC call `hsd.rpc_getMemoryInfo`.
        
        PARAMS:

            None.
        """
        
        endpoint = '/'

        message = '{ "method": "getmemoryinfo" }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to get memory info'}"
        return response
    ### END METHOD ################################### rpc_getMemoryInfo(self)

    def rpc_setLogLevel(self, log_level:str='NONE'):
        """
        DESCRIPTION:

            Change Log level of the running node.

            Levels are: `NONE`, `ERROR`, `WARNING`, `INFO`, `DEBUG`, `SPAM`
        
        PARAMS:

            (*) Denotes required argument

            ( ) log_level : Level for the logger. Default = `NONE`
        """
        
        endpoint = '/'

        message = '{ "method": "setloglevel", "params": [ "' + log_level + '" ] }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to set log level'}"
        return response
    ### END METHOD ################################### rpc_setLogLevel(self, log_level:str='NONE')

    def rpc_stop(self):
        """
        DESCRIPTION:

            Closes the wallet database.
        
        PARAMS:

            None.
        """
        
        endpoint = '/'

        message = '{ "method": "stop" }'
        try:
            response = self.post(endpoint, message)
        except:
            response = {}
            response['error'] = "{'message': 'RPC failed to close wallet database'}"
        return response
    ### END METHOD ################################### rpc_stop(self)
    