#A = [[],[]]

#for s in open('27A.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    if x>15 or y>25: pass
#    elif y>15: A[0].append([x,y])
#    else: A[1].append([x,y])

#B = [[],[],[]]
#for s in open('27B.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    if x<-2 or x>0: pass
#    elif y>5: B[0].append([x,y])
#    elif x<-1: B[1].append([x,y])
#    else: B[2].append([x,y])

#from math import *

#def centr(cl):
#    m = []
#    for p in cl:
#        s = sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#x0,y0 = centr(A[0])
#x1,y1 = centr(A[1])

#print(int(abs(min(x0,x1)*10000)),int(abs(min(y0,y1)*10000)))

#print([len(cl) for cl in B])

#A = [[],[]]

#for s in open('27A_2.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    if x<0 or y<0: pass
#    elif y>15: A[0].append([x,y])
#    else: A[1].append([x,y])

#B = [[],[],[]]
#for s in open('27B_2.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    if x<-2 or x>0: pass
#    elif y>5: B[0].append([x,y])
#    elif x<-1: B[1].append([x,y])
#    else: B[2].append([x,y])

#from math import *

#def centr(cl):
#    m = []
#    for p in cl:
#        s = sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#x0,y0 = centr(A[0])
#x1,y1 = centr(A[1])

#px = abs(x0-x1)*10000
#py = abs(y0-y1)*10000
#print(int(abs(px)), int(abs(py)))

#p0 = centr(B[0])
#p1 = centr(B[1])
#p2 = centr(B[2])
#print([len(cl) for cl in B])
#q1 = dist(p0,p1)
#q2 = max([dist(p0,p) for p in B[0]]+[dist(p1,p) for p in B[1]]+\
#     [dist(p2,p) for p in B[2]])

#print(int(q1*10000), int(q2*10000))

#A = [[],[]]

#for s in open('27A_3.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    if x>15: pass
#    elif y>10: A[0].append([x,y])
#    else: A[1].append([x,y])

#B = [[],[],[]]
#for s in open('27B_3.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    if x<-2 or x>0: pass
#    elif y>5: B[0].append([x,y])
#    elif x<-1: B[1].append([x,y])
#    else: B[2].append([x,y])

#from math import *

#def centr(cl):
#    m = []
#    for p in cl:
#        s = sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#p0 = centr(A[0])
#p1 = centr(A[1])

#d = [dist(p0,p) for p in A[1]]+[dist(p1,p) for p in A[0]]
#p1 = min(d)*10000
#p2 = max(d)*10000
#print(int(p1), int(p2))

#p0 = centr(B[0])
#p1 = centr(B[1])
#p2 = centr(B[2])
#d = [dist(p0,p1), dist(p0,p2), dist(p1,p2)]
#q1 = min(d)*10000
#q2 = max(d)*10000
#print(int(q1), int(q2))

#A = [[],[]]

#for s in open('27A_4.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    if y<-20: pass
#    elif x>15: A[0].append([x,y])
#    else: A[1].append([x,y])

#B = [[],[],[]]
#for s in open('27B_4.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    if x<5 or x>30: pass
#    elif y>12: B[0].append([x,y])
#    elif x<16: B[1].append([x,y])
#    else: B[2].append([x,y])

#from math import *

#def centr(cl):
#    m = []
#    for p in cl:
#        s = sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#x0,y0 = centr(A[0])
#x1,y1 = centr(A[1])
#px = min(x0,x1)*10000
#py = min(y0,y1)*10000
#print(int(abs(px)), int(abs(py)))

#print([len(cl) for cl in B])

#p0 = centr(B[0])
#d = [dist(p0,p) for p in B[0] if p!=p0]
#q1 = sum(d)/len(d)*10000

#p2 = centr(B[2])
#d = [dist(p2,p) for p in B[2] if p!=p2]
#q2 = sum(d)/len(d)*10000
#print(int(q1), int(q2))

#A = [[],[]]

#for s in open('27A_5.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    if x<0: A[0].append([x,y])
#    else: A[1].append([x,y])

