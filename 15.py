#def f(x):
#    return (a%7==0) and ((240%x==0)<=((a%x!=0)<=(780%x!=0)))
#
#for a in range(1,100000):
#    if all(f(x) == 1 for x in range(1,1000000)):
#           print(a)

#def f(x):
#    return (x%a!=0)<=((x%28==0)<=(x%49!=0))

#for a in range(1,10000):
#    if all(f(x) == 1 for x in range(1,1000000)):
#           print(a)

#def f(x):
#    return ((x%10==0) and (x%26==0) and (x>=300))<=(a<=x)

#for a in range(10000,1,-1):
#    if all(f(x)==1 for x in range(1,1000000)):
#           print(a)

#def f(x):
#    return (x%a==0) or ((x%23==0)<=(not(50<=x<=70)))

#for a in range(1,100000):
#    if all(f(x) == 1 for x in range(1,1000000)):
#           print(a)


#def f(x):
#    return ((x&52!=0)and(x&36==0))<=(x&a!=0)
#for a in range(1,100000):
#    if all(f(x)==1 for x in range(1,1000000)):
#        print(a)

#def f(x):
#    return ((x&103==0)and(x&94!=0))<=(x&a!=0)
#for a in range(1,100000):
#    if all(f(x) == 1 for x in range(1,1000000)):
#        print(a)

#def f(x):
#    return (x&30!=4) or ((x&35==1)<=(x&a==0))
#for a in range(10000,1,-1):
#    if all(f(x)==1 for x in range(1,1000000)):
#        print(a)

#def f(x,y):
#    return (x<a) and (y<a) and (x*y>1200)
#for a in range(1000,1,-1):
#    if all(f(x,y)==0 for x in range(1,1000)for y in range(1,1000)):
#           print(a)

#def f(x,y):
#    return (x<a)and(y<3*a)or(2*x+y>128)
#for a in range(1,10000):
#    if all(f(x,y)==1 for x in range(1,1000) for y in range(1,1000)):
#        print(a)

#def f(x,y):
#    return (x*y>a)or(x>y)or(11>x)
#for a in range(1000,1,-1):
#    if all(f(x,y)==1 for x in range(1,1000) for y in range(1,1000)):
#        print(a)

#def f(x):
#    return (a%5==0)and((2020%a!=0)<=((x%1718==0)<=(2023%a==0)))
#k=0
#for a in range(1,10000):
#    if all(f(x)==1 for x in range(1,1000000)):
#        k+=1
#print(k)

#def tr(x,y,z):
#    return x+y>z and x+z>y and y+z>x

#def f(x):
#    return tr(a,7,x) <= ((max(x+5,14)<=27) == (not tr(36,21,x)))
#
#for a in range(1000,1,-1):
#    if all(f(x)==1 for x in range(1,10**6)):
#        print(a)
#                
#def ugol(a,b,c):
#    return a>0 and b>0 and c>0 and a+b+c==180
#
#def f(x):
#    return ugol(37,a,x+45) == (ugol(a,x,90) and not(a+23<120))
#
#for a in range(1,1000):
#    if all(f(x)==1 for x in range(1,10**6)):
#        print(a)
#

#def f(x):
#    p= 23<=x<=45
#    q = 34<=x<=56
#    a = a1<=x<=a2
#    return not a or not p and q
#
#ox = [dx for x in (23,45,34,56) for dx in(x-0.01,x,x+0.01)]
#
#m = []
#for a1 in ox:
#    for a2 in ox:
#        if a2>a1 and all(f(x)==1 for x in ox):
#            m.append(a2-a1)
#print(max(m))

#def f(x):
#    b=25<=x<=40
#    c = 12<=x<=33
#    a= a1<x<=a2
#    return (b<=a)and((not c) or a)
#
#ox = [dx for x in (25,40,12,33) for dx in (x-0.01,x,x+0.01)]
#
#m=[]
#for a1 in ox:
#    for a2 in ox:
#        if a2>a1 and all(f(x)==1 for x in ox):
#            m.append(a2-a1)
#
#print(min(m))
#
#def f(x):
#    p=10<=x<=25
#    q=15<=x<=30
#    r=25<=x<=40
#    a=a1<=x<=a2
#    return (q<=(not r))and a and (not p)
#
#ox = [dx for x in (10,25,15,30,40) for dx in (x-0.01,x,x+0.01)]
#
#m=[]
#for a1 in ox:
#    for a2 in ox:
#        if a2>=a1 and all(f(x)==0 for x in ox):
#            m.append(a2-a1)
#print(max(m))
#
#def f(x):
#    P = 15<=x<=40
#    Q = 21<=x<=63
#    A = a1<=x<=a2
#    return P <= ((Q and not A) <= (not P))
#
#ox = [dx for x in (15,40,21,63) for dx in (x-0.01,x,x+0.01)]
#
#m = []
#for a1 in ox:
#    for a2 in ox:
#        if a2>a1 and all(f(x)==1 for x in ox):
#            m.append(a2-a1)
#print(min(m))
#
#def f(x):
#    p=15<=x<=33
#    q=35<=x<=48
#    a=a1<=x<=a2
#
#    return (a and not q)<=(p or q)
#
#ox=[dx for x in (15,33,35,48)  for dx in (x-0.01,x,x+0.01)]
#m=[]
#
#for a1 in ox:
#    for a2 in ox:
#        if a2>a1 and all(f(x)==1 for x in ox):
#            m.append(a2-a1)
#print(max(m))
#
#
#def f(x):
#    p=5<=x<=280
#    q=295<=x<=400
#    r=375<=x<=450
#    a=a1<=x<=a2
#
#    return (q<=p)or((not a)<=r)
#
#ox=[dx for x in (5,280,295,400,375,450)  for dx in (x-0.01,x,x+0.01)]
#m=[]
#
#for a1 in ox:
#    for a2 in ox:
#        if a2>a1 and all(f(x)==1 for x in ox):
#            m.append(a2-a1)
#print(min(m))
#
#def f(x):
#    B = 36<=x<=75
#    C = 60<=x<=110
#    A = a1<=x<=a2
#    return (not A) <= (B==C)
#
#ox = [dx for x in (36,75,60,110) for dx in (x-0.01,x,x+0.01)]
#
#m = []
#for a1 in ox:
#    for a2 in ox:
#        if a2>a1 and all(f(x)==1 for x in ox):
#            m.append(a2-a1)
#print(min(m))
#
#def f(x):
#    P = 69<=x<=91
#    Q = 77<=x<=114
#    A = a1<=x<=a2
#    return Q <= ((P==Q) or ((not P)<=A))
#
#ox = [dx for x in (69,91,77,114) for dx in (x-0.01,x,x+0.01)]
#
#m = []
#for a1 in ox:
#    for a2 in ox:
#        if a2>a1 and all(f(x)==1 for x in ox):
#            m.append(a2-a1)
#print(min(m))
#
#a = set()
#
#def f(x):
#    p= x in {1,3,4,9,11,13,15,17,19,21}
#    q= x in {3,6,9,12,15,18,21,24,27,30}
#    A = x in a
#
#    return (p<=A)or((not A)<=(not q))
#
#for x in range(1,1000):
#    if f(x)==0:
#        a.add(x)
#print(a)
#print(9*3*21*15)

a = set(range(1,1000))

def f(x):
    p=x in {2,4,6,8,10,12,14,16,18,20}
    q=x in {5,10,15,20,25,30,35,40,45,50}
    A=x in a
    return (A<=p)and(q<=(not A))

for x in range(1,1000):
    if f(x)==0:
        a.remove(x)
print(a)
