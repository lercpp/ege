#from fnmatch import *

#for x in range(23,10**9,23):
#    if fnmatch(str(x),'12345?7?8'):
#        print(x,x//23)

#from fnmatch import *
#for x in range(141,10**8,141):
#    if fnmatch(str(x),'1234*7'):
#        print(x,x//141)

#from fnmatch import *

#for x in range(2023,10**10,2023):
#    if fnmatch(str(x),'1?2139*4'):
#        print(x,x//2023)

#from fnmatch import *

#for x in range(0,10**7,159):
#    if fnmatch(str(x),'2?1*67'):
#        print(x,x//159)

#from fnmatch import *

#for x in range(0,10**10,3052):
#    if fnmatch(str(x),'1?2139*4'):
#        print(x,x//3052)

#from fnmatch import *

#for x in range(0,10**10,7993):
#    if fnmatch(str(x),'4*4736*1'):
#        print(x,x//7993)

#from itertools import *

#comb = []
#for l in 0,1,2:
#    for x in product('13579',repeat=l):
#        comb.append(''.join(x))

#ans = []
#for a1 in comb:
#    for a2 in '02468':
#        for a3 in comb:
#            x = int(f'1{a1}2{a2}3{a3}45')
#            if x<=10**8 and x%153==0:
#                ans.append(x)
#for x in sorted(ans):
#    print(x,x//153)

#from itertools import *

#comb = []
#for l in 0,1,2,3:
#    for x in product('13579',repeat=l):
#        comb.append(''.join(x))

#ans = []
#for a1 in '02468':
#    for a2 in comb:
#        x = int(f'1{a1}2157{a2}4')
#        if x<=10**10 and x%133==0:
#            ans.append(x)
#for x in sorted(ans):
#    print(x,x//133)

#from itertools import *
#a=[]
#for l in 0,1,2,3:
#    for x in product('02468',repeat=l):
#        a.append(''.join(x))

#ans=[]
#for a1 in a:
#    for c in '0123456789':
#        x=int(f'1592{a1}6{c}8')
#        if x<=10**10 and x%1996==0:
#            ans.append(x)
#for x in sorted(ans):
#    print(x,x//1996)

#for a1 in '2468':
#    for a2 in '0123456789':
#        for a3 in '0123456789':
#            for a4 in '13579':
#                for a5 in '02468':
#                    x = int(f'{a1}9{a2}23{a3}23{a4}{a5}')
#                    if x%1984==0:
#                        print(x,x//1984)

#deliteli
#def div(x):
#    d=set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(1204300,1204381):
#    d=[i for i in div(x) if i%2==0]
#    s=sum(d)
#    if s!=0 and s%10==0:
#        print(x,s)

#def div(x):
#    d=set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(250200,251200):
#    d=div(x)
#    if len(d)>=2:
#        m=min(d)+max(d)
#        if m%123==17:
#            print(x,m)

#def div(x):
#    d=set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(452021,453021):
#    d=div(x)
#    if len(d)>0:
#        m=min(d)+max(d)
#        if m%7==3:
#            print(x,m)

#def div(x):
#    d=set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(150000,151000):
#    d=div(x)
#    if len(d)>0:
#        s=sum(d)
#        if s%13==10:
#            print(x,s)


#def div(x):
#    d=set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(350000,351000):
#    d=div(x)
#    if len(d)>0:
#        m=max(d)-min(d)
#        if m%23==9:
#            print(x,m)

#def div(x):
#    d=set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(550000,551000):
#    d=div(x)
#    if len(d)>0:
#        f=sum(d)//len(d)
#        if f%31==13:
#            print(x,f)

#def div(x):
#    d=set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(500000,501000):
#    d=[i for i in div(x) if i%10==8 and i!=8]
#    if len(d)>0:
#        print(x,min(d))

#def div(x):
#    d=set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(550000,551000):
#    d=[i for i in div(x) if i%10==7]
#    if len(d)==3:
#        print(x,max(d))

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(300_000_001,300_001_000):
#    d = div(x)
#    if len(d)>=6:
#        print(x,d[-6])

