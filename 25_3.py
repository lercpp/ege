#def div(x):
#    d = set()
#    for i in range(1, int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(1_000_001,1_001_000):
#    d = [i for i in div(x) if len(div(i))==2]
#    if len(d)==3:
#        print(x, max(d))

#def div(x):
#    d=set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(32500001,10000000000):
#    d = [i for i in div(x) if len(div(i))==0]
#    s=sum(d)
#    if s!=0 and s%145==0:
#        print(x,s)

#def div(x):
#    d=set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(650001,700000):
#    d=[i for i in div(x) if len(div(i))==0]
#    if len(d)>0:
#        f=sum(d)//len(d)
#        if f%37==23:
#            print(x,f)

#def div(x):
#    d=set()
#    for i in range(1,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(5700001,5710000):
#    d=[i for i in div(x) if len(div(i))==2]
#    if len(d)>0:
#        m=max(d)+min(d)
#        if m>70000 and m**0.5%1==0:
#            print(x,m)

#def fact(x):
#    d = []
#    i = 2
#    while i**2<=x:
#        while x%i==0:
#            d.append(i)
#            x=x//i
#        i+=1
#    if x>1: d.append(x)
#    return d

#for x in range(125_697, 125_722):
#    d = fact(x)
#    if len(d)==2 and d[0]!=d[1]:
#        print(d[0],d[1])

#def fact(x):
#    d = []
#    i = 2
#    while i**2<=x:
#        while x%i==0:
#            d.append(i)
#            x=x//i
#        i+=1
#    if x>1: d.append(x)
#    return d

#for x in range(6_086_056, 6_088_000):
#    d = fact(x)
#    if len(d)==2 and str(d[0]).count('6')==1 and str(d[1]).count('6')==1:
#        print(x,max(d))

#def fact(x):
#    d=[]
#    i=2
#    while i**2<=x:
#        while x%i==0:
#            d.append(i)
#            x=x//i
#        i+=1
#    if x>1:d.append(x)
#    return d

#for x in range(12365267,12376266):
#    d=fact(x)
#    if len(d)==5 and len(set(d))==5 and len(fact(sum(d)))==1:
#        print(x,sum(d))

#def fact(x):
#    d = []
#    i = 2
#    while i**2<=x:
#        while x%i==0:
#            d.append(i)
#            x=x//i
#        i+=1
#    if x>1: d.append(x)
#    return d

#for x in range(24_517_512,24_530_000):
#    d = fact(x)
#    if len(d)==12:
#        print(x,max(d))

#def fact(x):
#    d = []
#    i = 2
#    while i**2<=x:
#        while x%i==0:
#            d.append(i)
#            x=x//i
#        i+=1
#    if x>1: d.append(x)
#    return d

#for x in range(5_000_001,6_000_000,2):
#    d = fact(x)
#    if len(d)==2 and d[0]%2!=0 and d[1]%2!=0 and len(fact(d[1]-d[0]))==1:
#        print(x,max(d))

def fact(x):
    d = []
    i = 2
    while i**2<=x:
        while x%i==0:
            d.append(i)
            x=x//i
        i+=1
    if x>1: d.append(x)
    return d

def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(5_200_001,5_220_000):
    d = fact(x)
    if len(d)==9 and len(div(x))%90==0:
        print(x,max(d))
