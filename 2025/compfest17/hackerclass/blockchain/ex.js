const { ethers } = require('ethers');

// Your credentials
const RPC_URL = 'http://ctf.compfest.id:7401/f70bebba-209c-4abc-a862-b3c9a6221813';
const PRIVATE_KEY = '7d9aa55dc1d21d793cbd57fdfee5d7db60297717ef95f446925a1f5e0861f943';
const SETUP_CONTRACT_ADDR = '0xE9C6Bd76178af67664130dA89b1e69D7E5EB491C';
const WALLET_ADDR = '0xC146eb404B051FaBD4915E84aBbA105648bf5FBD';

// We already found the secret!
const SECRET_NUMBER = '198514';
const SECRET_SENTENCE = 'Can i join COMPFEST 17? Here is my secret number: 198514';

// Contract ABIs
const setupABI = [
    "function challenge() public view returns (address)",
    "function isSolved() external view returns (bool)"
];

const secretABI = [
    "function guess(string calldata sentence, string calldata referrer) external payable",
    "function ReferedBy() public view returns (string memory)",
    "function GUESS_FEE() public view returns (uint256)",
    "function solved() public view returns (bool)",
    "function isChallengeSolved() public view returns (bool)"
];

async function createProvider() {
    const provider = new ethers.JsonRpcProvider(RPC_URL, undefined, {
        staticNetwork: true // This helps with network detection issues
    });
    
    // Test the connection
    try {
        await provider.getBlockNumber();
        console.log('✅ RPC connection successful');
        return provider;
    } catch (error) {
        console.log('❌ RPC connection failed:', error.message);
        return null;
    }
}

async function getReferrerWithRetry() {
    console.log('\n📖 Getting referrer from contract...');
    
    for (let attempt = 1; attempt <= 3; attempt++) {
        try {
            console.log(`🔄 Attempt ${attempt}/3`);
            
            const provider = new ethers.JsonRpcProvider(RPC_URL, undefined, {
                staticNetwork: true,
                batchMaxCount: 1 // Send requests one at a time
            });
            
            // Get Secret contract address
            const setupContract = new ethers.Contract(SETUP_CONTRACT_ADDR, setupABI, provider);
            const secretContractAddr = await setupContract.challenge();
            console.log('🎯 Secret Contract Address:', secretContractAddr);
            
            // Get referrer
            const secretContract = new ethers.Contract(secretContractAddr, secretABI, provider);
            const referrer = await secretContract.ReferedBy();
            console.log('👤 Referrer:', referrer);
            
            return { secretContractAddr, referrer };
            
        } catch (error) {
            console.log(`❌ Attempt ${attempt} failed:`, error.message);
            if (attempt < 3) {
                console.log('⏳ Waiting 2 seconds before retry...');
                await new Promise(resolve => setTimeout(resolve, 2000));
            }
        }
    }
    
    return null;
}

async function executeGuess(secretContractAddr, referrer) {
    console.log('\n🎲 Executing guess transaction...');
    
    try {
        const provider = new ethers.JsonRpcProvider(RPC_URL, undefined, {
            staticNetwork: true
        });
        const wallet = new ethers.Wallet(PRIVATE_KEY, provider);
        
        const secretContract = new ethers.Contract(secretContractAddr, secretABI, wallet);
        
        // Check current status
        const alreadySolved = await secretContract.solved();
        if (alreadySolved) {
            console.log('✅ Challenge already solved!');
            return true;
        }
        
        // Get guess fee
        const guessFee = await secretContract.GUESS_FEE();
        console.log('💸 Guess Fee:', ethers.formatEther(guessFee), 'ETH');
        
        // Check balance
        const balance = await provider.getBalance(WALLET_ADDR);
        console.log('💰 Balance:', ethers.formatEther(balance), 'ETH');
        
        if (balance < guessFee) {
            console.log('❌ Insufficient balance!');
            return false;
        }
        
        console.log('📝 Sending transaction with:');
        console.log('   Sentence:', SECRET_SENTENCE);
        console.log('   Referrer:', referrer);
        console.log('   Value:', ethers.formatEther(guessFee), 'ETH');
        
        // Send transaction
        const tx = await secretContract.guess(SECRET_SENTENCE, referrer, {
            value: guessFee,
            gasLimit: 300000
        });
        
        console.log('📤 Transaction sent:', tx.hash);
        console.log('⏳ Waiting for confirmation...');
        
        const receipt = await tx.wait();
        console.log('✅ Transaction confirmed!');
        console.log('⛽ Gas used:', receipt.gasUsed.toString());
        
        // Verify success
        const isSolved = await secretContract.isChallengeSolved();
        console.log('🏆 Challenge solved:', isSolved);
        
        return isSolved;
        
    } catch (error) {
        console.error('❌ Transaction failed:', error.message);
        return false;
    }
}

