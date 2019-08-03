'use strict';

var utils = require('../utils/writer.js');
var Device = require('../service/DeviceService');

module.exports.getDeviceUsage = function getDeviceUsage (req, res, next) {
  var deviceId = req.swagger.params['deviceId'].value;
  Device.getDeviceUsage(deviceId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.logUsageStats = function logUsageStats (req, res, next) {
  var body = req.swagger.params['body'].value;
  Device.logUsageStats(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
