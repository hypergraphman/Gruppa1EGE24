from ipaddress import ip_network

net = ip_network('114.179.203.128/255.255.255.192', False)
k = 0
for ip in net:
    if f'{int(ip):0>32b}'.count('1') % 3 == 0:
        k += 1
print(k)