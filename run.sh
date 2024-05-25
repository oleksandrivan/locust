#!/bin/sh

input=$1

if [ "$input" = "legacy-load" ]; then
    locust --users 100 --spawn-rate 10 --run-time 3m --html legacy-test.html --headless -f locustfile.py
elif [ "$input" = "proxy-load" ]; then
    locust --users 100 --spawn-rate 10 --run-time 3m --html proxy-test.html --headless -f locustfile-proxy.py
else
    echo "Invalid command" 
fi
