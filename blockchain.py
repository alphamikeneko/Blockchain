class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self):
        # Create a new block and add it to the chain.
        pass

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
        pass
    
    @property
    def last_block(self):
        # Return the last block in the chain.
        pass
