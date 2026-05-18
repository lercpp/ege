#from fnmatch import *

#for x in range(17,10**9,17):
#    if fnmatch(str(x),'12345?6?8'):
#        print(x,x//17)

#from fnmatch import *

#for x in range(161,10**8,161):
#    if fnmatch(str(x),'12*4?65'):
#        print(x,x//161)

#from fnmatch import *

#for x in range(0,10**8,2084):
#    if fnmatch(str(x),'*1?542?'):
#        print(x,x//2084)

#from fnmatch import *

#for x in range(0,10**8,2023):
#    if fnmatch(str(x),'3?1*57'):
#        print(x,x//2023)

#from fnmatch import *

#a = []
#for x in range(0,10**10,1234):
#    if fnmatch(str(x),'4*5*6') and fnmatch(str(x),'?74*68?'):
#        a.append(x)

#a = a[::-1]

#for x in a:
#    print(x,x//1234)

#a=[]

#for a1 in '0123456789':
#    for a2 in '0123456789':
#        for a3 in '0123456789':
#            x=int(f'12{a1}345{a2}67089{a3}')
#            if x%206==0:
#                a.append(x)
#

#from itertools import *

#a=[]

#for a1,a2,a3,a4 in product('02468',repeat=4):
#    for b1,b2,b3 in product('13579',repeat=3):
#        x=int(f'{a1}{b1}{a2}{a3}{b2}{a4}{b3}77')
#        if a1!='0' and x%7777==0:
#            a.append(x)
#a.sort()
#for x in a:
#    print(x,x//7777)

#from itertools import *
#a=[]
#for a1,a2,a3 in product('13579',repeat=3):
#    for p in '0123456789':
#        x=int(f'71{a1}{a2}{a3}39{p}28')
#        if x%2024==0:
#            a.append(x)

#a.sort()
#for x in a:
#    print(x,x//2024)

#from itertools import *

#comb = []
#for l in range(4):
#    for x in product('02468',repeat=l):
#        comb.append(''.join(x))

#a = set()
#for a1 in '0123456789':
#    for b1 in comb:
#        x = int(f'1592{b1}6{a1}8')
#        if x%1996 == 0:
#            a.add(x)

#a = sorted(a)
#for x in a:
#    print(x,x//1996)

k=0
for x in range(100000,1000000):
    if k==5:break
    if '0' not in str(x):
        for i in range(1,20):
            a2=x-3**i
            if a2>0 and a2%2!=0 and a2%113==0:
                k+=1
                print(x,i)
