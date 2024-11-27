from pymongo import MongoClient

class MongoDB:
    def __init__(self, db_name="blockchain_python_1", collection_name="blocks"):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_block(self, block_data):
        self.collection.insert_one(block_data)

    def get_all_blocks(self):
        return list(self.collection.find())
    
    def get_latest_block(self):
        """Ambil blok terakhir berdasarkan indeks tertinggi."""
        return self.collection.find_one(sort=[("index", -1)])

