# Lab: 
# 1. Given a list of strings filter valid ip addresses
# 2. In given ip_address filter out(remove) local_ip_addresses
from utilities.utils import is_valid_ip as vip

if __name__ == '__main__':
    # 1. Given a list of strings filter valid ip addresses
    list_of_ips = ["192.168.1.1","192.a.1.1","100.5.12.1","172.1.1.8","a.b.c.d","10.1.2.1"]
    valid_ips = list(filter(vip,list_of_ips))
    print(valid_ips)

    ## 2. In given ip_address filter out(remove) local_ip_addresses