#def div(x):
#    d = set()
#    for i in range(1, int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for k in range(1,15000):
#    x = 750_000+k
#    d = [i for i in div(x) if i%2==0]
#    if len(d)%2!=0:
#        print(k, len(d))

#def div(x):
#    d ={1}
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)

#for x in range(769999,767500,-1):
#    d=div(x)
#    if len(d)>0:
#        a=sum(d)//len(d)
#        if a%100==12:
#            print(x,a)

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(699999,690000,-1):
#    d = div(x)
#    if len(d)>0:
#        M = sum(d)//len(d)
#        if M%1000==313:
#            print(x,M)

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(10_000_001,10_100_000):
#    d = div(x)
#    if len(d)>=3:
#        S = d[-1]+d[-2]+d[-3]
#        if S**0.5%1==0:
#           print(S)

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(1_180_000,1_200_001):
#    d = div(x)
#    if len(d)>=2:
#        S = d[0]+d[1]
#        if S%2022==0:
#            print(x,S)

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(200_000_001,200_010_000):
#    d = div(x)
#    if len(d)>=5:
#        P = d[0]*d[1]*d[2]*d[3]*d[4]
#        if P%10==1 and P<=x:
#            print(P,d[4])

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(900_001,900_500):
#    d = div(x)
#    if len(d)>0:
#        M = max(d)+min(d)
#        if M%100==46:
#            print(x,M)

#prostie
#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(1_000_001,1_001_000):
#    d = [i for i in div(x) if len(div(i))==0]
#    if len(d)==3:
#        print(x,max(d))

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(1_200_001,1_201_000):
#    d = [i for i in div(x) if len(div(i))==0]
#    if len(d)>0:
#        M = max(d)+min(d)
#        if M>2000 and M%10==8:
#            print(x,M)

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(32_500_001,32_501_000):
#    d = [i for i in div(x) if len(div(i))==0]
#    S = sum(d)
#    if S!=0 and S%145==0:
#        print(x,S)

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(23_600_001,23_601_000):
#    d = [i for i in div(x) if len(div(i))==0]
#    if len(d)>0:
#        M = max(d)+min(d)
#        if M%213==171:
#            print(x,M)

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(9500000,9510000):
#    d=[i for i in div(x) if len(div(i))==0]
#    if len(d)>0:
#        f=sum(d)//len(d)
#        if f%813==0:
#            print(x,f)

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(1_474_999,1_470_000,-1):
#    d = [i for i in div(x) if len(div(i))==0]
#    S = sum(d)
#    if S!=0 and S<=42000 and S%6==0:
#        print(x,S)

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(55000000,55051000):
#    d = [i for i in div(x) if len(div(i))==0 and i%1000==777]
#    if len(d)>0:
#        print(x,min(d))

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(3_333_338,3_338_000):
#    d = [i for i in div(x) if len(div(i))==0]
#    if len(d)>0:
#        R = max(d)-min(d)
#        if R>1000 and R%3==0:
#            print(x,R)

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(749999,740000,-1):
#    d = [i for i in div(x) if len(div(i))==0 and i%10==7]
#    if len(d)>0:
#        F = sum(d)//len(d)
#        if F%111==0:
#            print(x,F)

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(456_790,460_000):
#    d = [i for i in div(x) if len(div(i))==0]
#    if len(d)>=4:
#        M = d[0]+d[1]+d[-1]+d[-2]
#        if M%114==39:
#            print(x,M)

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(5_400_001,5_410_000):
#    d = [i for i in div(x) if len(div(i))==0]
#    if len(d)>0:
#        M = min(d)+max(d)
#        if M>60_000 and str(M)==str(M)[::-1]:
#            print(x,M)

#def div(x):
#    d = set()
#    for i in range(2, int(x**0.5)+1):
#        if x%i==0:
#            d|={i,x//i}
#    return sorted(d)

