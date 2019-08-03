import React, { useState, useEffect, useRef } from 'react';

import Api from '../../Api';
import TopGradient from '../../Components/TopGradient';

import styles from './index.module.css';

const now = () => {
  return (new Date()).toLocaleString();
};

const Notifications = ({ auction, setAuctionSelected, pledgePlaced, setAuctionWon }) => {
  const [notifications, setNotifications] = useState([]);
  const [allNotifications, setAllNotifications] = useState([]);
  const notificationsRef = useRef(notifications);
  const allNotificationsRef = useRef(allNotifications);
  notificationsRef.current = notifications;
  allNotificationsRef.current = allNotifications;

  const [startTimer, setStartTimer] = useState(false);

  useEffect(() => {
    const getNotifications = async () => {
      const lastNotifications = await Api.Notifications.getLast({ offsetSequenceId: 0 });
      const n = lastNotifications.pop();
      setAllNotifications(lastNotifications);
      setNotifications([ { ...n, detail: `Auction opened for $${auction.totalIncentive || 500} and ${auction.litreGoalSaving || 250}L`, timestamp: now() } ]);
    };
    getNotifications();
  }, []);

  useEffect(() => {
    let newAllNotifications = [...allNotificationsRef.current];
    const notification = newAllNotifications.pop();
    setAllNotifications(newAllNotifications);
    setNotifications([ { ...notification, detail: `Pledged for $${pledgePlaced.incentiveAsked} and ${pledgePlaced.litres}L`, timestamp: now() }, ...notificationsRef.current ]);
    setStartTimer(!startTimer);
  }, [pledgePlaced]);

  useEffect(() => {
    if (pledgePlaced.litres === undefined) return;
    const getNotifications = () => {
      if (allNotifications.length) {
        let newAllNotifications = [...allNotificationsRef.current];
        const notification = newAllNotifications.pop();
        setAllNotifications(newAllNotifications);
        if (notification.sequenceId === 4) {
          setNotifications([ { ...notification, detail: `Walled Credited: $${pledgePlaced.incentiveAsked}`, timestamp: now() } , ...notificationsRef.current ]);
          setAuctionWon(pledgePlaced.incentiveAsked);
        } else {
          setNotifications([ { ...notification, timestamp: now() } , ...notificationsRef.current ]);
        }

        setStartTimer(!startTimer);
      }
    };
    const timeout = setTimeout(getNotifications, 5000);
    return () => window.clearTimeout(timeout);
  }, [startTimer]);

  return (
    <div className={`Container ${styles.Container}`}>
      <TopGradient from="#2c3e50" to="#2c3e50" />
      <h1>Notifications</h1>
      <div id={styles.Notifications}>
        { notifications.map((n, i) =>
          <div key={i} className={styles.Notification}>
            <div className={styles.Left}></div>
            <div className={styles.Detail}>
              <div className={styles.Timestamp}>
                <span>{n.timestamp}</span>
              </div>
              <div className={styles.Message}>
                <span>{n.detail}</span>
              </div>
              { n.sequenceId === 0 && pledgePlaced.litres === undefined &&
                <div className={styles.Actions}>
                  <button
                    type="button"
                    className="Button"
                    onClick={() => setAuctionSelected('auctionId')}
                  >
                    Place pledge
                  </button>
                </div>
              }
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Notifications;
