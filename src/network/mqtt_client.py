import paho.mqtt.client as mqtt
import json
from ..blockchain.chain import Blockchain

class WaterQualityClient:
    def __init__(self, blockchain: Blockchain):
        self.blockchain = blockchain
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
    
    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected to MQTT broker with code {rc}")
        client.subscribe("water/quality")
    
    # def on_message(self, client, userdata, msg):
    #     try:
    #         data = json.loads(msg.payload.decode())
    #         self.blockchain.add_block(data)
    #         print(f"Added block with data: {data}")
    #     except Exception as e:
    #         print(f"Error: {e}")
            
    def on_message(self, client, userdata, msg):
        try:
            raw_payload = msg.payload.decode()
            print(f"Raw Payload Received: {raw_payload}")
            data = json.loads(raw_payload)
            self.blockchain.add_block(data)
            print(f"Added block with data: {data}")
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
            print("Blockchain Data:")
        for block in self.blockchain.get_all_blocks():
            block.pop('_id', None)  # Hapus ObjectId dari output
            print(block)

    
    def start(self, broker="localhost", port=1883):
        self.client.connect(broker, port, 60)
        self.client.loop_forever()