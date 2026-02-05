#print('x y z')
#for x in 0,1:
#    for y in 0,1:
#        for z in 0,1:
#            f=(x<=y)and(y<=z)
#            if f == 1:
#                print(x,y,z)
#   

#print('w x y z')
#for w in 0,1:
#    for x in 0,1:
#        for y in 0,1:
#            for z in 0,1:
#              f= w or (x<=y) and (not z <= x) 
#              if f==0:
#                  print(w,x,y,z) 
#
#print('x y z w')
#for x in 0,1:
#    for y in 0,1:
#        for z in 0,1:
#            for w in 0,1:
#                f = (not x or y or not z)and(x or not y)or not w
#                if f==0:
#                    print(x,y,z,w)         

#print('a b c d')
#for a in 0,1:
#    for b in 0,1:
#        for c in 0,1:
#            for d in 0,1:
#                f = ((a and b)== (not c)and (b<=d))
#                if f == 1:
#                    print(a,b,c,d)
#
#print('w x y z')
#for w in 0,1:
#    for x in 0,1:
#        for y in 0,1:
#            for z in 0,1:
#                f= ((x or y)<=z)or (y==w)or z
#                if f==0:
#                    print(w,x,y,z)
#
#print('w x y z')
#for w in 0,1:
#    for x in 0,1:
#        for y in 0,1:
#            for z in 0,1:
#                f = x and (z<=w)and(not y)
#                if f==1:
#                    print(w,x,y,z)
#
#print('x y z w')
#for x in 0,1:
#    for y in 0,1:
#        for z in 0,1:
#            for w in 0,1:
#                f= (w<=y)and((x<=z)==(y<=x))
#                if f==1:
#                    print(x,y,z,w)
#
#print('w x y z')
#f or w in 0,1:
#   for x in 0,1:
#       for y in 0,1:
#           for z in 0,1:
#               f = not((not x or y)and not w)or not(z and not(y and w))
#               if f==0:
#                   print(w,x,y,z)
#
#print('x y z w')
#for x in 0,1:
#    for y in 0,1:
#        for z in 0,1:
#            for w in 0,1:
#                f = not(((x<=(y and w))and (z<=(x or y)))==w)
#                if f==1:
#                    print(x,y,z,w)
#     
#
#print('w x y z')
#for w in 0,1:
#    for x in 0,1:
#        for y in 0,1:
#            for z in 0,1:  
#                f1 =  (x<=y) or ((not w)== z)
#                f2 = (x<=y)==(w and (not z))
#                if f1 == f2:
#                    print(w,x,y,z)

#from itertools import *
#
#def f(w,x,y,z):
#    return x and not y and (not z or w)
#
#t = [(0,0,1,0),(0,0,1,1),(1,0,1,1)]
#
#for p in permutations('wxyz'):
#    if [f(**dict(zip(p,r)))for r in t] == [1,1,1]:
#        print(p)

from itertools import *

#def f(x,y,z):
#    return (not x and y and z)or(not x and not y and z)or(not x and not y and not z)
#
#t = [(0,0,0),(1,0,0),(1,0,1)]
#for p in permutations('xyz'):
#    if [f(**dict(zip(p,r)))for r in t]== [1,1,1]:
#        print(p)

#def f(w,x,y,z):
#    return w or (x<=y)and((not z)<=x)
#
#t = [(0,0,0,1),(0,0,1,0),(0,1,0,1)]
#
#for p in permutations('wxyz'):
#    if [f(**dict(zip(p,r)))for r in t]==[0,0,0]:
#        print(p)

#def f(w,x,y,z):
#    return ((x or y)<=z)or(y==w)or z
#
#for a1,a2,a3,a4 in product([0,1],repeat = 4):
#    t = [(0,1,a1,a2),(1,a3,1,0),(a4,1,1,0)]
#    if len(set(t))==3:
#        for p in permutations('wxyz'):
#            if [f(**dict(zip(p,r)))for r in t]==[0,0,0]:
#                print(p)
#
#def f(w,x,y,z):
#    return not(w<=(x==y))and (z<=x)
#
#for a1,a2,a3,a4,a5 in product([0,1],repeat=5):
#    t = [(a1,0,1,0),(0,a2,a3,0),(a4,1,1,a5)]
#    if len(set(t))==3:
#        for p in permutations('wxyz'):
#            if [f(**dict(zip(p,r)))for r in t]==[1,1,1]:
#                print(p)
#
#def f(w,x,y,z):
#    return (w<=(not(z<=x)))or y
#
#for a1,a2,a3,a4,a5,a6,a7 in product([0,1],repeat=7):
#    t = [(1,a1,a2,a3),(0,1,0,a4),(a5,0,a6,a7)]
#    if len(set(t))==3:
#        for p in permutations('wxyz'):
#            if [f(**dict(zip(p,r)))for r in t]==[0,0,0]:
#                print(p)

#def f(w,x,y,z):
#    return not(x<=z)or(y==w)or y
#
#for a1,a2,a3,a4,a5,a6,a7 in product([0,1],repeat=7):
#    t = [(1,0,a1,a2),(a3,1,0,a4),(0,a5,a6,a7)]
#    if len(set(t))==3:
#        for p in permutations('wxyz'):
#            if [f(**dict(zip(p,r)))for r in t]==[0,0,0]:
#                print(p)

#
#def f(k,l,m,n):
#    return not(k<=m) and (k or n) or (l<=n)
#
#for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat=7):
#    t = [(1,a1,a2,0), (a3,a4,a5,1), (0,1,a6,a7)]
#    if len(set(t))==3:
#        for p in permutations('klmn'):
#            if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
#                print(p)
#
#def f(x,y,w,z):
#    return w and ((y<=x)<=z)
#
#for a1,a2,a3,a4,a5 in product([0,1], repeat=5):
#    t = [(a1,a2,0,1), (0,a3,a4,0), (0,1,a5,1)]
#    if len(set(t))==3:
#        for p in permutations('xywz'):
#            if [f(**dict(zip(p,r))) for r in t]==[1,1,0]:
#                print(p)
#
#def f(x,y,w,z):
#    return (z==(not x))<=((w<=(not y))and(y<=x))
#
#for a1,a2,a3,a4,a5 in product([0,1], repeat=5):
#    t = [(1,1,1,0), (a1,a2,0,0), (a3,0,a4,a5)]
#    if len(set(t))==3:
#        for p in permutations('xywz'):
#            if [f(**dict(zip(p,r))) for r in t]==[1,0,0]:
#                print(p)
#
#def f(x,y,w,z):
#    return (w or y) and (x <= (not z)) and (not w)
#
#d = set()
#for a1,a2,a3,a4,a5 in product([0,1], repeat=5):
#    t = [(a1,0,a2,0), (1,a3,a4,a5), (1,1,0,0)]
#    if len(set(t))==3:
#        for p in permutations('xywz'):
#            if [f(**dict(zip(p,r))) for r in t]==[1,1,1]:
#                d.add(p)
#print(d)


def f(x,y,w,z,u):
    return ((z<=w)and(y==(not x))) <= (u==(y or z))

for a1,a2,a3,a4,a5,a6,a7,a8 in product([0,1], repeat=8):
    t = [(0,a1,0,0,0), (0,a2,a3,0,0), (a4,0,0,0,a5), (0,0,a6,a7,a8)]
    if len(set(t))==4:
        for p in permutations('xywzu'):
            if [f(**dict(zip(p,r))) for r in t]==[0,0,0,0]:
                print(p)