async function solveCTFRobust() {
    console.log('🚀 Starting COMPFEST 17 CTF Solution (Robust Version)...');
    console.log('🔢 Using found secret number:', SECRET_NUMBER);
    console.log('📝 Using sentence:', SECRET_SENTENCE);
    
    // Step 1: Get referrer and contract address
    const contractInfo = await getReferrerWithRetry();
    if (!contractInfo) {
        console.log('❌ Failed to get contract information');
        console.log('\n🔧 Manual steps:');
        console.log('1. Use a blockchain explorer to call ReferedBy() on the Secret contract');
        console.log('2. Use the sentence:', SECRET_SENTENCE);
        console.log('3. Send 0.5 ETH to the guess() function');
        return;
    }
    
    // Step 2: Execute the guess
    const success = await executeGuess(contractInfo.secretContractAddr, contractInfo.referrer);
    
    if (success) {
        console.log('\n🎉🎉🎉 CHALLENGE COMPLETED! 🎉🎉🎉');
    } else {
        console.log('\n❌ Challenge not completed. Try manual approach.');
    }
}

// Manual approach information
function showManualSteps() {
    console.log('\n🔧 Manual Steps (if RPC is unstable):');
    console.log('');
    console.log('1. SECRET SENTENCE FOUND:');
    console.log(`   "${SECRET_SENTENCE}"`);
    console.log('');
    console.log('2. Get referrer using blockchain explorer or cast:');
    console.log('   - Go to block explorer for your network');
    console.log('   - Navigate to Setup contract:', SETUP_CONTRACT_ADDR);  
    console.log('   - Call challenge() to get Secret contract address');
    console.log('   - Call ReferedBy() on Secret contract to get referrer');
    console.log('');
    console.log('3. Or use cast commands:');
    console.log(`   cast call ${SETUP_CONTRACT_ADDR} "challenge()" --rpc-url ${RPC_URL}`);
    console.log('   cast call SECRET_CONTRACT_ADDRESS "ReferedBy()" --rpc-url', RPC_URL);
    console.log('   cast --to-ascii RETURNED_HEX_DATA');
    console.log('');
    console.log('4. Send transaction:');
    console.log(`   cast send SECRET_CONTRACT_ADDRESS "guess(string,string)" "${SECRET_SENTENCE}" "REFERRER_VALUE" --value 0.5ether --private-key ${PRIVATE_KEY} --rpc-url ${RPC_URL}`);
}

// Alternative: Use cast commands
function showCastCommands() {
    console.log('\n⚡ Cast Commands (Foundry CLI):');
    console.log('');
    console.log('# 1. Get Secret contract address:');
    console.log(`cast call ${SETUP_CONTRACT_ADDR} "challenge()" --rpc-url ${RPC_URL}`);
    console.log('');
    console.log('# 2. Get referrer (replace SECRET_ADDR with result from step 1):');
    console.log('cast call SECRET_ADDR "ReferedBy()" --rpc-url', RPC_URL);
    console.log('');
    console.log('# 3. Decode referrer:');
    console.log('cast --to-ascii HEX_RESULT');
    console.log('');
    console.log('# 4. Send guess transaction:');
    console.log(`cast send SECRET_ADDR "guess(string,string)" "${SECRET_SENTENCE}" "REFERRER_VALUE" --value 0.5ether --private-key ${PRIVATE_KEY} --rpc-url ${RPC_URL}`);
}

// Run based on what you need
console.log('🎯 We found the secret! Now choose:');
console.log('1. Try robust solution: solveCTFRobust()');
console.log('2. Show manual steps: showManualSteps()');
console.log('3. Show cast commands: showCastCommands()');

// Try the robust solution
solveCTFRobust().catch(console.error);

// Also show alternatives
showCastCommands();
showManualSteps();

┌──(venv)(ilupii㉿asusVivobook)-[/mnt/d/ctf/compfest17/blockchain]
└─$ cast call 0xE9C6Bd76178af67664130dA89b1e69D7E5EB491C "challenge()" --rpc-url http://ctf.compfest.id:7401/f70bebba-209c-4abc-a862-b3c9a6221813
0x0000000000000000000000000ab9d79156ad2c51453ad1e9a9163d18b845f8a2

