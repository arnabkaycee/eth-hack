const WaterAuction = artifacts.require("WaterAuction");
const path = require('path');
const config = require("../config/config.json");
const fs = require('fs');

module.exports = function(deployer, network, accounts) {
  // deployer.deploy(ConvertLib);
  // deployer.link(ConvertLib, MetaCoin);
  // deployer.deploy(MetaCoin);
  deployer.deploy(WaterAuction).then(() => {
    return deployer.deploy(WaterAuction);
  }).then(() => {
    config.app.waterAuction = WaterAuction.address;
    config.userAccounts.ngo = accounts[0];
    let configFilePath = path.resolve('./config/config.json');
    return fs.writeFile(configFilePath, JSON.stringify(config, null, 2), (err) => {
      console.log("configuration updated", err);
    });
  });
};
