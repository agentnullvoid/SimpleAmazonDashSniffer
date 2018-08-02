#!/usr/bin/python

from scapy.all import *
import requests
import time

PKT_TIME_DIFF = 60

def methodA():
    print "Do something A"

def methodB():
    print "Do something B"

def methodC():
    print "Do something C"

dash_buttons = {"macA": {"name": "DashA", "func": methodA},
                "macB": {"name": "DashB", "func": methodB},
                "macC": {"name": "DashC", "func": methodC}}

dash_times = dict()

def arp_sniffer(pkt):
    if pkt.haslayer(ARP):
        if pkt[ARP].op == 1:
            mac = pkt[ARP].hwsrc
            if mac in dash_buttons.keys():
                if mac in dash_times.keys():
                    prev_time = dash_times[mac]
                    if (time.time() - prev_time) >= PKT_TIME_DIFF:
                        dash_buttons[mac]["func"]()
                        dash_times[mac] = time.time()
                else:
                    dash_buttons[mac]["func"]()
                    dash_times[mac] = time.time()

print "Starting sniffer..."
sniff(prn=arp_sniffer, filter="arp", store=0, count=0)
