#!/bin/bash
echo 'just type: agent.py'
docker-compose build
docker-compose run zabbix-mqtt-agent agent.py
