#!/usr/bin/python
from RosAPI import Core
from sys import argv

try:
    a = Core(argv[1])
except:
    print("No connection")
a.login("bgpmonlogin", "bgpmonpass")
peers = a.response_handler(a.talk(["/routing/bgp/peer/print"]))
peers_dict = {}
if len(peers) > 0:
    for peer in peers:
        # print("{} {} {}".format(peer['remote-address'], peer['remote-as'], peer['established']))
        peers_dict[peer['remote-address']] = peer['established']

if argv[2] in peers_dict:
    if peers_dict[argv[2]] == 'true':
        print(1)
    else:
        print(0)
else:
    print(0)
