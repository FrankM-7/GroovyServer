#!/bin/bash

echo "Stopping the bot..."
pkill -f bot.py

echo "Starting new screen..."
screen -d -m bash -c 'cd /home/frank/Groovy; git pull; source env/bin/activate; python bot.py'

