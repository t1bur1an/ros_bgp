# Description

Two scripts and template for monitoring bgp sessions in zabbix. 

Import template to your zabbix instalation.

Place scripts in zabbix external scripts folder.


# Files

* bgpdiscovery.py - used for returning peers list to zabbix
* bgpmon.py - get bgp session state and return 0 or 1.
* RosAPI - RouterOS API library for python (thx David Jelić and Luka Blašković)

# Configs

For change connection credentials you should replace placeholders in function a.login().

In bgpmon it will be line 9 and in bgpdiscovery it will be line 11.

# Authors

* bsod (t1bur1an)

