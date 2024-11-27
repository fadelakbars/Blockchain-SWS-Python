from datetime import datetime
import hashlib
import json

class Block:
    def __init__(self, index, data, prev_hash, timestamp=None):
        self.index = index
        self.timestamp = timestamp if timestamp else str(datetime.now())
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        data_to_hash = f"{self.index}{self.timestamp}{json.dumps(self.data, sort_keys=True)}{self.prev_hash}{self.nonce}"
        return hashlib.sha256(data_to_hash.encode()).hexdigest()

    def mine_block(self, difficulty: int):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()