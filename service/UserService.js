'use strict';
const Web3 = require('web3');

const config = require('../config/config.json');
const energyAuctionContract = require("../build/contracts/EnergyAuction.json");
const web3 = new Web3(new Web3.providers.WebsocketProvider(`ws://${config.node.address}:${config.node.port}`));
const eaContract = new web3.eth.Contract(energyAuctionContract.abi, config.app.energyAuction);
/**
 * Create user
 * This can only be done by the logged in user.
 *
 * body User Created user object
 * no response value expected for this operation
 **/


exports.createUser = function(body) {
  return new Promise(function(resolve, reject) {
    const userId = web3.utils.padRight(web3.utils.utf8ToHex(body.userId),64);
    const address = body.address;
    const userType = parseInt(body.userType);
    const deviceId = web3.utils.padRight(web3.utils.utf8ToHex(body.deviceId),64);
    const deviceType = parseInt(body.deviceType);

    const createUserCall = eaContract.methods.createUser(userId, userType, address, deviceId, deviceType).send({
      from: config.userAccounts.ngo,
      gasPrice: "200",
      gas: "99999"
    },(err,txHash)=>{
      if (err) reject(err);
      resolve(txHash);
    });
  });
}


/**
 *
 * userId String  (optional)
 * returns List
 **/
exports.getUsers = function(userId) {
  return new Promise(function(resolve, reject) {
    
    
    const createUserCall = eaContract.methods.getUser(userId).call({
        
      from: config.userAccounts.ngo,
      gasPrice: "200",
      gas: "99999"
    }, (err, result) => {

      if (err) reject(err);

      console.log(result);
      if (result && typeof result === 'object' && Object.keys(result).length ==6){
        let userId = web3.utils.hexToUtf8(result[0]);
        if(userId){
          let userObject = {
            "userId": web3.utils.hexToUtf8(result[0]),
            "deviceId": web3.utils.hexToUtf8(result[1]),
            "deviceType": web3.utils.hexToNumber(result[2]),
            "address": result[3],
            "userType": web3.utils.hexToNumber(result[4]),
            "walletBalance": web3.utils.hexToNumber(result[5])
          };
          resolve([userObject]);
        }else {resolve([])};
      }else {reject("Some error occured :"+result)}
    });   

  });
}
