#dots = []
#for s in open('27_b.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    dots.append([x,y])

#from math import *

#A = []
#while dots:
#    cl = [dots.pop()]
#    for p in cl:
#        sosed = [p1 for p1 in dots if dist(p,p1)<0.5]
#        cl.extend(sosed)
#        for p1 in sosed: dots.remove(p1)
#    A.append(cl)
#print([len(cl) for cl in A])

#def centr(cl):
#    m = []
#    for p in cl:
#        s = sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#x0,y0 = centr(A[0])
#x1,y1 = centr(A[1])
#px = (x0+x1)/2*10000
#py = (y0+y1)/2*10000
#print(int(px), int(py))

#x0,y0 = centr(A[0])
#x1,y1 = centr(A[1])
#x2,y2 = centr(A[2])
#px = (x0+x1+x2)/3*10000
#py = (y0+y1+y2)/3*10000
#print(int(px), int(py))


#dots=[]
#for s in open('27_b2.txt'):
#    x,y=[float(d) for d in s.replace(',','.').split()]
#    dots.append([x,y])
#from math import *
#A=[]
#while dots:
#    cl=[dots.pop()]
#    for p in cl:
#        sosed=[p1 for p1 in dots if dist(p,p1)<0.5]
#        cl.extend(sosed)
#        for p1 in sosed:dots.remove(p1)
#    A.append(cl)
#print([len(cl) for cl in A])

#def centr(cl):
#    m=[]
#    for p in cl:
#        s=sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#x0,y0=centr(A[0])
#x1,y1 = centr(A[1])
#px = (x0+x1)/2*100000
#py = (y0+y1)/2*100000
#print(int(px), int(py))

#x0,y0=centr(A[0])
#x1,y1=centr(A[1])
#x2,y2=centr(A[2])
#px = (x0+x1+x2)/3*100000
#py = (y0+y1+y2)/3*100000
#print(int(px), int(py))


#dots=[]
#for s in open('27_b3.txt'):
#    x,y=[float(d) for d in s.replace(',','.').split()]
#    dots.append([x,y])
#from math import *

#A=[]
#while dots:
#    cl=[dots.pop()]
#    for p in cl:
#        sosed=[p1 for p1 in dots if dist(p,p1)<0.6]
#        cl.extend(sosed)
#        for p1 in sosed:dots.remove(p1)
#    A.append(cl)
#print([len(cl) for cl in A])
#A=[cl for cl in A if len(cl)>10]

#def centr(cl):
#    m=[]
#    for p in cl:
#        s=sum(dist(p,p1)for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#x0,y0 = centr(A[0])
#x1,y1 = centr(A[1])
#px = (x0+x1)/2*100000
#py = (y0+y1)/2*100000
#print(int(abs(px)), int(abs(py)))

#x0,y0 = centr(A[0])
#x1,y1 = centr(A[1])
#x2,y2 = centr(A[2])
#px = (x0+x1+x2)/3*100000
#py = (y0+y1+y2)/3*100000
#print(int(abs(px)), int(abs(py)))

#dots=[]
#for s in open('27_B4.txt'):
#    x,y=[float(d) for d in s.replace(',','.').split()]
#    dots.append([x,y])
#from math import *
#A=[]
#while dots:
#    cl=[dots.pop()]
#    for p in cl:
#        sosed=[p1 for p1 in dots if dist(p,p1)<1]
#        cl.extend(sosed)
#        for p1 in sosed:dots.remove(p1)
#    A.append(cl)
#print([len(cl) for cl in A])
#A=[cl for cl in A if len(cl)>10]
#def centr(cl):
#    m=[]
#    for p in cl:
#        s=sum(dist(p,p1)for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#x0,y0 = centr(A[0])
#x1,y1 = centr(A[1])
#x2,y2 = centr(A[2])
#px = (x0+x1+x2)/3*100000
#py = (y0+y1+y2)/3*100000
#print(int(abs(px)), int(abs(py)))

#dots = []
#for s in open('27_B5.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    dots.append([x,y])

#from math import *

#A = []
#while dots:
#    cl = [dots.pop()]
#    for p in cl:
#        sosed = [p1 for p1 in dots if dist(p,p1)<1]
#        cl.extend(sosed)
#        for p1 in sosed: dots.remove(p1)
#    A.append(cl)

#print([len(cl) for cl in A])

#def centr(cl):
#    dx=[x for x,y in cl]
#    dy =[y for x,y in cl]
#    return [sum(dx)/len(dx),sum(dy)/len(dy)]

#x0,y0 = centr(A[0])
#x1,y1 = centr(A[1])
#x2,y2 = centr(A[2])
#px = (x0+x1+x2)/3*10000
#py = (y0+y1+y2)/3*10000
#print(int(px), int(py))


#dots = []
#for s in open('27_B6.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    dots.append([x,y])

#from math import *

#A = []
#while dots:
#    cl = [dots.pop()]
#    for p in cl:
#        sosed = [p1 for p1 in dots if dist(p,p1)<1]
#        cl.extend(sosed)
#        for p1 in sosed: dots.remove(p1)
#    A.append(cl)

#print([len(cl) for cl in A])
#def centr(cl):
#    m = []
#    for p in cl:
#        s = sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#x0,y0 = centr(A[0])
#x1,y1 = centr(A[1])
#x2,y2=centr(A[2])
#print(int(x2*10000),int(y1*10000))

#dots = []
#for s in open('27_B7.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    dots.append([x,y])

#from math import *

#A = []
#while dots:
#    cl = [dots.pop()]
#    for p in cl:
#        sosed = [p1 for p1 in dots if dist(p,p1)<1]
#        cl.extend(sosed)
#        for p1 in sosed: dots.remove(p1)
#    A.append(cl)

#print([len(cl) for cl in A])
#def centr(cl):
#    m = []
#    for p in cl:
#        s = sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]


#def acentr(cl):
#    m = []
#    for p in cl:
#        s = sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return max(m)[1]
#
#x0,y0 = centr(A[0])
#x1,y1 = centr(A[1])
#x2,y2 = centr(A[2])
#px=(x0+x1+x2)/3*
#x0,y0 = acentr(A[0])
#x1,y1 = acentr(A[1])
#x2,y2 = acentr(A[2])
#sy = (y0+y1+y2)/3*10000
#print(int(abs(px)), int(abs(sy)))


dots = []
for s in open('27_B8.txt'):
    x,y = [float(d) for d in s.replace(',','.').split()]
    dots.append([x,y])

from math import *

A = []
while dots:
    cl = [dots.pop()]
    for p in cl:
        sosed = [p1 for p1 in dots if dist(p,p1)<0.2]
        cl.extend(sosed)
        for p1 in sosed: dots.remove(p1)
    A.append(cl)

print([len(cl) for cl in A])
A = [cl for cl in A if len(cl)>10]

def centr(cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return min(m)[1]

x0,y0 = centr(A[0])
x1,y1 = centr(A[1])
print(int(min(x0,x1)*10000), int(abs(min(y0,y1)*10000)))
