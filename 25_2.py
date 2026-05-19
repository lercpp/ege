#def div(x):
#    d = set()
#    for i in range(1,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(164700,164753):
#    d = div(x)
#    if len(d)==6:
#        print(d[-2],d[-1])

#def div(x):
#    d=set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)
#for x in range(136179,10000000):
#    d = div(x)
#    if sum(d)%385==91:
#        print(x,sum(d))

#def div(x):
#    d=set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(1204300,1204380):
#    d=[i for i in div(x) if i%2==0]
#    if sum(d)!=0 and sum(d)%10==0:
#        print(x,sum(d))

#def div(x):
#    d = set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)


#for x in range(100000,500001):
#    d = [i for i in div(x) if i%2==0]
#    if len(d)>150:
#        print(x, d[-1] - d[0])

#def div(x):
#    d = set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(300000,301000):
#    d=[i for i in div(x) if i%3==0]
#    if len(d)==5:
#        print(x,max(d))

#def div(x):
#    d = set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)
#for x in range(700001,701000):
#    d = [i for i in div(x) if i%10==7 and i!=7]
#    if len(d)>0:
#        print(x, d[0])

#def div(x):
#    d = set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)
#for x in range(250200,251200):
#    d=div(x)
#    if len(d)>0:
#        m=d[-1]+d[0]
#        if m%123==17:
#            print(x,m)

#def div(x):
#    d = set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(550001,551000):
#    d = div(x)
#    if len(d)>0:
#        F = sum(d)//len(d)
#        if F%31==13:
#            print(x,F)

#def div(x):
#    d = set()
#    for i in range(1,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(4_000_001,4_001_000):
#    d = [i for i in div(x) if i!=x]
#    if len(d)>=5:
#        M = d[-5]+d[-4]+d[-3]+d[-2]+d[-1]
#        if M%10==0:
#            print(x,M)

def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(400_000_001,400_001_000):
    d = div(x)
    if len(d)>=7:
        print(d[-7],len(d))
