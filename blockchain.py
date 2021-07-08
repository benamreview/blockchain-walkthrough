import hashlib
import json
class Block:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = {
            "transaction_list": transaction_list,
            "previous_block_hash": previous_block_hash
        }
        self.block_hash = hashlib.sha256(json.dumps(self.block_data).encode()).hexdigest()


t1 = "Happy Birthday to You Mike!"
t2 = "Thank you Michelle!"
t3 = "Happy Birthday to You Bob!"
t4 = "Thanks!!"
t5 = "Happy Birthday to You Lona!"
t6 = "Thank you Paul!!"

