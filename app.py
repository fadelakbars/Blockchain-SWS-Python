from flask import Flask, render_template
from src.blockchain.chain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    blocks = blockchain.get_all_blocks()
    
    # Format ulang data
    formatted_blocks = []
    for block in blocks:
        formatted_blocks.append({
            "index": block["index"],
            "timestamp": block["timestamp"],
            "transactions": ", ".join(
                [f"{key}: {value}" for key, value in block["data"].items()]
            ) if block["data"] else "No transactions",
            "hash": block["hash"],
            "prev_hash": block["prev_hash"]
        })
    
    return render_template('index.html', blocks=formatted_blocks)


if __name__ == '__main__':
    app.run(debug=True)
