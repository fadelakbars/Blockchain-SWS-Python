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
    
    def on_message(self, client, userdata, msg):
        try:
            raw_payload = msg.payload.decode()
            data = json.loads(raw_payload)
            self.blockchain.add_block(data)
            print(f"Added block with data: {data}")
            
            # Validasi blockchain setelah blok ditambahkan
            if self.blockchain.is_chain_valid():
                print("Blockchain is valid.")
            else:
                print("Blockchain is invalid!")
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        except Exception as e:
            print(f"Error: {e}")


    
    def start(self, broker="localhost", port=1883):
        self.client.connect(broker, port, 60)
        self.client.loop_forever()