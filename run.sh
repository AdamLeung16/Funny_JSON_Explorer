#!/bin/bash
export PATH="$PATH:/home/adamleung/桌面/softwareProject/Funny_JSON_Explorer/src"
source ~/.bashrc
fje -f test/test.json -s tree -i poker
fje -f test/test.json -s tree -i chess
fje -f test/test.json -s rectangle -i poker
fje -f test/test.json -s rectangle -i chess
fje -f test/test.json -s tree -i music -c config/icon.json