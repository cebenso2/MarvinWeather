#!/bin/bash
NOW=$(date +"%D-%T: ")
printf "$NOW" >> /home/pi/marvin/weather/log.txt
/usr/bin/python3 /home/pi/marvin/weather/main.py >> /home/pi/marvin/weather/log.txt