#B = [[],[],[]]
#for s in open('27B_5.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    if x<-40: B[0].append([x,y])
#    elif y<-20: B[1].append([x,y])
#    elif y>10: B[2].append([x,y])

#from math import *

#def centr(cl):
#    m = []
#    for p in cl:
#        s = sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#x0,y0 = centr(A[0])
#x1,y1 = centr(A[1])
#sx = (x0+x1)*10000
#sy = (y0+y1)*10000
#print(int(abs(sx)), int(abs(sy)))

#print([len(cl) for cl in B])

#q1 = max(x for x,y in B[2])*10000
#q2 = max(y for x,y in B[1])*10000

#print(int(abs(q1)), int(abs(q2)))

#A = [[],[]]

#for s in open('27A_6.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    if x>2: A[0].append([x,y])
#    else: A[1].append([x,y])

#B = [[],[],[]]
#for s in open('27B_6.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    if x>3: B[0].append([x,y])
#    elif y>-2.5: B[1].append([x,y])
#    else: B[2].append([x,y])

#from math import *

#def centr(cl):
#    m = []
#    for p in cl:
#        s = sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#p0 = centr(A[0])
#p1 = centr(A[1])
#px = min(dist(p0,(2.1, 5)), dist(p1,(2.1, 5)))*10000
#x0,y0 = p0
#x1,y1 = p1

#py = dist( (2.1,5), ((x0+x1)/2, (y0+y1)/2) )*10000

#print(int(px), int(py))

#print([len(cl) for cl in B])

#p1 = centr(B[1])
#q1 = len([p for p in B[0]+B[1]+B[2] if dist(p1,p)<=5])
#p2 = centr(B[2])
#q2 = len([p for p in B[0]+B[1]+B[2] if dist(p2,p)>5])
#print(q1,q2)


#A = [[],[]]

#for s in open('27A_7.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    if x<0 or x>10: pass
#    elif y>10: A[0].append([x,y])
#    else: A[1].append([x,y])

#B = [[],[],[]]
#for s in open('27B_7.txt'):
#    x,y = [float(d) for d in s.replace(',','.').split()]
#    if x<0 or x>40 or y<0: pass
#    elif x>24: B[0].append([x,y])
#    elif y>16: B[1].append([x,y])
#    else: B[2].append([x,y])

#from math import *

#def acentr(cl):
#    m = []
#    for p in cl:
#        s = sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return max(m)[1]

#x0,y0 = acentr(A[0])
#x1,y1 = acentr(A[1])
#px = max(x0,x1)*10000
#py = max(y0,y1)*10000
#print(int(abs(px)), int(abs(py)))

#p0 = acentr(B[0])
#p1 = acentr(B[1])
#p2 = acentr(B[2])
#print([len(cl) for cl in B])
#q1 = dist(p0,p1)*10000
#q2 = max([dist(p0,p) for p in B[0]]+[dist(p1,p) for p in B[1]]+\
#         [dist(p2,p) for p in B[2]])*10000
#print(int(q1), int(q2))

A = [[],[]]

for s in open('27A_8.txt'):
    x,y = [float(d) for d in s.replace(',','.').split()]
    if x>6: A[0].append([x,y])
    else: A[1].append([x,y])

B = [[],[],[]]
for s in open('27B_8.txt'):
    x,y = [float(d) for d in s.replace(',','.').split()]
    if y>5: B[0].append([x,y])
    elif x<2: B[1].append([x,y])
    else: B[2].append([x,y])
s
from math import *

def krai(cl1,cl2):
    m = []
    for p1 in cl1:
        for p2 in cl2:
            m.append([dist(p1,p2),[p1,p2]])
    return min(m)[1]

d = krai(A[0],A[1])
px = sum(x for x,y in d)/2*10000
py = sum(y for x,y in d)/2*10000
print(int(px), int(py))

d = krai(B[0],B[1])+krai(B[1],B[2])+krai(B[0],B[2])
px = sum(x for x,y in d)/6*10000
py = sum(y for x,y in d)/6*10000
print(int(px), int(py))
