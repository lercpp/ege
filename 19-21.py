#def g(s,p,end):
#    if s>=40 or p>end:return p==end or p==end-2
#    h=[g(s+1,p+1,end),g(s+4,p+1,end),g(s*2,p+1,end)]
#    return any(h) if (p+1)%2==end%2 else all(h)
#print(19,[s for s in range(1,40) if g(s,0,2)])
#print(20,[s for s in range(1,40) if g(s,0,3)])
#print(21,[s for s in range(1,40) if not g(s,0,2)and g(s,0,4)])

#def g(s,p,end):
#    if s>=78 or p>end:return p==end or p==end-2
#    h=[g(s+1,p+1,end),g(s+4,p+1,end),g(s*4,p+1,end)]
#    return any(h) if (p+1)%2==end%2 else all(h)
#print(19,[s for s in range(1,78) if g(s,0,2)])
#print(20,[s for s in range(1,78) if g(s,0,3)])
#print(21,[s for s in range(1,78) if not g(s,0,2)and g(s,0,4)])

#def g(s,p,end):
#    if s>=111 or p>end:return p==end or p==end-2
#    h=[g(s+1,p+1,end),g(s+3,p+1,end),g(s*4,p+1,end)]
#    return any(h) if (p+1)%2==end%2 else all(h)
#print(19,[s for s in range(1,111) if g(s,0,2)])
#print(20,[s for s in range(1,111) if g(s,0,3)])
#print(21,[s for s in range(1,111) if g(s,0,4)])

#def g(s,p,end):
#    if s<=87 or p>end:return p==end or p==end-2
#    h=[g(s-2,p+1,end),g(s//2,p+1,end)]
#    return any(h) if (p+1)%2==end%2 else all(h)
#print(19,[s for s in range(89,100) if g(s,0,2)])
#print(20,[s for s in range(89,10000) if g(s,0,3)])
#print(21,[s for s in range(89,10000) if not g(s,0,2) and g(s,0,4)])

#def g(s,e):
#    if s>=17 or e<0:return e%2==0
#    h=[g(s-3,e-1),g(s-8,p+1,e),g(s//3,e-1)]
#    return any(h) if (e-1)%2==0 else all(h)
#print(19,[s for s in range(17,100) if g(s,2)])

#def g(s,m):
#    if s>=54:return m%2==0
#    if m==0:return 0
#    h=[g(s+2,m-1),g(s*2,m-1)]
#    return any(h) if (m-1)%2==0 else all(h)
#print(19,[s for s in range(1,54) if g(s,2)])
#print(20,[s for s in range(1,54) if not g(s,1) and g(s,3)])
#print(21,[s for s in range(1,54) if not g(s,2) and g(s,4)])

#def f(s,m):
#    if s>=39:return m%2==0
#    if m==0:return 0
#    h=[f(s+1,m-1),f(s+3,m-1),f(s*2,m-1)]
#    return any(h) if (m-1)%2==0 else all(h)
#print(19,[s for s in range(1,40) if f(s,2)])
#print(20,[s for s in range(1,40) if not f(s,1) and f(s,3)])
#print(21,[s for s in range(1,40) if not f(s,2) and f(s,4)])

#def f(s,m):
#    if s<=12:return m%2==0
#    if m==0:return 0
#    h=[f(s-1,m-1),f(s-2,m-1),f(s-3,m-1),f(s-4,m-1),f(s-5,m-1),f(s//5,m-1)]
#    return any(h) if (m-1)%2==0 else all(h)
#print(19,[s for s in range(20,1000) if f(s,2)])
#print(20,[s for s in range(20,1000) if not f(s,1) and f(s,3)])
#print(21,[s for s in range(20,1000) if not f(s,2) and f(s,4)])

#def f(s,m):
#    if s<=17:return m%2==0
#    if m==0:return 0
#    h=[f(s-3,m-1),f(s-5,m-1),f(s//2,m-1)]
#    return any(h) if (m-1)%2==0 else all(h)
#print(19,[s for s in range(18,1000) if f(s,2)])
#print(20,[s for s in range(18,1000) if not f(s,1) and f(s,3)])
#print(21,[s for s in range(18,1000) if not f(s,2) and f(s,4)])


