#!/bin/bash
pid=`ps -ef | grep run_api | grep -v grep | awk "{print $2}"`
if [[ $pid -gt 0 ]]
then
  kill -9 $pid
  echo "pid $pid has been killed"
fi

path="/home/woody/backend/flask_demo"
if [[ ! -d "$path" ]]
then
  cd /home/woody/backend
  git clone -b dev ssh://git@github.com:woody3/flask_demo.git
  cd ./flask_demo/
else
  cd /home/woody/backend/flask_demo
  git pull origin master
fi

nohup python run_api.py >> logs/log.log 2 > &1 &
echo "service publish success"
  
