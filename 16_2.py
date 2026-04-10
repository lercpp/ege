from functools import *
#@lru_cache(None)
#def f(n):
#    if n==1:
#        return 1
#    return (3*n+5)*f(n-1)
#for i in range(1,10000):f(i)
#print(f(2073)/f(2070))

#@lru_cache(None)
#def f(n):
#    if n>=2222:return n
#    if n<2222:return n**3+f(n+2)
#for i in range(2223,1,-1):f(i)
#print(f(4)-f(10))

#@lru_cache(None)
#def f(n):
#    if n<3:return 1
#    if n>2 and n%2==0:return f(n-1)+n-1
#    if n>2 and n%2!=0:return f(n-2)+2*n-2
#for i in range(1,1000):f(i)
#print(f(2048)-f(2045))

#@lru_cache(None)
#def f(n):
#    if n<10:return n-1
#    if n>=10 and n%2==0:return 3*n-1+f(n-3)
#    return 5*n+2+f(n-4)
#for i in range(1,1000):f(i)
#print(f(4445)-f(4444))

#@lru_cache(None)
#def f(n):
#    if n==1:return 1
#    if n>1:return n*f(n-1)
#for i in range(1,10000):f(i)
#print((f(2024)-f(2023))/f(2022))

#@lru_cache(None)
#def f(n):
#    if n==1:return 1
#    return 2*n*f(n-1)
#for i in range(1,10000):f(i)
#print((f(2024)//16-f(2023))/f(2022))

#@lru_cache(None)
#def f(n):
#    if n>10000:return n-10000
#    return f(n+1)+f(n+2)
#for i in range(100000,1,-1):f(i)
#print(f(12345)*((f(10)-f(12))//f(11))+f(10101))

#@lru_cache(None)
#def f(n):
#    if n>=2010:return n
#    return f(n+3)+f(n+2)+f(n+1)
#for i in range(10000,1,-1):f(i)
#print((f(2000)-2*(f(2002)+f(2003)))//f(2004))

#from math import factorial
#@lru_cache(None)
#def f(n):
#    if n>=5000:return factorial(n)
#    return 2*f(n+1)//(n+1)
#for i in range(5000,1,-1):f(i)
#print(1000*f(7)//f(4))

#@lru_cache(None)
#def f(n):
#    if n<3:return n
#    return n-1+f(n-1)
#for i in range(1,5000):f(i)
#print(f(4044))

#@lru_cache(None)
#def f(n):
#    return g(n-1)+g(n-3)

#@lru_cache(None)
#def g(n):
#    if n<=9:return 3*n
#    return g(n-4)+2
#for i in range(1,500000):f(i)
#print(f(42999))

#@lru_cache(None)
#def g(n):
#    if n<100:return n
#    if n>=100:return f(n-3)+1
#@lru_cache(None)
#def f(n):
#    return g(n-2)
#for i in range(1,5001):g(i)

#print(f(5000))

#@lru_cache(None)
#def f(n):
#    if n==1:return 2
#    return f(n-1)+5*n**2
#for i in range(1,100):f(i)
#print(f(39))

#@lru_cache(None)
#def f(n):
#    if n==1:return 1
#    if n%2==0:return n+f(n-1)
#    return 2*f(n-2)
#for i in range(1,1000):f(i)
#print(f(26))

#@lru_cache(None)
#def f(n):
#    if n==1:return 1
#    if n==2:return 2
#    if n>2 and n%2==0:return (n+f(n-2))//5
#    return (2*n+f(n-1)+f(n-2))//4
#for i in range(1,1000):f(i)
#print(f(50))

#@lru_cache(None)
#def f(n):
#    if n<2:return 1
#    if n%3==0:return f(n//3)-1
#    return f(n-1)+7
#for n in range(1,100000):
#    if f(n)==111:
#        print(n)

#@lru_cache(None)
#def f(n):
#    if n<3:return 1
#    if n%2!=0:return f(n-1)+n
#    return f(n-3)+2*n
#for i in range(1,1000):f(i)
#print(f(2048)-f(2041))

