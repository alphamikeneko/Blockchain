import hashlib
import json

from time import time
from uuid import uuid4


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        # Create a new block and add it to the chain.
        # :param proof: <int>
        # :param previous_hash: <str>
        # :return: <dict>
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipinet, amount):
        # Add a new transaction to the list.
        # :param sender: <str>
        # :param recipient: <str>
        # :param amount: <int>
        # :return: <int>

        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        
        return self.last_block['index'] + 1

    
    @staticmethod
    def hash(block):
        # Hash the block.
        # :param block: <dict>
        # :return: <str>
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    @property
    def last_block(self):
        # Return the last block in the chain.
        return self.chain[-1]

    
    def proof_of_work(self, last_proof):
        # :param last_proof: <int>
        # :return: <int>
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
