#!/usr/bin/env bash
BASE_DIR='/home/pi/bcx19-shakti';
echo "Cleaning up previous temporary files ..."
cd ${BASE_DIR} && rm -fr build
tmux kill-session -t ganache
tmux kill-session -t node
echo "Starting Ethereum service ..."
cd ${BASE_DIR} && tmux new-session -d -s ganache 'ganache-cli -d -l 999999999 -m "between vacant meadow invest minute tenant mobile front spring hungry globe inspire"'
echo "Waiting Ethereum service to start ..."
sleep 30
echo "Deploying Smart Contract ..."
cd ${BASE_DIR} && truffle migrate --reset
sleep 10
echo "Starting dApp Server ..."
cd ${BASE_DIR} && tmux new-session -d -s node 'node index.js'
echo "dApp Server started ..."
echo "======================================"
echo "Initial Setup Complete"
echo "======================================"
#echo "Execute 'python3 BCX_Demo.py' ..."
#cd ${BASE_DIR}/agents
read -p "Do you want to start Demo? (y/n) " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    cd ${BASE_DIR}/agents && python3 BCX_Demo.py
fi