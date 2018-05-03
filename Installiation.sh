#!/bin/bash

sudo apt-get install git binwalk exiftool volatility python-pip python-pexpect wget zbar-tools
git clone https://github.com/AUCyberClub/axion.git
cd axion
sudo pip install -r requirements.txt
path=$(pwd | grep axion)
echo "#!/bin/bash" >> axion
echo "cd $path" >> axion
echo "python2 $path/axion.py" >> axion
sudo chmod +x axion
sudo mv axion /usr/bin

#John Jumbo Donwloader
wget http://download.openwall.net/pub/projects/john/contrib/linux/john-1.7.9-jumbo-5-Linux-x86-64.tar.gz
tar -xvf john-1.7.9-jumbo-5-Linux-x86-64.tar.gz
mv john-1.7.9-jumbo-5-Linux-x86-64/run ./john_files
chmod +x john_files/*
rm -rf john-1.7.9-jumbo*
