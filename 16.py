#from functools import *
#@lru_cache(None)

#def f(n):
#    if n == 1: return 1
#    if n>1:return n*f(n-1)

#for i in range(1,2024):f(i)
#print (f(2023)/f(2020))

#from functools import *
#@lru_cache(None)

#def f(n):
#    if n == 1 : return 1
#    if n > 1: return n**2+f(n-1)

#for i in range(1,10000):f(i)
#print(f(1000)-f(997))

#from functools import *
#@lru_cache(None)

#def f(n):
#    if n > 100000:return n
#    if n<= 100000:return f(n+1)+5*n+2

#for i in range(1,100000):f(i)
#print(f(3)-f(7))

#from functools import *
#@lru_cache(None)

#def f(n):
#    if n<=3:return n
#    if n>3 and n%2!=0:return 2*n+f(n-2)
#    if n> 3 and n%2==0:return n**2+f(n-1)

#for i in range(1,1000000):f(i)
#print(f(10000)-f(9995))

#from functools import *
#@lru_cache(None)

#def f(n):
#    if n>=10000:return n
#    if n< 10000 and n%3==0:return n+f(n/3)
#    if n <10000 and n%3!=0:return 2*n+f(n+3)

#for i in range(1,10000):f(i)
#print(f(999)-f(46))


#from functools import *
#@lru_cache(None)

#def f(n):
#    if n==1:return 1
#    if n>1:return (2*n-1)*f(n-1)

#for i in range(1,10000):f(i)
#print(f(3516)/f(3513))


from functools import *
from math import *
@lru_cache(None)

def f(n):
    if n>=5000:return factorial(n)
    if 1<=n and n<5000:return 2**(5000-n)*factorial(n)

for i in reversed(range(1,5001)):f(i)
print(1000*f(7)/f(4))

#from functools import *
#@lru_cache(None)

#def f(n):
#    if n>10000:return n-10000
#    if 1<= n and n<=10000:return f(n+1)+f(n+2)

#for i in range(1,1000):f(i)
#print(f(12345)*((f(10)-f(12))/f(11))f(10101))

#from functools import *
#@lru_cache(None)

#def f(n):
#    if n==1:return 2
#    if n>1:return 2*f(n-1)

#for i in range(1,10000):f(i)
#print(f(1900)/2**1890)

#from functools import *
#@lru_cache(None)

#def f(n):
#    if n<4:return 1
#    if n>3 and n%2!=0:return n
#    if n>3 and n%2==0:return f(n-1)+f(n-2)+f(n-3)

#for i in range(1,10000):f(i)
#print(f(2254)-f(2252))
