#a = [int(x) for x in open('17_1.txt')]

#m = max(x for x in a if abs(x)%1000==121)

#def ch(x):
#    return 1000<=abs(x)<10000 and x%2==0

#ans = []

#for x,y,z in zip(a,a[1:],a[2:]):
#    if ch(x)+ch(y)+ch(z)<=1 and x+y+z<=m:
#        ans.append(x+y+z)
#print(len(ans), max(ans))

#a = [int(x) for x in open('17_2.txt')]

#m = max(x for x in a if x%100==17)

#def ch(x):
#    return 1000<=x<=10000

#ans = []

#for x,y,z in zip(a,a[1:],a[2:]):
#    if ch(x)+ch(y)+ch(z)==2 and (x%5==0 or y%5==0 or z%5==0) and x+y+z>m:
#        ans.append(x+y+z)
#print(len(ans),max(ans))

#a = [int(x) for x in open('17_3.txt')]

#m = max(x for x in a if hex(x)[2:][-2:]=='0f')

#ans = []

#for x,y in zip(a,a[1:]):
#    if (x%7==0)+(y%7==0)==1 and (x+y)%m==0:
#        ans.append(x+y)
#print(len(ans),max(ans))

#a = [int(x) for x in open('17_3.txt')]

#a = [int(x) for x in open('17_7.txt')]

#def ch(x):
#    return x>0 and x%10==9

#ans = []

#for x,y,z in zip(a,a[1:],a[2:]):
#    if not ch(x) and ch(y) and not ch(z):
#        ans.append(x+y+z)
#print(len(ans),max(ans))

#m = max(x for x in a if hex(x)[2:][-2:]=='0f')

#ans = []

#for x,y in zip(a,a[1:]):
#    if (x%7==0)+(y%7==0)==1 and (x+y)%m==0:
#        ans.append(x+y)
#print(len(ans),max(ans))

#a = [int(x) for x in open('17_4.txt')]

#m = max(x for x in a if abs(x)%100==25)

#def sm(x):
#    s = sum(map(int,str(abs(x))))
#    return s%2!=0

#ans = []

#for x,y,z in zip(a,a[1:],a[2:]):
#    if sm(x)+sm(y)+sm(z)>=2 and x+y+z<=m:
#        ans.append(x+y+z)
#print(len(ans),max(ans))


#from itertools import *
#a = [int(x) for x in open('17_5.txt')]

#ans = []

#for x,y in combinations(a,2):
#    if (x+y)%120==0:
#        ans.append(x+y)
#print(len(ans),max(ans))

#from itertools import *
#a = [int(x) for x in open('17_6.txt')]

#ans = []

#for x,y in combinations(a,2):
#    if (x-y)%36==0 and (x%13==0 or y%13==0):
#        ans.append(abs(x-y))
#print(len(ans),max(ans))

#a = [int(x) for x in open('17_8.txt')]

#m = max(x for x in a if 10<=abs(x)<100)

#ans1 = []

#for x,y,w,z in zip(a,a[1:],a[2:],a[3:]):
#    if abs(x)%10==abs(w)%10==abs(y)%10==abs(z)%10:
#        ans1.append(x+y+w+z)
#A = max(ans1)

#ans = []

#for x,y,w,z,q in zip(a,a[1:],a[2:],a[3:],a[4:]):
#    if (x<A)+(y<A)+(w<A)+(z<A)+(q<A)==1 and (x+y+w+z+q)%m==0:
#        ans.append(x+y+w+z+q)
#print(len(ans),min(ans))

#a = [int(x) for x in open('17_9.txt')]

#ans = []

#for x,y in zip(a,a[1:]):
#    if 50<=abs(x)+abs(y)<=200:
#        ans.append(min(x,y))
#print(len(ans), min(ans))


a = [int(x) for x in open('17_10.txt')]

m = max(a)

ans = []

for x,y,z in zip(a,a[1:],a[2:]):
    if x+y+z<=m:
        ans.append(x)
        ans.append(y)
        ans.append(z)
print(len(ans)//3, max(ans)+min(ans))
