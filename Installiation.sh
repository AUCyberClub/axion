#!/bin/bash

sudo apt-get install git binwalk exiftool volatility python-pip
git clone https://github.com/AUCyberClub/axion.git
cd axion
sudo pip install -r requirements.txt