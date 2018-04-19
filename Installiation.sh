#!/bin/bash

sudo apt-get install git binwalk exiftool volatility python-pip
git clone https://github.com/AUCyberClub/axion.git
cd axion
sudo pip install -r requirements.txt
path=$(pwd | grep axion)
echo "#!/bin/bash" >> axion
echo "cd $path" >> axion
echo "python $path/axion.py" >> axion
sudo chmod +x axion
sudo mv axion /usr/bin
