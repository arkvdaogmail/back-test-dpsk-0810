import os
from thor_devkit import transaction, cry
import requests

# 1. Load config (replace values if not using .env)
PRIVATE_KEY = os.getenv('PRIVATE_KEY', 'your_private_key_hex')
NODE_URL = os.getenv('NODE_URL', 'https://testnet.vechain.org')
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS', '0xYourContractAddress')

# 2. Prepaid gas function
def vechain_prepaid_gas_flow(content_hash):
    """Test sending a transaction with prepaid gas"""
    tx = transaction.Transaction({
        "chainTag": 0x4a,  # Testnet
        "blockRef": "0x0000000000000000",
        "expiration": 720,
        "clauses": [{
            "to": CONTRACT_ADDRESS,
            "value": 0,
            "data": "0x" + content_hash
        }],
        "gasPriceCoef": 0,
        "gas": 50000
    })
    
    # Sign
    tx.signature = cry.secp256k1.sign(
        tx.get_signing_hash(),
        bytes.fromhex(PRIVATE_KEY)
    
    # Send
    response = requests.post(
        f"{NODE_URL}/transactions",
        json={"raw": "0x" + tx.encode().hex()}
    )
    return response.json().get('id')

# 3. Test execution
if __name__ == '__main__':
    print("=== TEST START ===")
    try:
        tx_id = vechain_prepaid_gas_flow("a1b2" * 16)  # Test hash
        print(f"✅ TX Successful! ID: {tx_id}")
        print(f"Explorer: https://explore-testnet.vechain.org/transactions/{tx_id}")
    except Exception as e:
        print(f"❌ Failed: {str(e)}")
    print("=== TEST END ===")