#def f(a,b,m):
#    if a+b>=231:return m%2==0
#    if m==0:return 0
#    h=[f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
#    return any(h) if (m-1)%2==0 else any(h)
##all->any
#print(19,[s for s in range(1,214) if f(17,s,2)])
#print(20,[s for s in range(1,214) if not f(17,s,1) and f(17,s,3)])
#print(21,[s for s in range(1,214) if not f(17,s,2) and f(17,s,4)])

#def f(a,b,m):
#    if a+b>=150:return m%2==0
#    if m==0:return 0
#    h=[f(a+1,b,m-1),f(a,b+1,m-1),f(a+2,b,m-1),f(a,b+2,m-1),f(a+b,b,m-1),f(a,b+a,m-1)]
#    return any(h) if (m-1)%2==0 else all(h)
#print(19,[s for s in range(1,87) if f(61,s,2)])
#print(20,[s for s in range(1,87) if not f(61,s,1) and f(61,s,3)])
#print(21,[s for s in range(1,87) if not f(61,s,2) and f(61,s,4)])


#def f(a,b,m):
#    if a*b>=541:return m%2==0
#    if m==0:return 0
#    h=[f(a+10,b,m-1),f(a,b+10,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
#    return any(h) if (m-1)%2==0 else any(h)

#print(19,[s for s in range(1,90) if f(6,s,2)])
#print(20,[s for s in range(1,90) if not f(6,s,1) and f(6,s,3)])
#print(21,[s for s in range(1,90) if not f(6,s,2) and f(6,s,4)])

#from math import *
#def f(a,b,m):
#    if a+b<=20:return m%2==0
#    if m==0:return 0
#    h=[f(a-1,b,m-1),f(a,b-1,m-1),f(ceil(a/2),b,m-1),f(a,ceil(b/2),m-1)]
#    return any(h) if (m-1)%2==0 else all(h)

#print(19,[s for s in range(11,1000) if f(10,s,2)])
#print(20,[s for s in range(11,1000) if not f(10,s,1) and f(10,s,3)])
#print(21,[s for s in range(11,1000) if not f(10,s,2) and f(10,s,4)])

#def f(s,m):
#    if 36<=s<=60:return m%2==0
#    if s>60:return m%2!=0
#    if m==0:return 0
#    h=[f(s+1,m-1),f(s*2,m-1),f(s*3,m-1)]
#    return any(h) if (m-1)%2==0  else all(h)
#print(19,[s for s in range(1,36) if f(s,2)])
#print(20,[s for s in range(1,36) if not f(s,1) and f(s,3)])
#print(21,[s for s in range(1,36) if not f(s,2) and f(s,4)])    

#def f(a,b,m):
#    if a>=479 or b>=479:return m%2==0
#    if m==0:return 0
#    h = [f(a+1,b,m-1),f(a,b+1,m-1),f(a+3,b,m-1),f(a,b+3,m-1),\
#         f(a*2,b,m-1),f(a,b*2,m-1)]
#    return any(h) if (m-1)%2==0 else all(h)

#print(19,[s for s in range(1,479) if f(239,s,2)])
#print(20,[s for s in range(1,479) if not f(239,s,1) and f(239,s,3)])
#print(21,[s for s in range(1,479) if not f(239,s,2) and f(239,s,4)])

#def f(s,m):
#    if s<=16:return m%2==0
#    if m==0:return 0
#    h=[f(s-3,m-1),f(s-8,m-1),f(s//3,m-1)]
#    return any(h) if (m-1)%2==0 else all(h)

#print(19,[s for s in range(18,1000) if f(s,2)])
#print(20,[s for s in range(18,479) if not f(s,1) and f(s,3)])
#print(21,[s for s in range(18,479) if not f(s,2) and f(s,4)])

def f(a,b,m):
    if a+b>=259:return m%2==0
    if m==0:return 0
    h=[f(a+1,b,m-1),f(a*2,b,m-1),f(a,b+1,m-1),f(a,b*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)

print(19,[s for s in range(1,242) if f(17,s,2)])















































