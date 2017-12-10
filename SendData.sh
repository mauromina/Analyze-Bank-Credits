#!/bin/bash
clear
echo "sending training data"
curl -X GET -H "X-API-TOKEN: FOOBAR1" -H "Content-Type: application/json; charset=utf-8" http://127.0.0.1:5000/train -d '{"data-url": "sample-data.csv"}'
