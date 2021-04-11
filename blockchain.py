import hashlib
import json
import datetime

class Blockchain(object):
    def __init__(self):
        #Empty blockchain
        self.blockchain = []
        #Pending transactions to be mined
        self.pending_transactions = []
        self.nonce = 0
        #Creating Genesis block
        self.new_block("Genesis") 

    #Creates new block and removes pending transactions
    def new_block(self, previous_hash=None):
        #New Block
        block = {
            "index" : len(self.blockchain) ,
            'timestamp': str(datetime.datetime.now()),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash or self.mine_block(self.blockchain[-1]),
            'nonce': self.nonce,
        }
        #Clear pending transactions
        self.pending_transactions = []
        self.blockchain.append(block)

        return block
    
    #Returns previous block to be hashed
    def last_block(self):
        return self.blockchain[-1]

    
    #Stores each transaction
    def new_transaction(self, sender, recipient, amount):
        #single transaction
        transaction = {
            "Sender" : sender,
            "Recipient" : recipient,
            "Amount" : amount
        }
        #Appending to pending transactions
        self.pending_transactions.append(transaction)

    def mine_block(self, last_block) :
        #Dictionary type to json type
        string_object = json.dumps(last_block)

        #Encodes string
        text_encode = string_object.encode()

        #Returns hash object in hex format
        raw_hash = hashlib.sha256(text_encode)

        #Digesting hash object to string
        hex_hash = raw_hash.hexdigest()
        
        #Verified block condition
        prefix_zeroes = 4

        #local nonce to be appended
        nonce = 0

        #Looping till block is verified
        while(hex_hash[:prefix_zeroes] != ("0" * prefix_zeroes)):
            string_object = json.dumps(last_block)
            string_object += str(nonce)
            text_encode = string_object.encode()
            raw_hash = hashlib.sha256(text_encode)
            hex_hash = raw_hash.hexdigest()
            nonce += 1

        #Updating global nonce
        self.nonce = nonce
        return hex_hash

    def return_blockchain(self):
        return self.blockchain

"""blockchain = Blockchain()

blockchain.new_transaction("Rajiv", "Tanush", '5 BTC')
blockchain.new_transaction("Tanush", "Pradyumna", '1 BTC')
blockchain.new_transaction("Pradyumna", "Rajiv", '5 BTC')
blockchain.new_block()

blockchain.new_transaction("Elon Musk", "Bill Gates", '100 BTC')
blockchain.new_transaction("Bill Gates", "Jeff Bezos", '250 BTC')
blockchain.new_transaction("Jeff Bezos", "Mark Zuckerberg", '720 BTC')
blockchain.new_block()

print(blockchain.return_blockchain())"""

    






