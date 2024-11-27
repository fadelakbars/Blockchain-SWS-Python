from datetime import datetime
import hashlib
import json

class Block:
    def __init__(self, index: int, data: dict, prev_hash: str):
        self.index = index
        self.timestamp = str(datetime.now())
        self.data = data  # Data sensor air
        self.prev_hash = prev_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """Menghitung hash dari block"""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "prev_hash": self.prev_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def mine_block(self, difficulty: int):
        """Mining block dengan proof of work"""
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()