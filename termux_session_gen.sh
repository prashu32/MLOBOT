#!/bin/bash
clear
echo "
    ¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯
 ¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯

"
# Termux session string generator for MloBot
echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/prashu32/MloBot/master/resources/mlobot-setup.py
pip install telethon
python mlobot-setup.py
