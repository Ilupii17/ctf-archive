from Crypto.Hash import keccak

def find_secret():
    target = bytes.fromhex("726061b2dddd96177e52d122926939b0608ac99930f2f980c08045e863f6ecf3")
    
    for i in range(1000000):
        number = str(i).zfill(6)
        sentence = f"Can i join COMPFEST 17? Here is my secret number: {number}"
        
        # Calculate keccak256 hash
        k = keccak.new(digest_bits=256)
        k.update(sentence.encode('utf-8'))
        hash_result = k.digest()
        
        if hash_result == target:
            print(f"Found it!")
            print(f"Number: {number}")
            print(f"Sentence: {sentence}")
            print(f"Hash: {hash_result.hex()}")
            return sentence
        
        if i % 10000 == 0:
            print(f"Checked {i} numbers...")
    
    print("Not found!")
    return None

if __name__ == "__main__":
    find_secret()


# GANTI SEMUA YANG DI DALAM <>
cast send 726061b2dddd96177e52d122926939b0608ac99930f2f980c08045e863f6ecf3 \
  "guess(string,string)" \
  "Can i join COMPFEST 17? Here is my secret number: 198514" \
  "<STRING_REFERRER_YANG_ANDA_TEMUKAN>" \
  --value 0.5ether \
  --private-key <PRIVATE_KEY_ANDA> \
  --rpc-url <RPC_URL_ANDA>