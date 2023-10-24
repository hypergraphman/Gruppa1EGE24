from ipaddress import ip_network, ip_address

a = []
for i in range(0, 32 + 1):
    n1 = ip_network(f'192.148.56.26/{i}', False)
    n2 = ip_network(f'192.148.56.43/{i}', False)
    if n1 != n2:
        a.append(i)
print(min(a))
