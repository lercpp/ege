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
                
def ugol(a,b,c):
    return a>0 and b>0 and c>0 and a+b+c==180

def f(x):
    return ugol(37,a,x+45) == (ugol(a,x,90) and not(a+23<120))

for a in range(1,1000):
    if all(f(x)==1 for x in range(1,10**6)):
        print(a)


