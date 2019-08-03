'use strict';


/**
 * Create user
 * This can only be done by NGO.
 *
 * body User Created user object
 * no response value expected for this operation
 **/
exports.createUser = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 *
 * userId String  (optional)
 * returns List
 **/
exports.getUsers = function(userId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "address" : "address",
  "walletBalance" : 6,
  "userType" : 0,
  "userId" : "userId",
  "deviceId" : "deviceId"
}, {
  "address" : "address",
  "walletBalance" : 6,
  "userType" : 0,
  "userId" : "userId",
  "deviceId" : "deviceId"
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