┌──(venv)(ilupii㉿asusVivobook)-[/mnt/d/ctf/compfest17/blockchain]
└─$ cast call 0x0000000000000000000000000ab9d79156ad2c51453ad1e9a9163d18b845f8a2 "ReferedBy()" --rpc-url http://ctf.compfest.id:7401/f70bebba-209c-4abc-a862-b3c9a6221813
error: invalid value '0x0000000000000000000000000ab9d79156ad2c51453ad1e9a9163d18b845f8a2' for '[TO]': invalid string length

For more information, try '--help'.

┌──(venv)(ilupii㉿asusVivobook)-[/mnt/d/ctf/compfest17/blockchain]
└─$ # Get the referrer
cast call 0x0ab9d79156ad2c51453ad1e9a9163d18b845f8a2 "ReferedBy()" --rpc-url http://ctf.compfest.id:7401/f70bebba-209c-4abc-a862-b3c9a6221813
^C

┌──(venv)(ilupii㉿asusVivobook)-[/mnt/d/ctf/compfest17/blockchain]
└─$ cast call 0x0ab9d79156ad2c51453ad1e9a9163d18b845f8a2 "ReferedBy()" --rpc-url http://ctf.compfest.id:7401/f70bebba-209c-4abc-a862-b3c9a6221813
0x0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000002b544f4d415320414c5048415244204544492d534f554e442062657273616d612044654a6179204f4849454d000000000000000000000000000000000000000000

┌──(venv)(ilupii㉿asusVivobook)-[/mnt/d/ctf/compfest17/blockchain]
└─$ 0x0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000002b544f4d415320414c5048415244204544492d534f554e442062657273616d612044654a6179204f4849454d000000000000000000000000000000000000000000^Cst --to-ascii

┌──(venv)(ilupii㉿asusVivobook)-[/mnt/d/ctf/compfest17/blockchain]
└─$ cast --to-ascii 0x0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000002b544f4d415320414c5048415244204544492d534f554e442062657273616d612044654a6179204f4849454d000000000000000000000000000000000000000000
 +TOMAS ALPHARD EDI-SOUND bersama DeJay OHIEM

┌──(venv)(ilupii㉿asusVivobook)-[/mnt/d/ctf/compfest17/blockchain]
└─$ cast send 0x0ab9d79156ad2c51453ad1e9a9163d18b845f8a2 "guess(string,string)" "Can i join COMPFEST 17? Here is my secret number: 198514" "TOMAS ALPHARD EDI-SOUND bersama DeJay OHIEM" --value 0.5ether --private-key 7d9aa55dc1d21d793cbd57fdfee5d7db60297717ef95f446925a1f5e0861f943 --rpc-url http://ctf.compfest.id:7401/f70bebba-209c-4abc-a862-b3c9a6221813

blockHash            0x02124e63aa662f7f33556bd536e403199df3412fc15e9689abf4712443743db0
blockNumber          2
contractAddress
cumulativeGasUsed    47623
effectiveGasPrice    1000000000
from                 0xC146eb404B051FaBD4915E84aBbA105648bf5FBD
gasUsed              47623
logs                 []
logsBloom            0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
root
status               1 (success)
transactionHash      0x0542bda9e5bb9783e7a3db397d88acbad4c94a081f294c9a603bddda4cb008d6
transactionIndex     0
type                 2
blobGasPrice         1
blobGasUsed
to                   0x0AB9D79156aD2c51453aD1e9A9163d18B845F8A2

┌──(venv)(ilupii㉿asusVivobook)-[/mnt/d/ctf/compfest17/blockchain]
└─$ cast call 0x0ab9d79156ad2c51453ad1e9a9163d18b845f8a2 "solved()" --rpc-url http://ctf.compfest.id:7401/f70bebba-209c-4abc-a862-b3c9a6221813
0x0000000000000000000000000000000000000000000000000000000000000001

┌──(venv)(ilupii㉿asusVivobook)-[/mnt/d/ctf/compfest17/blockchain]
└─$ cast call 0xE9C6Bd76178af67664130dA89b1e69D7E5EB491C "isSolved()" --rpc-url http://ctf.compfest.id:7401/f70bebba-209c-4abc-a862-b3c9a6221813
0x0000000000000000000000000000000000000000000000000000000000000001

┌──(venv)(ilupii㉿asusVivobook)-[/mnt/d/ctf/compfest17/blockchain]
└─$ cast send
Error: error sending request for url (http://localhost:8545/)

Context:
- Error #0: client error (Connect)
- Error #1: tcp connect error: Connection refused (os error 111)