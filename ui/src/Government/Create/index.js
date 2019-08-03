import React, { useState } from 'react';

import Api from '../../Api';
import TopGradient from '../../Components/TopGradient';

import styles from './index.module.css';

const validate = (value, setValue, re) => {
  re.test(value) && setValue(value);
};

const floatTest = /^(\d+(\.\d*)?)?$/;
const toDateTime = (date, time) => (new Date(`${date}T${time}:00`)).getTime();

const Create = ({ setAuction }) => {
  const [payout, setPayoutRaw] = useState('');
  const [savings, setSavingsRaw] = useState('');
  const [startDate, setStartDate] = useState('');
  const [startTime, setStartTime] = useState('');
  const [endDate, setEndDate] = useState('');
  const [endTime, setEndTime] = useState('');

  const setPayout = v => validate(v, setPayoutRaw, floatTest);
  const setSavings = v => validate(v, setSavingsRaw, floatTest);

  const isValid = payout && savings && startDate && startTime && endDate && endTime;

  const onSubmit = e => {
    e.preventDefault();
    const start = toDateTime(startDate, startTime);
    const end = toDateTime(endDate, endTime);

    const data = {
      bidStartTimestamp: start,
      savingStartTimestamp: start,
      bidEndTimestamp: end,
      savingEndTimestamp: end,
      totalIncentive: parseFloat(payout),
      litreGoalSaving: parseFloat(savings),
      users: [],
      auctionId: '003',
    };

    setAuction(data);

    Api.Auction.create(data)
      .then(() => {
        setPayoutRaw('');
        setSavingsRaw('');
        setStartDate('');
        setStartTime('');
        setEndDate('');
        setEndTime('');
      });
  };

  return (
    <div className={`Container ${styles.Container}`}>
      <TopGradient from="#2c3e50" to="#2c3e50" />
      <h1 className={styles.Title}>Create Auction</h1>
      <form id={styles.Form} onSubmit={onSubmit}>
        <div className={styles.Input}>
          <label htmlFor="incentive">Total Incentive Payout:</label>
          <input
            id="incentive"
            type="text"
            placeholder="Total Incentive Payout"
            value={payout}
            onChange={e => setPayout(e.currentTarget.value)}
          />
        </div>
        <div className={styles.Input}>
          <label htmlFor="savings">Target Savings:</label>
          <input
            id="savings"
            type="text"
            placeholder="Target Savings"
            value={savings}
            onChange={e => setSavings(e.currentTarget.value)}
          />
        </div>
        <div className="row">
          <div className={styles.Input}>
            <label htmlFor="start-date">Start Time:</label>
            <div className="row">
              <input
                id="start-date"
                type="date"
                value={startDate}
                onChange={e => setStartDate(e.currentTarget.value)}
              />
              <input
                id="start"
                type="time"
                value={startTime}
                onChange={e => setStartTime(e.currentTarget.value)}
              />
            </div>
          </div>
          <div className={styles.Input}>
            <label htmlFor="end-date">End Time:</label>
            <div className="row">
              <input
                id="end-date"
                type="date"
                value={endDate}
                onChange={e => setEndDate(e.currentTarget.value)}
              />
              <input
                id="end"
                type="time"
                value={endTime}
                onChange={e => setEndTime(e.currentTarget.value)}
              />
            </div>
          </div>
        </div>
        <div id={styles.Submit}>
          <button type="submit" className="Button" disabled={!isValid}>
            Create Auction
          </button>
        </div>
      </form>
    </div>
  );
};

export default Create;
