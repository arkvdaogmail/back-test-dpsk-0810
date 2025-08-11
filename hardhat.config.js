import '@vechain/sdk-hardhat-plugin';

const config = {
  solidity: {
    compilers: [
      {
        version: '0.8.20',
        settings: {
          optimizer: { enabled: true, runs: 200 },
          evmVersion: 'paris'
        }
      }
    ]
  },
  networks: {
    vechain_testnet: {
      url: 'https://testnet.vechain.org',
      accounts: [/* your private key or mnemonic config */],
      gas: 'auto',
      gasPrice: 'auto'
    }
  }
};

export default config;
