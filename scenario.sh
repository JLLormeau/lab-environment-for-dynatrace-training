#!/bin/bash

echo "step 1 start"
sh remote-start-stop-easytravel.sh restart 2>&1

echo "sleep 2m"
sleep 2m

echo "sleep issue"
sh remote-start-stop-easytravel.sh issue 2>&1

echo "sleep 5m"
sleep 5m

echo "sleep restart"
sh remote-start-stop-easytravel.sh restart 2>&1

echo "sleep 5m"
sleep 5m

echo "sleep restartmongo"
sh remote-start-stop-easytravel.sh restartmongo 2>&1

echo "sleep 5m"
sleep 5m

echo "sleep restart"
sh remote-start-stop-easytravel.sh restart 2>&1
