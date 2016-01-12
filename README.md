# Dillinger

This two scripts written for monitoring bgp sessions in zabbix. They by template discover every hour(by default) sessions, create items and triggers. 
Very simple at now, but i can't find that in internet. So... use if you want.

Import template to your zabbix instalation.

Place scripts in zabbix external scripts folder.

# Files

* bgpdiscovery.py - used for returning peers list to zabbix
* bgpmon.py - get bgp session state and return 0 or 1.
* RosAPI - RouterOS API library for python (thx David Jelić and Luka Blašković)

# Authors

* bsod (t1bur1an)

