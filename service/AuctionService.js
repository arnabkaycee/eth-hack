'use strict';
const Web3 = require('web3');
const config = require('../config/config.json');
const userService = require('./UserService');
const energyAuctionContract = require("../build/contracts/EnergyAuction.json");
const web3 = new Web3(new Web3.providers.WebsocketProvider(`ws://${config.node.address}:${config.node.port}`));
const eaContract = new web3.eth.Contract(energyAuctionContract.abi, config.app.energyAuction);

/**
 * Create auction
 * This can only be done by NGO
 *
 * body Auction 
 * no response value expected for this operation
 **/
exports.createAuction = function(body) {
  return new Promise(function(resolve, reject) {
    
    const auctionId = web3.utils.padRight(web3.utils.utf8ToHex(body.auctionId),64);
    const addresses = body.users;
    const totalIncentive = parseInt(body.totalIncentive);
    const wattHourGoalSaving = parseInt(body.wattHourGoalSaving);
    const bidStartTimestamp = parseInt(body.bidStartTimestamp);
    const bidEndTimestamp = parseInt(body.bidEndTimestamp);
    const offStartTimestamp = parseInt(body.offStartTimestamp);
    const offEndTimestamp = parseInt(body.offEndTimestamp);

    const createUserCall = eaContract.methods.createAuction(auctionId, totalIncentive, 
      wattHourGoalSaving, bidStartTimestamp, 
      bidEndTimestamp, offStartTimestamp, 
      offEndTimestamp, addresses).send({

      from: config.userAccounts.ngo,
      gasPrice: "200",
      gas: "999999999"
    }, (err,txHash)=>{
      if (err) reject (err);
      resolve(txHash)
    });

  });
};

/**
 * This can only be done by NGO
 *
 * body Auction 
 * no response value expected for this operation
 **/
exports.closeAuction = function(body) {
  return new Promise(function(resolve, reject) {
    
    const auctionIdHex = web3.utils.padRight(web3.utils.utf8ToHex(body.auctionId),64);
    
    //TODO 
    let maxIncentive = 0;
    const getAuctionCall = eaContract.methods.getAuction(auctionIdHex).call({
        
      from: config.userAccounts.ngo,
      gasPrice: "200",
      gas: "999999999"
    }).then((result)=> {
      console.log(result);
      if (result && typeof result === 'object' && Object.keys(result).length ==7){
        let auctionId = web3.utils.hexToUtf8(result[0]);
        if(auctionId){
          maxIncentive = web3.utils.hexToNumber(result[1]);


    //SC-CALL - getAuctionBids
    const getAuctionBidsCall = eaContract.methods.getAuctionBids(auctionIdHex).call({
      from: config.userAccounts.ngo,
      gasPrice: "200",
      gas: "999999999"
  }).then((result)=> {
    console.log(result);
    if (result && typeof result === 'object' && Object.keys(result).length ==3){
      let bidArr = [];

      //create the array of bid objects
      for (let i=0; i<result[0].length;i++){
        let bidObj = {
          bidId : web3.utils.hexToUtf8(result[0][i]),
          bidAmount : web3.utils.hexToNumber(result[1][i]),
          wattSaving : web3.utils.hexToNumber(result[2][i])
        }
        bidArr.push(bidObj);
      }
      bidArr = bidArr.sort((bid1, bid2) => {
        let costPerSavingBid1 = bid1.bidAmount / bid1.wattSaving;
        let costPerSavingBid2 = bid2.bidAmount / bid2.wattSaving;
        if(costPerSavingBid1 === costPerSavingBid2){
          return 0;
        }else return costPerSavingBid1 > costPerSavingBid2 ? 1 : -1;
      });
      
      let totalIncentivePayout = 0, bidIdArr = [];
      //select top n bidders where the total incentive payout == sum of the top n bidder's bid amount  
      for (let i = 0; i<bidArr.length; i++){
        if (totalIncentivePayout + bidArr[i].bidAmount > maxIncentive) break;
        totalIncentivePayout += bidArr[i].bidAmount;
        bidIdArr.push(web3.utils.padRight(web3.utils.utf8ToHex(bidArr[i].bidId),64));
      }
      
      
      //decide on the winners
      //let bidIdArr = bidArr.map(obj => web3.utils.padRight(web3.utils.utf8ToHex(obj.bidId),64));

      //SC-CALL - registerWinningBids

    const registerWinningBidsCall = eaContract.methods.registerWinningBids(auctionIdHex, bidIdArr).send({
      from: config.userAccounts.ngo,
      gasPrice: "200",
      gas: "999999999"
    }, (err,txHash)=>{
      if(!err) resolve(txHash);
      else reject(err);
    });
      console.log(bidArr);
    }else {reject("Some error occured :"+result)}
      });

        }
      }
    });

  });
}


