import React, { useState, useEffect } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import Api from '../Api';
import Government from '../Government';
import User from '../User';

import styles from './index.module.css';

const getAuction = () => {
  const cached = sessionStorage.getItem('AUCTION');
  if (cached) {
    return JSON.parse(cached);
  }
  return {};
};

const saveAuction = (auction) => {
  sessionStorage.setItem('AUCTION', JSON.stringify(auction));
};

const Dashboard = () => {
  const [userInfo, setUserInfo] = useState([]);
  const [auctionWon, setAuctionWon] = useState(0);
  const [auction, setAuction] = useState(getAuction());

  useEffect(() => {
    Api.User.getInfo({ userId: '' })
      .then(setUserInfo);
  }, []);

  return (
    <div id={styles.Dashboard}>
      <header id={styles.Header}>
        <div id={styles.Logo}>
          <h1>Save Water</h1>
          <div id={styles.Droplet}></div>
        </div>
        <div id={styles.WalletInfo}>
          <h2>Wallet balance:</h2>
          <span>{userInfo.length ? parseInt(userInfo[0].walletBalance) + parseInt(auctionWon) : ''}</span>
        </div>
      </header>
      <BrowserRouter>
        <Switch>
          <Route path="/government">
            <Government setAuction={(auction) => { saveAuction(auction); setAuction(auction); }} auction={auction} />
          </Route>
          <Route path="/">
            <User user={userInfo && userInfo[0]} auctionWon={auctionWon} setAuctionWon={setAuctionWon} auction={auction} />
          </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
};

export default Dashboard;
