#!/usr/bin/python
from RosAPI import Core
from sys import argv
import json

try:
    a = Core(argv[1])
except:
    print("No connection")

a.login("bgpmonlogin", "bgpmonpass")
peers = a.response_handler(a.talk(["/routing/bgp/peer/print"]))
out = {'data': []}
if len(peers) > 0:
    for peer in peers:
        out['data'].append({"{#BGPPEER}": peer['remote-address']})

print(json.dumps(out, indent=4, sort_keys=True))
