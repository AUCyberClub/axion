#!/bin/bash

clear

echo " ____________________________________________ "
echo "|****WELCOME TO AUCC AXION INSTALLIATION*****|"
echo "|____________________________________________|"
echo ""
echo "Axion is a simple toolkit that contains useful tools and capable of control the I/Os of those tools to make it easier your life in CTFs."
echo ""
echo "This program is under GPL-3 LICENSE"
echo ""
echo "https://github.com/AUCyberClub/axion"
echo ""
echo "Axion uses or controls following tools or packages--->"
echo ""
echo "git          binwalk      exiftool"
echo "volatility   python-pip   python-pexpect"
echo "wget         zbar-tools   pdf-parser"
echo "john-jumbo"
echo ""
echo "Axion uses following external python libraries--->"
echo ""
echo "setuptools colorama hashid pybase64"
echo ""
echo "_______________________________________________________"
echo ""
echo "Choose a language to continue the installation"
echo ""
echo "'T' for Turkish and 'E' for English --->"

read lang

if [ "$lang" = "E" ]; then
    git clone https://github.com/AUCyberClub/axion.git
elif [ "$lang" = "T" ]; then
    git clone https://github.com/AUCyberClub/axion-tr axion
else
    echo "Wrong input !!"
    exit 1
fi

sudo apt-get install git binwalk exiftool volatility python-pip python-pexpect wget zbar-tools
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
