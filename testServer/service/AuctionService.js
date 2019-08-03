'use strict';


/**
 * This can only be done by NGO
 *
 * body Auction
 * no response value expected for this operation
 **/
exports.closeAuction = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
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
    resolve();
  });
}


/**
 * Create auction
 * This can only be done by NGO
 *
 * body Auction
 * no response value expected for this operation
 **/
exports.createAuction = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
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
    resolve();
  });
}


/**
 *
 * auctionId String  (optional)
 * returns List
 **/
exports.getAuction = function(auctionId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
      "auctionId" : "001",
      "bidStartTimestamp" : 1564851175980,
      "savingEndTimestamp" : 1565851262380,
      "totalIncentive" : 500,
      "litreGoalSaving" : 6000000,
      "savingStartTimestamp" : 1564851175980,
      "users" : [ "users", "users" ],
      "bidEndTimestamp" : 1565851262380
    }, {
      "auctionId" : "002",
      "bidStartTimestamp" : 1,
      "savingEndTimestamp" : 2,
      "totalIncentive" : 1000,
      "litreGoalSaving" : 8000000,
      "savingStartTimestamp" : 5,
      "users" : [ "users", "users" ],
      "bidEndTimestamp" : 5
    } ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 *
 * auctionId String  (optional)
 * returns List
 **/
exports.getBids = function(auctionId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
      "auctionId" : "auctionId",
      "bidAmount" : 0,
      "litreSaving" : 6,
      "userId" : "userId",
      "bidId" : "bidId"
    }, {
      "auctionId" : "auctionId",
      "bidAmount" : 0,
      "litreSaving" : 6,
      "userId" : "userId",
      "bidId" : "bidId"
    } ];
    console.log(auctionId);
    console.log(examples[Object.keys(examples)[0]].filter(v => v.auctionId === auctionId));
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]].filter(v => v.auctionId === auctionId));
    } else {
      resolve();
    }
  });
}


/**
 *
 * auctionId String  (optional)
 * returns List
 **/
exports.getWinningBids = function(auctionId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
      "auctionId" : "001",
      "bidAmount" : 10,
      "litreSaving" : 20,
      "userId" : "user001",
      "bidId" : "bid-76"
    }, {
      "auctionId" : "002",
      "bidAmount" : 5,
      "litreSaving" : 50,
      "userId" : "user007",
      "bidId" : "bid-28"
    }, {
      "auctionId" : "002",
      "bidAmount" : 6,
      "litreSaving" : 45,
      "userId" : "user011",
      "bidId" : "bid-65"
    }, {
      "auctionId" : "002",
      "bidAmount" : 8,
      "litreSaving" : 40,
      "userId" : "user013",
      "bidId" : "bid-43"
    }, {
      "auctionId" : "002",
      "bidAmount" : 20,
      "litreSaving" : 70,
      "userId" : "user020",
      "bidId" : "bid-10"
    }, {
      "auctionId" : "002",
      "bidAmount" : 25,
      "litreSaving" : 100,
      "userId" : "user004",
      "bidId" : "bid-1"
    }, {
      "auctionId" : "002",
      "bidAmount" : 30,
      "litreSaving" : 100,
      "userId" : "user100",
      "bidId" : "bid-7"
    } ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]].filter(v => v.auctionId === auctionId));
    } else {
      resolve();
    }
  });
}

