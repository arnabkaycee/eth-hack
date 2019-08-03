'use strict';


/**
 *
 * deviceId String  (optional)
 * returns List
 **/
exports.getDeviceUsage = function(deviceId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "usageId" : "usageId",
  "deviceId" : "deviceId",
  "watt" : 0,
  "timestamp" : 0
}, {
  "usageId" : "usageId",
  "deviceId" : "deviceId",
  "watt" : 80,
  "timestamp" : 0
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * logUsageStats
 * This can only be done by NGO
 *
 * body Body 
 * no response value expected for this operation
 **/
exports.logUsageStats = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}

