export default {
  base: 'http://localhost:8080/v1',
  Auction: {
    base: '/auction',
    create: {
      base: '',
      method: 'POST',
    },
    getAll: {
      base: '',
      method: 'GET',
    },
    getTopRanked: {
      base: '/bid/wins',
      method: 'GET',
    }
  },
  User: {
    base: '/user',
    getInfo: {
      base: '',
      method: 'GET',
    },
  },
  Devices: {
    base: '/device',
    getUsage: {
      base: '/usage',
      method: 'GET',
    },
  },
  Notifications: {
    base: '/notification',
    getLast: {
      base: '',
      method: 'GET',
    },
  },
};
