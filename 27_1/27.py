#clA=[[],[]]

#for s in open('27_A.txt'):
#    x,y=[float(d) for d in s.replace(',','.').split()]
#    if y>8:clA[0].append([x,y])
#    else:clA[1].append([x,y])

#clB=[[] for i in range(5)]

#for s in open('27_B.txt'):
#    x,y=[float(d) for d in s.replace(',','.').split()]
#    if y>14:clB[0].append([x,y])
#    elif y>10:clB[1].append([x,y])
#    elif y>6:clB[2].append([x,y])
#    elif x>10:clB[3].append([x,y])
#    else:clB[4].append([x,y])

#from math import *
#def centr(cl):
#    m = []
#    for p in cl:
#        s = sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#centrA = [centr(x) for x in clA]
#sx = sum(x for x,y in centrA)/len(centrA)
#sy = sum(y for x,y in centrA)/len(centrA)

#print(int(sx*10000), int(sy*10000))

#centrB = [centr(x) for x in clB]
#sx = sum(x for x,y in centrB)/len(centrB)
#sy = sum(y for x,y in centrB)/len(centrB)

#print(int(sx*10000), int(sy*10000))

#clA=[[],[]]

#for s in open('27_A2.txt'):
#    x,y=[float(d) for d in s.replace(',','.').split()]
#    if x>2:clA[0].append([x,y])
#    else:clA[1].append([x,y])

#clB=[[],[],[]]

#for s in open('27_B2.txt'):
#    x,y=[float(d) for d in s.replace(',','.').split()]
#    if x>3.5:clB[0].append([x,y])
#    elif y>-2.5:clB[1].append([x,y])
#    else:clB[2].append([x,y])

#from math import *
#def dist(p1,p2):
#    x1,y1,x2,y2=*p1,*p2
#    return max(abs(x2-x1),abs(y2-y1))
#def centr(cl):
#    m=[]
#    for p in cl:
#        s=sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#centrA=[centr(x) for x in clA]
#sx=sum(x for x,y in centrA)/len(centrA)
#sy=sum(y for x,y in centrA)/len(centrA)

#print(int(abs(sx*10000)),int(abs(sy*10000)))

#centrB=[centr(x) for x in clB]
#sx=sum(x for x,y in centrB)/len(centrB)
#sy=sum(y for x,y in centrB)/len(centrB)

#print(int(abs(sx*10000)),int(abs(sy*10000)))


#A=[[],[]]

#for s in open('27_A3.txt'):
#    x,y=[float(d) for d in s.replace(',','.').split()]
#    if x>23:A[0].append([x,y])
#    else:A[1].append([x,y])

#B=[[],[],[]]

#for s in open('27_B3.txt'):
#    x,y=[float(d) for d in s.replace(',','.').split()]
#    if x<-10:B[0].append([x,y])
#    elif x>18:B[1].append([x,y])
#    else:B[2].append([x,y])

#def dist(p1,p2):
#    x1,y1,x2,y2 = *p1, *p2
#    return abs(x2-x1)+abs(y2-y1)

#def centr(cl):
#    m = []
#    for p in cl:
#        s = sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#clA = [[],[]]

#for s in open('27_A4.txt'):
#    x,y = [float(d) for d in s.split()]
#    if y>x+2:
#        clA[0].append([x,y])
#    else:
#        clA[1].append([x,y])

#clB = [[],[],[]]

#for s in open('27_B4.txt'):
#    x,y = [float(d) for d in s.split()]
#    if x>0 and y<x+3:
#        clB[0].append([x,y])
#    elif x<0 and y< -x/3+3:
#        clB[1].append([x,y])
#    else:
#        clB[2].append([x,y])

#from math import dist

#def centr(cl):
#    m = []
#    for p in cl:
#        s = sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#centrA = [centr(x) for x in clA]
#sx = sum(x for x,y in centrA)/len(centrA)
#sy = sum(y for x,y in centrA)/len(centrA)

#print(int(sx*100000), int(sy*100000))


#centrB = [centr(x) for x in clB]
#sx = sum(x for x,y in centrB)/len(centrB)
#sy = sum(y for x,y in centrB)/len(centrB)

#print(int(sx*100000), int(sy*100000))
#centrA = [centr(x) for x in A]
#sx = sum(x for x,y in centrA)/len(centrA)
#sy = sum(y for x,y in centrA)/len(centrA)

