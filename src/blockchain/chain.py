from typing import List
from .block import Block
from src.database.db import MongoDB
class Blockchain:
    def __init__(self, difficulty=2):
        self.difficulty = difficulty
        self.db = MongoDB()  # Inisialisasi MongoDB
        # Jika database kosong, buat genesis block
        if self.db.collection.count_documents({}) == 0:
            self.create_genesis_block()
        else:
            # Muat blockchain dari database
            self.chain = self.db.get_all_blocks()

    def create_genesis_block(self):
        """Membuat blok genesis."""
        genesis_block = Block(0, {"message": "Genesis Block"}, "0")
        genesis_block.mine_block(self.difficulty)
        self.db.insert_block(genesis_block.__dict__)  # Simpan ke MongoDB
        print("Genesis block created!")

    # def add_block(self, data):
    #     """Tambah blok baru ke blockchain."""
    #     prev_block = self.get_latest_block()
    #     new_block = Block(
    #         prev_block["index"] + 1, data, prev_block["hash"]
    #     )
    #     new_block.mine_block(self.difficulty)
    #     self.db.insert_block(new_block.__dict__)  # Simpan ke MongoDB
    #     print(f"Block added: {new_block.__dict__}")

    def add_block(self, data):
        """Tambah blok baru ke blockchain."""
        prev_block = self.get_latest_block()
        new_block = Block(
            index=prev_block["index"] + 1 if prev_block else 0,
            data=data,
            prev_hash=prev_block["hash"] if prev_block else "0"
        )
        new_block.mine_block(self.difficulty)
        self.db.insert_block(new_block.__dict__)  # Simpan ke MongoDB
        print(f"Block added: {new_block.__dict__}")
        
    def get_latest_block(self):
        """Ambil blok terakhir dari database."""
        return self.db.get_latest_block()
    
    def get_all_blocks(self):
        """Ambil semua blok dari database."""
        return self.db.get_all_blocks()

