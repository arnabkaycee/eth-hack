import React, { useState, useEffect } from 'react';

import Api from '../../Api';
import TopGradient from '../../Components/TopGradient';

import styles from './index.module.css';

const inBetween = (start, end) => {
  const now = (new Date()).getTime();
  if (now < start) return -1;
  if (now > end) return 1;
  return 0;
};

const getStatus = (status) => {
  if (status === -1) return 'Not yet started';
  if (status === 0) return 'Ongoing';
  return 'Ended';
};

const getClassName = (status) => {
  if (status === -1) return styles.future;
  if (status === 0) return styles.present;
  return styles.past;
};

const List = ({ auctionSelected, setAuctionSelected, auction }) => {
  const [auctions, setAuctions] = useState([]);

  useEffect(() => {
    Api.Auction.getAll()
      .then(r => setAuctions(r));
  }, []);

  return (
    <div className={`Container ${styles.Container}`}>
      <TopGradient from="#2c3e50" to="#2c3e50" />
      <h1 className={styles.Title}>Created Auctions</h1>
      <div id={styles.Auctions}>
        <div id={styles.AuctionHeader}>
          <div>Id</div>
          <div>Details</div>
          <div>Incentive Payout</div>
          <div>Litre Goal Saving</div>
          <div>Status</div>
        </div>
        { ( auction.auctionId !== undefined ? [ ...auctions, auction ] : auctions ).reverse().map((a, i) =>
          <div
            className={`${styles.Auction} ${auctionSelected === a.auctionId ? styles.selected : ''}`}
            key={i}
            onClick={() => setAuctionSelected(a.auctionId)}
          >
            <div><span className={styles.Id}>{a.auctionId}</span></div>
            <div><span className={styles.Details}>{a.details || 'details'}</span></div>
            <div><span className={styles.Incentive}>${a.totalIncentive}</span></div>
            <div><span className={styles.LitreGoal}>{a.litreGoalSaving}L</span></div>
            <div>
              <span className={`${styles.Status} ${getClassName(inBetween(a.bidStartTimestamp, a.bidEndTimestamp))}`}>
                {getStatus(inBetween(a.bidStartTimestamp, a.bidEndTimestamp))}
              </span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default List;
