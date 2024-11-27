import pytest
from src.blockchain.block import Block

def test_block_creation():
    block = Block(1, {"test": "data"}, "prev_hash")
    assert block.index == 1
    assert block.data == {"test": "data"}
    assert block.prev_hash == "prev_hash"

def test_block_mining():
    block = Block(1, {"test": "data"}, "prev_hash")
    difficulty = 2
    block.mine_block(difficulty)
    assert block.hash.startswith("0" * difficulty)