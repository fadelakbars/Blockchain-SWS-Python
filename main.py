from src.blockchain.chain import Blockchain
from src.network.mqtt_client import WaterQualityClient
from config.settings import Settings
from src.blockchain.chain import Blockchain

def main():
    blockchain = Blockchain()
    client = WaterQualityClient(blockchain)
    
    print("Starting Water Quality Blockchain...")
    try:
        client.start(Settings.MQTT_BROKER, Settings.MQTT_PORT)
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()