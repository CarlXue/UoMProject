#!/bin/sh

echo "open Chrome"
/usr/bin/open -a "/Applications/Google Chrome.app" 'http://localhost:3000'
echo "Start"
pwd
cd /
pwd
cd /Users/junyiliu/Documents/Song\ Xue/UoMProject/Storing\ System/
pwd
echo "Run server"
rails server
