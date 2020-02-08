#!/bin/bash

echo "Installing DailyWiki"

cwd=$(pwd)
cd ~

mkdir DailyWiki

cp -avr $"cwd"/conf DailyWiki
cp -avr $"cwd"/imageformats DailyWiki
cp -avr $"cwd"/lib DailyWiki
cp -avr $"cwd"/logs DailyWiki
cp -avr $"cwd"/platforms DailyWiki
cp -avr $"cwd"/resources DailyWiki
cp -avr $"cwd"/src DailyWiki
cp $"cwd"/main DailyWiki
cp $"cwd"/README.txt DailyWiki

crontab -e @reboot /DailyWiki/main









