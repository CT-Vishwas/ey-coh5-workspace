d1 = {
    "192.168.1.23" : 4,
    "192.168.1.21" : 1,
    "192.168.1.6" : 15,
    "192.168.1.19" : 2,
    "192.168.1.20" : 57,
    "192.168.1.2" : 9, 
    "192.168.1.26" : 3,
}

# iterate over dict items
l1 = list(d1.items())
l1.sort(key=lambda x: x[1], reverse=True)
print("Printing List of Ips with failed attempts in descending order:")
print("IP ADDRESS\t|\tNUMBER OF FAILED ATTEMPTS")
print("-"*50)
for k,v in l1:
    print(k,"\t|\t",v)