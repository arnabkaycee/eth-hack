import React, { useState, useEffect } from 'react';

import Api from '../../Api';
import TopGradient from '../../Components/TopGradient';

import styles from './index.module.css';

const Usage = ({ deviceId, pledgePlaced, auctionWon }) => {
  const [usages, setUsages] = useState([]);

  useEffect(() => {
    if (deviceId) {
      Api.Devices.getUsage()
        .then(setUsages)
    }
  }, [deviceId]);

  const todaySavings = usages.length ? usages[0].watt : 0;
  const weekSavings = usages.reduce((acc, v) => acc + v.watt, 0);

  return (
    <div className={`Container ${styles.Container}`}>
      <TopGradient from="#2c3e50" to="#2c3e50" />
      <h1>Water Usage Savings</h1>
      <div id={styles.Usage}>
        <div className={styles.Column}>
          <span>{parseInt(todaySavings) + (auctionWon ? parseInt(pledgePlaced.litres) : 0)} L</span>
          <h3>Today</h3>
        </div>
        <div className={styles.Column}>
          <span>{parseInt(weekSavings) + (auctionWon ? parseInt(pledgePlaced.litres) : 0)} L</span>
          <h3>Week</h3>
        </div>
        <div className={styles.Column}>
          <span>50%</span>
          <h4 className={styles.less}>Less than yesterday</h4>
        </div>
        <div className={styles.Column}>
          <span>20%</span>
          <h4 className={styles.more}>More than last week</h4>
        </div>
      </div>
    </div>
  );
};

export default Usage;
