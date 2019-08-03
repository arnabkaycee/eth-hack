import Config from './config';

function getUrl(model, method) {
  return [
    Config[model][method].method,
    `${Config.base}${Config[model].base}${Config[model][method].base}`
  ];
}

function request(model, apiMethod, data='') {
  const [method, url] = getUrl(model, apiMethod);
  if (method === 'POST') {
    return fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
  } else if (method === 'GET') {
    let query = [];
    if (data) {
      for (const key in data) {
        query.push(`${key}=${data[key]}`);
      }
    }
    return fetch(`${url}${query ? '?' + query.join('&') : ''}`);
  }
}

const Auction = {
  create: async function(data) {
    return await request('Auction', 'create', data);
  },
  getAll: async function() {
    const response = await request('Auction', 'getAll');
    return await response.json();
  },
  getTopRanked: async function(data) {
    const response =  await request('Auction', 'getTopRanked', data);
    return await response.json();
  },
};

const User = {
  getInfo: async function(data) {
    const response = await request('User', 'getInfo', data)
    return await response.json();
  },
};

const Devices = {
  getUsage: async function(data) {
    const response = await request('Devices', 'getUsage', data)
    return await response.json();
  },
};

const Notifications = {
  getLast: async function(data) {
    const response = await request('Notifications', 'getLast', data)
    return await response.json();
  },
};

const Api = {
  Auction,
  User,
  Devices,
  Notifications,
};

export default Api;