/**
 * This can only be done by NGO
 *
 * body Auction 
 * no response value expected for this operation
 **/
exports.closeAuctionPledge = function(body) {
  return new Promise(function(resolve, reject) {
    
    //TODO
    const auctionIdHex = web3.utils.padRight(web3.utils.utf8ToHex(body.auctionId),64);

    //fetch the list of users and their devices participated in the auction
    
    const getParticipatingDeviceCall = eaContract.methods.getParticipatingDevicesInAuctionPledge(auctionIdHex).call({  
      from: config.userAccounts.ngo,
      gasPrice: "200",
      gas: "999999999"
    }).then((result)=> {

      console.log(result);
      if (result && typeof result === 'object' && Object.keys(result).length === 4){
         let participatingDeviceIds = [];
         let participatingDeviceAndBidsObjArr = [];
         for (let i=0; i<result[0].length;i++){
           let obj = {
            deviceId : web3.utils.hexToUtf8(result[0][i]),
            bidId : web3.utils.hexToUtf8(result[1][i]),
            offStartTimestamp : web3.utils.hexToNumber(result[2][i]),
            offEndTimestamp : web3.utils.hexToNumber(result[3][i])
           }
           participatingDeviceIds.push(result[0][i]);
           participatingDeviceAndBidsObjArr.push(obj);
         }       
        // for each device filter the number of ticks >= tickThreshold/hour, and sum of each device watt <= wattThreshold/hour
        eaContract.getPastEvents('DeviceUsageRegistered',{
          filter: {_deviceId: participatingDeviceIds}, // Using an array means OR: e.g. 20 or 23
          fromBlock: 0,
          toBlock: 'latest'
      },(err,events) => {
        if (err) reject(err);

        console.log(events); // same results as the optional callback above
        let deviceUsages = convertUsageEventsToObject(events);
        if (deviceUsages){
          let qualifiedBidsAndUsages = classifyAndFilterDeviceUsages(deviceUsages,participatingDeviceAndBidsObjArr,0);
          console.log(qualifiedBidsAndUsages);

          const incentivisePledgeKeepersCall = eaContract.methods
          .incentivisePledgeKeepers(auctionIdHex, 
            qualifiedBidsAndUsages[0], 
            qualifiedBidsAndUsages[1]).send({

            from: config.userAccounts.ngo,
            gasPrice: "200",
            gas: "999999999"
          }, (err,txHash)=>{
            if(!err) resolve(txHash);
            else reject(err);
          });
        }
      });
      // .then((events) => {

      // });

      }else {reject("Some error occured while fetching participating device ids for pledge :"+result)}
    });

    //SC Call - getUser
    //get device id
    
    //Event call with the list of devices participated in the auction.

    // for each device filter the number of ticks >= tickThreshold/hour, and sum of each device watt <= wattThreshold/hour
    //get hexUsageIds
    //SC call - incentivisePledgeKeepers(auctionIdHex, hexBidIdArr, hexUsageIds)



  });
} 
//pass events[0].returnValues
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


let classifyAndFilterDeviceUsages = function (deviceUsageArr, bidArr, thresholdWatt) {
  let qualifiedBidMap = new Map();
  let qualifiedUsageMap = new Map();
  for (let i = 0; i < bidArr.length; i++) {

    let currentBidId = bidArr[i].bidId;
    qualifiedBidMap.set(currentBidId, true);
    qualifiedUsageMap.set(currentBidId, []);

    for (let j = 0; j < deviceUsageArr.length; j++){
      if (deviceUsageArr[j].deviceId === bidArr[i].deviceId 
         && deviceUsageArr[j].timestamp >= bidArr[i].offStartTimestamp
         && deviceUsageArr[j].timestamp <= bidArr[i].offEndTimestamp
        ){

          if (qualifiedBidMap.get(currentBidId)){
            if (deviceUsageArr[j].watt <= thresholdWatt){
              qualifiedUsageMap.get(currentBidId).push(deviceUsageArr[j].usageId);
            }else {
              qualifiedBidMap.set(currentBidId, false);
            }
          }
          // let bidIdHex = web3.utils.padRight(web3.utils.utf8ToHex(bidArr[i].bidId),64);
          // let usageIdHex = web3.utils.padRight(web3.utils.utf8ToHex(deviceUsageArr[j].usageId),64);
          // qualifiedBidIds.add(bidIdHex);
          // qualifiedUsageIds.add(usageIdHex);
      }
    }
  }
  let qualifiedBidIds = [];
  let qualifiedUsageIds = [];
  qualifiedBidMap.forEach((value,key,map) => {
    if (value) {
      qualifiedBidIds.push(key);
      qualifiedUsageIds = qualifiedUsageIds.concat(qualifiedUsageMap.get(key));
    }
  });
  qualifiedBidIds = qualifiedBidIds.map(bidId => web3.utils.padRight(web3.utils.utf8ToHex(bidId),64));
  qualifiedUsageIds = qualifiedUsageIds.map(usageId => web3.utils.padRight(web3.utils.utf8ToHex(usageId),64));

  return [qualifiedBidIds, qualifiedUsageIds];
}

