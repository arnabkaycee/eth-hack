'use strict';
const Web3 = require('web3');

const config = require('../config/config.json');
const waterAuctionContract = require("../build/contracts/WaterAuction.json");
const web3 = new Web3(new Web3.providers.WebsocketProvider(`ws://${config.node.address}:${config.node.port}`));
const eaContract = new web3.eth.Contract(waterAuctionContract.abi, config.app.waterAuction);

/**
 *
 * deviceId String  (optional)
 * returns List
 **/
exports.getDeviceUsage = function(deviceId) {
  return new Promise(function(resolve, reject) {
    const deviceIdHex = web3.utils.padRight(web3.utils.utf8ToHex(deviceId),64);
    
    eaContract.getPastEvents('DeviceUsageRegistered',{
      filter: {_deviceId: [deviceIdHex]}, // Using an array means OR: e.g. 20 or 23
      fromBlock: 0,
      toBlock: 'latest'
  },(err,events) => {
    if (err) reject(err);

    console.log(events); // same results as the optional callback above
    let deviceUsages = convertUsageEventsToObject(events);
    resolve(deviceUsages);

  });

  });
}

let convertUsageEventsToObject = function(events){
  let eventObjects = [];
  for (let i = 0; i<events.length; i++){
    let event = events[i].returnValues;
    if (event && typeof event === 'object' && Object.keys(event).length > 0 && Object.keys(event).length % 2 === 0){
      let eventData = {
          usageId:web3.utils.hexToUtf8(event[0]),
          deviceId : web3.utils.hexToUtf8(event[1]),
          timestamp : web3.utils.hexToNumber(event[2]),
          watt : web3.utils.hexToNumber(event[3])
      };
      eventObjects.push(eventData);
    }
  }
  return eventObjects;
}

/**
 * logUsageStats
 * This can only be done by NGO
 *
 * body DeviceUsageStats 
 * no response value expected for this operation
 **/
exports.logUsageStats = function(body) {
  return new Promise(function(resolve, reject) {
    
    const usageId = web3.utils.padRight(web3.utils.utf8ToHex(body.usageId),64);
    const watt = parseInt(body.literConsumed);
    const userId = body.userId;

    const registerDeviceUsageCall = eaContract.methods.registerDeviceUsage(usageId, watt).send({
      from: userId,
      gasPrice: "200",
      gas: "999999"
    }, (err,txHash)=>{
      if (err) reject (err);
      resolve(txHash)
    });


  });
}
