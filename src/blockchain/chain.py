from typing import List
from .block import Block

class Blockchain:
    def __init__(self, difficulty: int = 2):
        self.chain: List[Block] = []
        self.difficulty = difficulty
        self.create_genesis_block()
    
    def create_genesis_block(self):
        """Membuat block pertama"""
        genesis_block = Block(0, {"message": "Genesis Block"}, "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)
    
    def get_latest_block(self) -> Block:
        return self.chain[-1]
    
    def add_block(self, data: dict):
        """Menambah block baru"""
        prev_block = self.get_latest_block()
        new_block = Block(prev_block.index + 1, data, prev_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)