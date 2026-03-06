#print(*[f'{x:08b}' for x in (255,255,254,0)])
#print( )
#print(*[f'{x:08b}' for x in (208,207,224,0)])

#from ipaddress import *
#for mask in range(33):
#     net =ip_network(f'215.181.200.27/{mask}',0)
#     print(net,net.netmask)

#from ipaddress import *
#for mask in range(33):
#    net=ip_network(f'142.198.113.106/{mask}',0)
#    print(net,mask)

#from ipaddress import *
#for mask in range(33):
#    net = ip_network(f'241.185.253.57/{mask}',0)
#    print(net,32-mask)

#from ipaddress import *
#for mask in range(33):
#    net = ip_network(f'108.133.75.91/{mask}',0)
#    print(net, 2**(32-mask))

#from ipaddress import *
#for mask in range(33):
#    net = ip_network(f'157.127.182.76/{mask}',0)
#    net1 = ip_network(f'157.127.190.80/{mask}',0)
#    if net!=net1:
#        print(mask)

#from ipaddress import *
#net = ip_network(f'102.161.200.51/255.255.255.0',0)
#print(net[-2])

#from ipaddress import *
#net = ip_network(f'192.168.12.207/255.192.0.0',0)
#m=[]
#for ip in net:
#    b=f'{ip:b}'
#    if b.count('0')==b.count('1'):
#        m.append(ip)
#print(m[-1])

#from ipaddress import *
#net = ip_network(f'172.16.168.0/255.255.248.0',0)
#m=0
#for ip in net:
#    b=f'{ip:b}'
#    if b.count('1')%5!=0:
#        m+=1
#print(m)


#from ipaddress import *
#net = ip_network(f'214.187.224.0/255.255.224.0',0)
#m = 0
#for ip in net:
#    b=f'{ip:b}'
#    if b.count('1')%6!=0 and b[-4]+b[-3]+b[-2]+b[-1]=='1000':
#        m+=1
#print(m)

#from ipaddress import *
#net=ip_network(f'203.111.195.0/255.255.240.0',0)
#m=0
#for ip in net:
#    b=f'{ip:b}'
#    if b.count('0')%3==0 and '000' in b and '111' in b:
#        m+=1
#print(m)

#from ipaddress import *
#def c(ip):
#    b=f'{ip:b}'
#    l=b[:16]
#    r=b[16:]
#    return l.count('0')>r.count('0')
#m=0
#for a in range(256):
#    net = ip_network(f'207.0.{a}.167/255.255.255.192',0)
#    if all(c(ip)==1 for ip in net):
#        m+=1
#print(m)
#from ipaddress import *

#for mask in range(33):
#    net = ip_network(f'84.32.84.32/{mask}',0)
#    ip = net[-2]
#    b = f'{ip:b}'
#    if b.count('1')==19:
#        print(mask)

from ipaddress import *
for mask in range(24,33):
    net = ip_network(f'172.16.168.0/{mask}',0)
    k=0
    for ip in net:
        b=f'{ip:b}'
        if b.count('0')%7==0:
            k+=1
    if k==35:
        print(net.netmask)
