from web3 import Web3

def get_referrer():
    # Connect to your RPC provider
    w3 = Web3(Web3.HTTPProvider('YOUR_RPC_URL'))
    
    # Contract details
    contract_address = 'YOUR_SECRET_CONTRACT_ADDRESS'
    
    # Minimal ABI for ReferedBy function
    abi = [
        {
            "inputs": [],
            "name": "ReferedBy",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function"
        }
    ]
    
    # Create contract instance
    contract = w3.eth.contract(address=contract_address, abi=abi)
    
    try:
        # Call the ReferedBy function
        referrer = contract.functions.ReferedBy().call()
        print(f'Referrer: {referrer}')
        return referrer
    except Exception as e:
        print(f'Error getting referrer: {e}')
        return None

if __name__ == "__main__":
    get_referrer()
