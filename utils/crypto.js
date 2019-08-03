const ethCrypto = require('eth-crypto');
const secp256k1 = require('@aztec/secp256k1');

const Web3 = require('web3');
const config = require('../config/config.json');

const energyAuctionContract = require("../build/contracts/EnergyAuction.json");
const web3 = new Web3(new Web3.providers.WebsocketProvider(`ws://${config.node.address}:${config.node.port}`));
const eaContract = new web3.eth.Contract(energyAuctionContract.abi, config.app.energyAuction);



const encryptMessage = async (publicKey, msg) => {
    const encrypted = await ethCrypto.encryptWithPublicKey(
        publicKey.slice(4),
        msg,
    );
    return ethCrypto.cipher.stringify(encrypted);
};

const decryptMessage = async (privateKey, encryptedMsg) =>
    ethCrypto.decryptWithPrivateKey(
        privateKey,
        ethCrypto.cipher.stringify(encryptedMsg),
        );

const validatePrivateKeyFormat = (privateKey) => {
    let formattedKey = privateKey;
    if (formattedKey.length === 64) {
        formattedKey = `0x${formattedKey}`;
    }
    if (!formattedKey.match(/^0x[a-f0-9]{64}$/i)) {
        console.log('Private key format not valid', privateKey);
        return '';
    }
    return formattedKey;
};

const privateKeyToPublicKey = (privateKey) => {
    const validPrivateKey = validatePrivateKeyFormat(privateKey);
    if (!validPrivateKey) {
        return '';
    }

    const {
        publicKey,
    } = secp256k1.accountFromPrivateKey(validPrivateKey);
    return publicKey;
};



const validate = async function () {

    //const privateKey = '0xd8e70f46bcdd6c0437779bad4b927cb9160490620e7c69d9c26dbf7ddbf69701';
    const privateKey = '16ac9ab555191da02f53884c255b8bd1659a2dd0350e66e170e17343dc1da815';
    const publicKey = privateKeyToPublicKey(privateKey);
    const msg = '0x2b70f4d74af494af185b5f1077e3afabea22be1d766221c0cef8da8178cbc547000001f403fa453653e56aeac3286da7931f9df9376de7e59d9dba9f2f1af41924f34cc883';
    const encrypted = await encryptMessage(publicKey, msg);


    const decrypted = await decryptMessage(privateKey, encrypted);


    console.log(`encrypted : ${encrypted}`);
    console.log(`decrypted : ${decrypted}`);

};

const stringToBytes32 = function(str){
    return web3.utils.padRight(web3.utils.utf8ToHex(str),64);
};

const bytes32ToString = function(str) {
    return web3.utils.hexToUtf8(str);
};

const hexToNumber = function(hexStr) {
    return web3.utils.hexToNumber(hexStr);
};

const  numberToHex = function(number) {
    return web3.utils.numberToHex(numberToHex);
};

module.exports = {encryptMessage, decryptMessage, validatePrivateKeyFormat, privateKeyToPublicKey, validate, stringToBytes32, bytes32ToString, numberToHex, hexToNumber};

//validate();
