import React, { useState, createRef, useEffect } from 'react';

import TopGradient from '../../Components/TopGradient';

import styles from './index.module.css';

const validate = (value, setValue, re) => {
  re.test(value) && setValue(value);
};

const floatTest = /^(\d+(\.\d*)?)?$/;

const Pledge = ({ auctionSelected, setAuctionSelected, setPledgePlaced }) => {
  const [litres, setLitresRaw] = useState('');
  const [incentiveAsked, setIncentiveAskedRaw] = useState('');

  const litresInput = createRef(null);

  const setLitres = v => validate(v, setLitresRaw, floatTest);
  const setIncentiveAsked = v => validate(v, setIncentiveAskedRaw, floatTest);

  const isValid = litres && incentiveAsked;

  const onSubmit = e => {
    e.preventDefault();
    setPledgePlaced({
      litres,
      incentiveAsked,
    });
    setAuctionSelected('');
  };

  useEffect(() => {
    if (auctionSelected) {
      litresInput.current.focus();
    }
  }, [auctionSelected]);

  return (
    <div className={`Container ${styles.Container}`}>
      <TopGradient from="#2c3e50" to="#2c3e50" />
      <h1>Pledge</h1>
      { auctionSelected ? (
        <form id={styles.Form} onSubmit={onSubmit}>
          <div className={styles.Input}>
            <label htmlFor="litres">Litres:</label>
            <input
              id="litres"
              type="text"
              ref={litresInput}
              placeholder="Litres"
              value={litres}
              onChange={e => setLitres(e.currentTarget.value)}
            />
          </div>
          <div className={styles.Input}>
            <label htmlFor="incentiveAsked">Incentive Asked:</label>
            <input
              id="incentiveAsked"
              type="text"
              placeholder="Incentive Asked"
              value={incentiveAsked}
              onChange={e => setIncentiveAsked(e.currentTarget.value)}
            />
          </div>
          <div id={styles.Submit}>
            <button type="submit" className="Button" disabled={!isValid}>
              Pledge
            </button>
          </div>
        </form>
      ) : null }
    </div>
  );
};

export default Pledge;
