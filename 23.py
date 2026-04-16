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

def f(c,e,b):
    if c>e:return 0
    if c==e:return 1
    return f(c+b,e,b)+f(c*2,e,b)
for b in range(1,1000):
    if f(1,10,b)*f(10,100,b)==13:
        print(b)
