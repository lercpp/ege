#def f(c,e):
#    if c>e:return 0
#    if c==e:return 1
#    if c<e:return f(c+1,e)+f(c*2,e)+f(c**2,e)
#print(f(5,154))


#def f(c,e):
#    if c>e or c==14:return 0
#    if c==e:return 1
#    return f(c+1,e)+f(c+2,e)+f(c*3,e)
#print(f(1,10)*f(10,15))

#def f(c,e):
#    if c>e or c==10 or c==15:return 0
#    if c==e:return 1
#    return f(c+1,e)+f(c+2,e)+f(c+3,e)
#print(f(5,11)*f(11,18))

#def f(c,e):
#    if c>e:return 0
#    if c==e:return 1
#    return f(c+1,e)+f(c*2,e)
#print(f(2,7)*f(7,16)*f(16,39))

#def f(c,e):
#    if c<e:return 0
#    if c==e:return 1
#    return f(c-2,e)+f(c-5,e)
#print(f(23,2))

#def f(c,e):
#    if c<e or c==24:return 0
#    if c==e:return 1
#    return f(c-2,e)+f(c-3,e)+f(c//4,e)
#print(f(36,13))

#def f(c,e):
#    if c<e or c==7:return 0
#    if c==e:return 1
#    return f(c-1,e)+f(c-3,e)+f(c//2,e)
#print(f(19,10)*f(10,3))

#def f(c,e):
#    if c<e or c==28:return 0
#    if c==e:return 1
#    return f(c-3,e)+f(c//3,e)+f(c//2,e)
#print(f(46,20)*f(20,3))

#def f(c,e):
#    if c>e or c==17:return 0
#    if c==e:return 1
#    return f(c+2,e)+f(c+3,e)+f(c+5,e)
#print(f(5,13)*f(13,25))

#def f(c,e):
#    if c>e or c==13:return 0
#    if c==e:return 1
#    return f(c+2,e)+f(c+3,e)+f(c+5,e)
#print(f(5,17)*f(17,25))

#def f(c,e):
#    if c>e :return 0
#    if c==e:return 1
#    return f(c+2,e)+f(c+4,e)+f(c+5,e)
#for e in range(1,1000):
#    if f(31,e)==1001:
#        print(e)

#def f(c,e):
#    if c<e:return 0
#    if c==e:return 1
#    if c>e:
#        k=f(c-3,e)
#        if c%2==0: k+=f(c//3,e)
#        if c>=10: k+=f(c//10,e)
#        return k
#print(f(1250,20))

#def f(c,e,b):
#    if c>e:return 0
#    if c==e:return 1
#    return f(c+b,e,b)+f(c*2,e,b)
#for b in range(1,1000):
#    if f(1,10,b)*f(10,100,b)==13:
#        print(b)


#def f(c,e,step):
#    if c>e or step>7: return 0
#    if c==e: return step==7
#    if c<e: return f(c+1,e,step+1)+f(c+4,e,step+1)+f(c*2,e,step+1)

#print(f(3,27,0))


#def f(c,e,s):
#    if c>e or s>5:return 0
#    if c==e:return s==5
#    if c<e: return f(c+2,e,s+1)+f(c+3,e,s+1)+f(c*2,e,s+1)

#k = 0
#for e in range(11,400):
#    if f(10,e,0)>0:
#        k += 1
#print(k)

#def f(c,e,s):
#    if c>e or s>mx: return 0
#    if c==e: return s==mx
#    if c<e: return f(c+2,e,s+1)+f(c*2,e,s+1)

#for mx in range(1,20):
#    if f(1,100,0)>0:
#        print(mx)

#def f(c,e,p):
#    if c>e: return 0
#    if c==e: return 1
#    if c<e and p=='+1': return f(c+3,e,'+3')+f(c*2,e,'*2')
#    if c<e and p!='+1': return f(c+1,e,'+1')+f(c+3,e,'+3')+f(c*2,e,'*2')

#print(f(3,30,''))

#def f(c,e,k):
#    if c>e: return 0
#    if c==e: return k==1
#    if c<e: return f(c+1,e,k)+f(c+2,e,k)+f(c*2,e,k+1)

#print(f(2,12,0))

#def f(c,e,k1,k2,k3):
#    if c>e: return 0
#    if c==e: return k1>0 and k2>0 and k3>0
#    if c<e: return f(c+1,e,k1+1,k2,k3)+f(c+2,e,k1,k2+1,k3)+\
#       f(c*2,e,k1,k2,k3+1)

#print(f(3,25,0,0,0))

#def f(c,e,k):
#    k += 1
#    if c>e: return 0
#    if c==e: return k>52
#    if c<e: return f(c+2,e,k)+f(c*3,e,k)+f(c*4,e,k)

#print(f(2,400,0))

#def f(c,e,k1):
#    if c%2!=0: k1+=1
#    if c>e or k1>1: return 0
#    if c==e: return k1==1
#    if c<e: return f(c+1,e,k1)+f(c+2,e,k1)+f(c*2,e,k1)

#print(f(2,40,0))

#def f(c,e,k0):
#    if c%2==0: k0+=1
#    if c>e: return 0
#    if c==e: return k0==6
#    if c<e: return f(c+1,e,k0)+f(c+3,e,k0)+f(c+5,e,k0)

#print(f(3,25,0))

#def f(c,e,s):
#    if c>e or s>5: return 0
#    if c==e: return s<=5
#    if c<e: return f(c+1,e,s+1)+f(c*2,e,s+1)

#for x in range(2,100):
#    if f(1,x,0)==0:
#        print(x)

#def f(c,e,tr):
#    if c>e or c==28 or 'BACA' in tr: return 0
#    if c==e: return 1
#    if c<e: return f(c+2,e,tr+'A')+f(c+3,e,tr+'B')+f(c*2,e,tr+'C')

#print(f(2,40,''))

#d = set()
#def f(c,s,p):
#    if s==24:
#        d.add(c)
#        return 1
#    if s<24:
#        if p=='+1': return f(c+7,s+1,'+7')+f(c*4,s+1,'*4')
#        if p=='+7': return f(c+1,s+1,'+1')+f(c*4,s+1,'*4')
#        if p=='*4': return f(c+1,s+1,'+1')+f(c+7,s+1,'+7')
#        if p=='': return f(c+1,s+1,'+1')+f(c+7,s+1,'+7')+f(c*4,s+1,'*4')

#print(f(1,0,''))
#print(len(d))

from functools import *

@lru_cache(None)
def f(c,e,k18,p):
    if c==18: k18 = 1
    if c>e or c==33: return 0
    if c==e: return k18==1
    if c<e and p!='*2': return f(c+1,e,k18,'+1')+f(c+3,e,k18,'+3')+\
       f(c*2,e,k18,'*2')
    if c<e and p=='*2': return f(c+1,e,k18,'+1')+f(c+3,e,k18,'+3')

print(f(2,51,0,''))
