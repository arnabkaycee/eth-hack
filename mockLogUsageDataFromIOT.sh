#!/usr/bin/env bash

echo 'Mocking Data from Device 1 from User 1'


curl -X POST \
  http://localhost:8080/v1/device/usage \
  http://localhost:8080/v1/user \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "literConsumed": 0,
  "usageId": "usg001",
  "userId": "0x9aeC04AEa530111F337f3D121488f22383098627"
}'

echo ''

echo 'Mocking Data from Device 2 from User 2'
curl -X POST \
  http://localhost:8080/v1/device/usage \
  http://localhost:8080/v1/user \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "literConsumed": 0,
  "usageId": "usg002",
  "userId": "0x263a5223a294C64b5E48Cab164e95131938C87ea"
}'
