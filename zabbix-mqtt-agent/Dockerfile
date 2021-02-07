FROM ubuntu:20.04
RUN apt update && apt install -y zabbix-agent python3-pip
ADD requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
ADD zabbix_agentd.conf /etc/zabbix
COPY agent.py /usr/local/bin
RUN chmod a+x /usr/local/bin/agent.py
CMD /usr/local/bin/agent.py