#for x in range(5_700_001,5_710_000):
#    d = [i for i in div(x) if len(div(i))==0]
#    if len(d)>0:
#        M = min(d)+max(d)
#        if M>70_000 and M**0.5%1==0:
#            print(x,M)

#def fact(n):
#    for i in range(2,int(n**0.5)+1):
#        if n%i==0:
#            return [i]+fact(n//i)
#    return [n]

#for x in range(125697,125722):
#    d = fact(x)
#    if len(d)==2 and d[0]!=d[1]:
#        print(d[0],d[1])

#def fact(n):
#    for i in range(2,int(n**0.5)+1):
#        if n%i==0:
#            return [i]+fact(n//i)
#    return [n]

#for x in range(1_324_728,1_330_000):
#    d=fact(x)
#    if len(d)==2 and str(d[0]).count('5')==1 and str(d[1]).count('5')==1:
#        print(x,max(d))

#def fact(n):
#    for i in range(2,int(n**0.5)+1):
#        if n%i==0:
#            return [i]+fact(n//i)
#    return [n]

#for x in range(7_305_679,7_310_000):
#    d = fact(x)
#    if len(d)==4 and str(sum(d))==str(sum(d))[::-1]:
#        print(x,sum(d))       

#def fact(n):
#    for i in range(2,int(n**0.5)+1):
#        if n%i==0:
#            return [i]+fact(n//i)
#    return [n]

#for x in range(3_502_101,3_505_000):
#    d = fact(x)
#    if len(d)==4 and 11 in d:
#        print(x,max(d))

#def fact(n):
#    for i in range(2,int(n**0.5)+1):
#        if n%i==0:
#            return [i]+fact(n//i)
#    return [n]

#for x in range(8_000_010,8_010_000,100):
#    d = fact(x)
#    if len(d)==len(set(d)):
#        print(x,max(d))                   

#def fact(n):
#    for i in range(2,int(n**0.5)+1):
#        if n%i==0:
#            return [i]+fact(n//i)
#    return [n]

#for x in range(5_000_012,5_010_000,100):
#    d = fact(x)
#    d5 = [x for x in d if d.count(x)==5]
#    if len(d5)>0:
#        print(x, min(d5))

#def fact(n):
#    for i in range(2,int(n**0.5)+1):
#        if n%i==0:
#            return [i]+fact(n//i)
#    return [n]

#for x in range(89428305, 89500000):
#    d = fact(x)
#    if len(d)>=6 and x%sum(d)==0:
#        print(x, sum(d))

#def fact(n):
#    for i in range(2,int(n**0.5)+1):
#        if n%i==0:
#            return [i]+fact(n//i)
#    return [n]
#for x in range(3_909_601,3_910_000):
#    d=fact(x)
#    dq=[i for i in d if max(d)>x]
#    if len(d)==7 and max(d)>sum(dq):
#        print(x,max(d))


#def fact(n):
#    for i in range(2,int(n**0.5)+1):
#        if n%i==0:
#            return [i]+fact(n//i)
#    return [n]

#for x in range(123456789, 123459000):
#    d = fact(x)
#    if len(d)==7 and '5' in str(sum(d)) and max(d)%10==9:
#        print(x,max(d))


#def fact(n):
#    for i in range(2,int(n**0.5)+1):
#        if n%i==0:
#            return [i]+fact(n//i)
#    return [n]

#for x in range(987654320, 98765000,-1):
#    d = fact(x)
#    if len(d)==13 and '1' in str(sum(d)):
#        print(x,max(d))

#for x in range(1_000_001,1_100_000):
#    for i in range(1,20):
#        y = x-5**i
#        if y>0 and y%222==0 and '1' not in str(y) and \
#           '3' not in str(y) and '5' not in str(y) and \
#           '7' not in str(y) and '9' not in str(y):
#            print(x,i)

for x in range(100000,150000):
    for i in range(1,20):
        y = x-3**i
        if '0' not in str(x) and y>0 and y%2!=0 and y%113==0:
            print(x,i)
