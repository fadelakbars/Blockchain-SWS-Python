from typing import List
from .block import Block
from src.database.db import MongoDB
from datetime import datetime

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
        # genesis_block = Block(0, {"message": "Genesis Block"}, "0")
        genesis_block = Block(
            index=0,
            data={"message": "Genesis Block"},
            prev_hash="0",
            timestamp=str(datetime.now())  # Tambahkan timestamp
        )
        genesis_block.mine_block(self.difficulty)
        self.db.insert_block(genesis_block.__dict__)  # Simpan ke MongoDB
        print("Genesis block created!")

    def add_block(self, data):
        """Tambah blok baru ke blockchain."""
        prev_block = self.get_latest_block()
        new_block = Block(
            index=prev_block["index"] + 1 if prev_block else 0,
            data=data,
            prev_hash=prev_block["hash"] if prev_block else "0",
            timestamp=str(datetime.now())
        )
        new_block.mine_block(self.difficulty)
        print(f"New block hash: {new_block.hash}")
        self.db.insert_block(new_block.__dict__)  # Simpan ke MongoDB
        print(f"Block added: {new_block.__dict__}")
        
        if self.is_chain_valid():
            print("Blockchain is valid after adding block.")
        else:
            print("Blockchain is invalid after adding block.")

        
    def get_latest_block(self):
        """Ambil blok terakhir dari database."""
        return self.db.get_latest_block()
    
    def get_all_blocks(self):
        """Ambil semua blok dari database."""
        return self.db.get_all_blocks()
    
    def is_chain_valid(self):
        blocks = self.get_all_blocks()
        for i in range(1, len(blocks)):
            prev_block = blocks[i - 1]
            current_block = blocks[i]

            if "_id" in current_block:
                del current_block["_id"]
            if "_id" in prev_block:
                del prev_block["_id"]

            if current_block["prev_hash"] != prev_block["hash"]:
                print(f"Blockchain broken at block {current_block['index']}")
                return False

            temp_block = Block(
                index=current_block["index"],
                data=current_block["data"],
                prev_hash=current_block["prev_hash"],
                timestamp=current_block["timestamp"]
            )
            temp_block.nonce = current_block["nonce"]  # Set the nonce before hash calculation
            temp_block.hash = temp_block.calculate_hash()

            if current_block["hash"] != temp_block.hash:
                print(f"Block {current_block['index']} hash invalid")
                print(f"Stored hash: {current_block['hash']}")
                print(f"Recalculated hash: {temp_block.hash}")
                return False

        print("Blockchain is valid.")
        return True