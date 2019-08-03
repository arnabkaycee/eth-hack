import React, { useState } from 'react';

import List from './List';
import Details from './Details';
import Create from './Create';
import styles from './index.module.css';

const Government = ({ auction, setAuction }) => {
  const [auctionSelected, setAuctionSelected] = useState('');

  return (
    <main id={styles.Government}>
      <List
        auctionSelected={auctionSelected}
        setAuctionSelected={setAuctionSelected}
        auction={auction}
      />
      <Details
        auctionSelected={auctionSelected}
      />
      <Create
        setAuction={setAuction}
      />
    </main>
  );
};

export default Government;
