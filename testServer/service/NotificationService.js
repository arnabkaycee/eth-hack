'use strict';


/**
 *
 * sequenceId String exact sequence id, fetches only one result (optional)
 * offsetSequenceId String fetch the results where `sequenceId` >= `offsetSequenceId` (optional)
 * limit Integer limit the number of results starting from the offset starting with the sequence id denoted by `offsetSequenceId` (optional)
 * returns List
 **/
exports.getNotification = function(sequenceId,offsetSequenceId,limit) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [
      {
        "detail" : "Walled Credited $20",
        "sequenceId" : 4
      }, {
        "detail" : "Kept pledge",
        "sequenceId" : 3
      }, {
        "detail" : "Won Auction",
        "sequenceId" : 2
      }, {
        "detail" : "Pledged for 25L and $20",
        "sequenceId" : 1
      }, {
        "detail" : "Auction opened for $500 and 250L",
        "sequenceId" : 0
      }
    ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

