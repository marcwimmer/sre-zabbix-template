#!/usr/bin/env python3
import time
from pyzabbix import ZabbixMetric, ZabbixSender
import os
import sys
import subprocess
from pyzabbix.api import ZabbixAPI
host = os.getenv("ZBX_HOSTNAME")

hostname = 'e753f873-ddee-4e25-89ce-c80b29476e38'
key = 'mykey1'


# Send metrics to zabbix trapper
packet = [
    ZabbixMetric(hostname, key, 2),
]

result = ZabbixSender(use_config=True).send(packet)
print(result)

sys.exit(0)
