# IP_anon - IP address replacement script

The aim is to write a script that will:

- Detect IP addresses given an input file (currently sample_conf.txt)
- Create a mapping of IP addresses or subnets to matching RFC 1918 addresses, while preserving the relevant octets. E.g: 212.122.32.5 : 172.16.1.5, 212.122.32.0 255.255.224.0 : 172.12.32 255.255.255.224

This would allow files to be shared amongst network administrators easily for troubleshooting purposes.


