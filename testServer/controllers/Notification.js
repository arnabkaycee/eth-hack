'use strict';

var utils = require('../utils/writer.js');
var Notification = require('../service/NotificationService');

module.exports.getNotification = function getNotification (req, res, next) {
  var sequenceId = req.swagger.params['sequenceId'].value;
  var offsetSequenceId = req.swagger.params['offsetSequenceId'].value;
  var limit = req.swagger.params['limit'].value;
  Notification.getNotification(sequenceId,offsetSequenceId,limit)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
