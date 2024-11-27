from src.blockchain.chain import Blockchain
from src.network.mqtt_client import WaterQualityClient
from config.settings import Settings

def main():
    blockchain = Blockchain(Settings.BLOCKCHAIN_DIFFICULTY)
    client = WaterQualityClient(blockchain)
    
    print("Starting Water Quality Blockchain...")
    try:
        client.start(Settings.MQTT_BROKER, Settings.MQTT_PORT)
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()