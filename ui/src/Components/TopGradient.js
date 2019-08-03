import React from 'react';

const TopGradient = ({ from, to }) => {
  return (
    <div style={{
        width: '100%',
        background: `linear-gradient(to right, ${from}, ${to})`,
        height: '0.5rem',
      }}>
    </div>
  );
};

export default TopGradient;
