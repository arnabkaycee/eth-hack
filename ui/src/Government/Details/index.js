import React, { useState, useEffect } from 'react';

import Api from '../../Api';
import TopGradient from '../../Components/TopGradient';

import styles from './index.module.css';

const Details = ({ auctionSelected }) => {
  const [topRanked, setTopRanked] = useState([]);

  useEffect(() => {
    if (auctionSelected !== '') {
      Api.Auction.getTopRanked({ auctionId: auctionSelected })
        .then(r => setTopRanked(r));
    }
  }, [auctionSelected]);

  return (
    <div className={`Container ${styles.Container}`}>
      <TopGradient from="#2c3e50" to="#2c3e50" />
      <h1>Top Rankers</h1>
      <div id={styles.Details}>
        <div id={styles.ListHeader}>
          <div><span>User Id</span></div>
          <div><span>Bid Id</span></div>
          <div><span>Bid Amount</span></div>
          <div><span>Litre Saving</span></div>
        </div>
        <div id={styles.BidList}>
          { topRanked.map((t, i) =>
            <div
              key={i}
              className={styles.Bid}
            >
              <div><span>{t.userId}</span></div>
              <div><span>{t.bidId}</span></div>
              <div><span>{t.bidAmount}</span></div>
              <div><span>{t.litreSaving}</span></div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Details;
