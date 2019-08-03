'use strict';

var utils = require('../utils/writer.js');
var Auction = require('../service/AuctionService');

module.exports.closeAuction = function closeAuction (req, res, next) {
  var body = req.swagger.params['body'].value;
  Auction.closeAuction(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.closeAuctionPledge = function closeAuctionPledge (req, res, next) {
  var body = req.swagger.params['body'].value;
  Auction.closeAuctionPledge(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.createAuction = function createAuction (req, res, next) {
  var body = req.swagger.params['body'].value;
  Auction.createAuction(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.createBid = function createBid (req, res, next) {
  var body = req.swagger.params['body'].value;
  Auction.createBid(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getAuction = function getAuction (req, res, next) {
  var auctionId = req.swagger.params['auctionId'].value;
  Auction.getAuction(auctionId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getBids = function getBids (req, res, next) {
  var auctionId = req.swagger.params['auctionId'].value;
  Auction.getBids(auctionId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getWinningBids = function getWinningBids (req, res, next) {
  var auctionId = req.swagger.params['auctionId'].value;
  Auction.getWinningBids(auctionId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