#@lru_cache(None)
#def f(n):
#    if n<3:return 3
#    return  2*n+5+f(n-2)
#for i in range(1,10000):f(i)
#print(f(3027)-f(3023))

#@lru_cache(None)
#def f(n):
#    if n>=10000:return n
#    if n%2==0:return f(n+2)-3
#    return f(n+2)+1
#for i in range(10000,80,-1):f(i)
#print(f(94)-f(80))

#@lru_cache(None)
#def f(n):
#    if n>3000:return 1
#    if n%2==0:return f(n+1)-n+1
#    return f(n+2)-2*n+2
#for i in range(30000,1,-1):f(i)
#print(2*f(39)-2*f(34))

#@lru_cache(None)
#def f(n):
#    return g(n-1)
#@lru_cache(None)
#def g(n):
#    if n<=9:return 3*n
#    return g(n-2)+1
#for i in range(9,47995):g(i)
#print(f(47995))

#@lru_cache(None)
#def f(n):
#    if n>30:return f(n-6)+2048
#    return 3*(g(n-5)+13)
#@lru_cache(None)
#def g(n):
#    if n>=221337: return 2*n+50
#    return g(n+11)-48
#for i in range(221337,1,-1):g(i)
#print(f(5078))

#@lru_cache(None)
#def f(n):
#    if n<3:return n
#    if n%2!=0:return f(n-1)+f(n-2)+1
#    return sum(f(i) for i in range(1,n))
#print(f(38))

#@lru_cache(None)
#def f(n):
#    if n<=2:return 1
#    if n%2!=0:return f(n-1)-n
#    return f(n-2)+g(n-1)+2
#@lru_cache(None)
#def g(n):
#    if n<=0:return 2
#    if n%2!=0:return f(n-1)-2*g(n-2)
#    return 2*f(n-2)*g(n-1)
#for i in range(1,10000):g(i)
#print(f(96))

#нестандартные
#k=0
#def f(n):
#    global k
#    k+=1
#    if n>=1:
#        k+=1
#        f(n-1)
#        f(n-3)
#        k+=1
#f(40)
#print(k)

#k=0
#def f(n):
#    global k
#    k+=n+1
#    if n>1:
#        k+=n+5
#        f(n-1)
#        f(n-2)
#f(30)
#print(k)

#def f(n):
#    if n<=1:return n
#    if n%3==0:return n+f(n//3)
#    return n+f(n+3)
#for n in range(1,1000):
#    try:
#       print(n,f(n))
#    except:
#        pass

#def f(n):
#    if n<3:return n+1
#    if n%2==0:return f(n-2)+n-2
#    return f(n+2)+n+2
#k=0
#for n in range(1,1000):
#    try:
#        if 10000<=f(n)<100000:
#            k+=1
#    except:
#        pass
#print(k)

#@lru_cache(None)
#def f(n):
#    if n>=3210:return 1
#    return f(n+3)+7
#for n in range(10000,15,-1):f(n)
#@lru_cache(None)
#def g(n):
#    if n<10:return n
#    return g(n-3)+5
#print(f(15)-g(3000))

#@lru_cache(None)
#def f(n):
#    if n>=10000:return n
#    if n%6==0:return n//6+f(n//6+2)
#    return n+f(n+2)
#for i in range(10000,7,-1):
#    if i%2!=0:
#        f(i)
#print(f(264)-f(7))

#@lru_cache(None)
#def f(n):
#    if n==1:return 2
#    return f(n-1)*3**(n%5)/3**(n%7)
#print(f(1025)//f(1030))

def f(n):
    if n<2: return n
    return f(n//2)*10+n%2

for n in range(1,20):
    print(n,f(n))

print(int('100000100001000100101',2))

s = 0
for k in range(123_456_789,0,-1):
    if 11_223_456_789%k==0:
        s += k**2
print(s)
