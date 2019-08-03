import React, { useState } from 'react';

import Notifications from './Notifications';
import Usage from './Usage';
import Pledge from './Pledge';
import styles from './index.module.css';

const User = ({ user, setAuctionWon, auction, auctionWon }) => {
  const [auctionSelected, setAuctionSelected] = useState('');
  const [pledgePlaced, setPledgePlaced] = useState({});

  return (
    <main id={styles.User}>
      <Notifications
        auctionSelected={auctionSelected}
        setAuctionSelected={setAuctionSelected}
        pledgePlaced={pledgePlaced}
        setAuctionWon={setAuctionWon}
        auction={auction}
      />
      <Usage
        deviceId={user && user.deviceId}
        pledgePlaced={pledgePlaced}
        auctionWon={auctionWon}
      />
      <Pledge
        auctionSelected={auctionSelected}
        setAuctionSelected={setAuctionSelected}
        setPledgePlaced={setPledgePlaced}
      />
    </main>
  );
};

export default User;