#print(int(abs(sx*1000)), int(abs(sy*1000)))

#centrB = [centr(x) for x in B]
#sx = sum(x for x,y in centrB)/len(centrB)
#sy = sum(y for x,y in centrB)/len(centrB)

#print(int(abs(sx*1000)), int(abs(sy*1000)))

#A=[[],[],[]]

#for s in open('27_A5.txt'):
#    x,y =[float(d) for d in s.replace(',','.').split()]
#    if x<5:A[0].append([x,y])
#    elif y>5:A[1].append([x,y])
#    else:A[2].append([x,y])

#B=[[],[],[],[]]

#for s in open('27_B5.txt'):
#    x,y=[float(d) for d in s.replace(',','.').split()]
#    if x>10 and y<10:B[0].append([x,y])
#    elif x>10 and y<x:B[1].append([x,y])
#    elif x<10:B[2].append([x,y])
#    elif y>x:B[3].append([x,y])
#    else: B[4].append([x,y])

#from math import *

#def centr(cl):
#    m=[]
#    for p in cl:
#        s=sum(dist(p,p1) for p1 in cl)
#        m.append([s,p])
#    return min(m)[1]

#cenA=[centr(x) for x in A]
#sx=sum(x for x,y in cenA)/len(cenA)
#sy=sum(y for x,y in cenA)/len(cenA)
#print(int(abs(sx*100000)),int(abs(sy*100000)))

#cenB=[centr(x) for x in B]
#sx=sum(x for x,y in cenB)/len(cenB)
#sy=sum(y for x,y in cenB)/len(cenB)        
#print(int(abs(sx*100000)),int(abs(sy*100000)))


#A=[[],[]]

#for s in open('27_A6.txt'):
#    x,y=[float(d) for d in s.replace(',','.').split()]
#    if y>2 and x>3 or y<-1 and x>7:pass
#    elif x>3 and y<-1 or x>5 and y<1 or x>6 and y<4:A[0].append([x,y])
#    else:A[1].append([x,y])

#B=[[],[],[]]

#for s in open('27_B6.txt'):
#    x,y=[float(d) for d in s.replace(',','.').split()]
#    if y>8 and x<4 or y>9 and x>10 and y<-2 and x>9:pass
#    elif  5<=x<=8 and 2<=y<=7:B[0].append([x,y])
#    elif  x<=8 and y<=7:B[1].append([x,y])
#    else:B[2].append([x,y])

#from math import *

#def centr(cl):
#    m=[]
#    for p in cl:
#        s=sum(dist(p,p1)for p1 in cl)
#        m.append([s,p])
#        return min(m)[1]

#centrA = [centr(x) for x in A]
#sx = sum(x for x,y in centrA)/len(centrA)
#sy = sum(y for x,y in centrA)/len(centrA)

#print(int(sx*100000), int(sy*100000))

#centrB = [centr(x) for x in B]
#sx = sum(x for x,y in centrB)/len(centrB)
#sy = sum(y for x,y in centrB)/len(centrB)

#print(int(sx*100000), int(sy*100000))


clA = [[],[]]

for s in open('27_A7.txt'):
    x,y = [float(d) for d in s.split()]
    if x>5 and y>7 or x<2 and y<-1:
        pass
    elif x>2 and 3<=y<=6 or x>6:
        clA[0].append([x,y])
    else:
        clA[1].append([x,y])

clB = [[],[],[]]
for s in open('27_B7.txt'):
    x,y = [float(d) for d in s.split()]
    if x<2 and y<2 or 7<x<8 and 4<y<6 or x>9 and y>9:
        pass
    elif x>4 and y<2 or x>7 and y<7.5:
        clB[0].append([x,y])
    elif x>4:
        clB[1].append([x,y])
    else:
        clB[2].append([x,y])

from math import dist

def centr(cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return min(m)[1]

centrA = [centr(x) for x in clA]
sx = sum(x for x,y in centrA)/len(centrA)
sy = sum(y for x,y in centrA)/len(centrA)

print(int(sx*100000), int(sy*100000))

centrB = [centr(x) for x in clB]
sx = sum(x for x,y in centrB)/len(centrB)
sy = sum(y for x,y in centrB)/len(centrB)

print(int(sx*100000), int(sy*100000))





























