#!/usr/bin/env bash

echo 'Creating Sponsor User'

curl -X POST \
  http://localhost:8080/v1/user \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "userId": "usr001",
  "address": "0x895aE9efB156e388Bd324e466576285906d20827",
  "userType": 0,
  "deviceId": "",
  "deviceType": 0
}'
echo ''

echo 'Creating Housing Complex User 1'

curl -X POST \
  http://localhost:8080/v1/user \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "userId": "usr002",
  "address": "0x9aeC04AEa530111F337f3D121488f22383098627",
  "userType": 1,
  "deviceId": "dev001",
  "deviceType": 0
}'
echo ''
echo 'Creating Housing Complex User 2'

curl -X POST \
  http://localhost:8080/v1/user \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "userId": "usr003",
  "address": "0x263a5223a294C64b5E48Cab164e95131938C87ea",
  "userType": 1,
  "deviceId": "dev002",
  "deviceType": 0
}'
echo ''
echo 'Creating Housing Complex User 3'

curl -X POST \
  http://localhost:8080/v1/user \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "userId": "usr004",
  "address": "0x628B31Bc31d04f425fb93209AFA332e893735184",
  "userType": 1,
  "deviceId": "dev003",
  "deviceType": 0
}'
echo ''
#curl -X POST \
#  http://localhost:8080/v1/auction/bid \
#  -H 'Accept: application/json' \
#  -H 'Content-Type: application/json' \
#  -d '{
#  "auctionId": "auction001",
#  "bidId" : "bid001",
#  "userId" : "0x9aeC04AEa530111F337f3D121488f22383098627",
#  "bidAmount":160,
#  "litreSaving" : 80
#}'
