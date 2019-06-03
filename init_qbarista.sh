#!/bin/bash
echo "Installing the Quiz Barista:"
echo

echo "Initializing the Python environment:"
echo "python3 -m venv env"
python3 -m venv env

echo "Recreating the environment from requirements.txt:"
echo "pip install -r requirements.txt"
echo
source env/bin/activate
pip install -r requirements.txt
echo

echo "Adding a cronjob to automatically start the TCP server..."
path=$(pwd)
crontab -l > .currentcrontab
echo "@reboot $path/env/bin/python $path/startup.py" >> .currentcrontab
crontab .currentcrontab
rm .currentcrontab

echo "Done!"