/**
 *
 * auctionId String  (optional)
 * returns List
 **/
exports.getAuction = function(auctionId) {
  return new Promise(function(resolve, reject) {

    const auctionIdHex = web3.utils.padRight(web3.utils.utf8ToHex(auctionId),64);
    const getAuctionCall = eaContract.methods.getAuction(auctionIdHex).call({
        
      from: config.userAccounts.ngo,
      gasPrice: "200",
      gas: "999999999"
    }).then((result)=> {
      console.log(result);
      if (result && typeof result === 'object' && Object.keys(result).length ==7){
        let auctionId = web3.utils.hexToUtf8(result[0]);
        if(auctionId){
          let auctionObject = {
            "auctionId": web3.utils.hexToUtf8(result[0]),
            "totalIncentive": web3.utils.hexToNumber(result[1]),
            "wattHourGoalSaving": web3.utils.hexToNumber(result[2]),
            "bidStartTimestamp": web3.utils.hexToNumber(result[3]),
            "bidEndTimestamp": web3.utils.hexToNumber(result[4]),
            "offStartTimestamp": web3.utils.hexToNumber(result[5]),
            "offEndTimestamp": web3.utils.hexToNumber(result[6])
          };
          resolve([auctionObject]);
        }else {resolve([])};
      }else {reject("Some error occured :"+result)}
    });
  });
}


/**
 *
 * auctionId String  (optional)
 * returns List
 **/
exports.getWinningBids = function(auctionId) {
  return new Promise(function(resolve, reject) {

    const auctionIdHex = web3.utils.padRight(web3.utils.utf8ToHex(auctionId),64);
    
    const getWinningBidsCall = eaContract.methods.getWinningBids(auctionIdHex).call({
      from: config.userAccounts.ngo,
      gasPrice: "200",
      gas: "999999999"
  }).then((result)=> {
    console.log(result);
    if (result && typeof result === 'object' && Object.keys(result).length == 4){
      let bidArr = [];

      //create the array of bid objects
      for (let i=0; i<result[0].length;i++){
        let bidObj = {
          bidId : web3.utils.hexToUtf8(result[0][i]),
          userId : web3.utils.hexToUtf8(result[1][i]),
          bidAmount : web3.utils.hexToNumber(result[2][i]),
          wattSaving : web3.utils.hexToNumber(result[3][i])
        }
        bidArr.push(bidObj);
      }
      resolve(bidArr);
    }
  });

  });
}

/**
 * Create bid
 *
 * body Bid 
 * no response value expected for this operation
 **/
exports.createBid = function(body) {
  return new Promise(function(resolve, reject) {
    
    const auctionId = web3.utils.padRight(web3.utils.utf8ToHex(body.auctionId),64);
    const bidId = web3.utils.padRight(web3.utils.utf8ToHex(body.bidId),64);
    const addresses = body.userId;
    const bidAmount = parseInt(body.bidAmount);
    const wattSaving = parseInt(body.wattSaving);
    const offStartTimestamp = parseInt(body.offStartTimestamp);
    const offEndTimestamp = parseInt(body.offEndTimestamp);

    const createBidCall = eaContract.methods.placeBid(auctionId, bidId, 
      bidAmount, offStartTimestamp, 
      offEndTimestamp, wattSaving).send({
      from: addresses,
      gasPrice: "200",
      gas: "999999999"
    }, (err,txHash)=>{
      if (err) reject(err);
      resolve(txHash)
    });


  });
}
exports.getBids = function(auctionId) {
  return new Promise(function(resolve, reject) {
    const auctionIdHex = web3.utils.padRight(web3.utils.utf8ToHex(auctionId),64);
    
    const getAuctionBidsCall = eaContract.methods.getAuctionBids(auctionIdHex).call({
      from: config.userAccounts.ngo,
      gasPrice: "200",
      gas: "999999999"
  }).then((result)=> {
    console.log(result);
    if (result && typeof result === 'object' && Object.keys(result).length ==3){
      let bidArr = [];

      //create the array of bid objects
      for (let i=0; i<result[0].length;i++){
        let bidObj = {
          bidId : web3.utils.hexToUtf8(result[0][i]),
          bidAmount : web3.utils.hexToNumber(result[1][i]),
          wattSaving : web3.utils.hexToNumber(result[2][i])
        }
        bidArr.push(bidObj);
      }
      resolve(bidArr);
    }
  });
});
}
