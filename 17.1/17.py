#a=[int(x) for x in open('17.1.txt')]

#n=[]
#for x,y in zip(a,a[1:]):
#    if (x%7==0 or y%7==0) and (abs(x)%10==3 or abs(y)%10==3):
#        n.append(x+y)
#print(len(n),min(n))


#a=[int(x) for x in open('17.2.txt')]
#m = min(x for x in a if x>0 and x%41==0)
#n=[]
#for x,y in zip(a,a[1:]):
#    if x!=y and abs(x-y)%m==0:
#        n.append(x+y)
#print(len(n),max(n))


#a=[int(x) for x in open('17.3.txt')]

#m=min(a)
#n=[]

#for x,y in zip(a,a[1:]):
#    if x%43==m and y%43==m:
#        n.append(abs(x-y))
#print(len(n),max(n))

#a=[int(x) for x in open('17_4.txt')]
#m=min(x for x in a if 100<=x<1000 and x%10==5)
#n=[]

#for x,y in zip(a,a[1:]):
#    if (100<=x<1000 or 100<=y<1000) and (x+y)%m==0:
#        n.append(x+y)
#print(len(n),max(n))


#a=[int(x) for x in open('17_5.txt')]
#m=len([x for x in a if x%32==0])
#n=[]

#for x,y in zip(a,a[1:]):
#    if (x<0 or y<0) and (x+y)<m:
#        n.append(x+y)
#print(len(n),max(n))

#a=[int(x) for x in open('17_6.txt')]
#m=min(x for x in a if x%52==0)
#n=[]

#for x,y,z in zip(a,a[1:],a[2:]):
#    if (x%113+y%113+z%113)==m:
#        n.append(x+y+z)
#print(len(n),max(n))


#a=[int(x) for x in open('17_7.txt')]
#n=[]
#m=max(x for x in a if abs(x)%10==9)

#for x,y in zip(a,a[1:]):
#    if (abs(x)%10==9)+(abs(y)%10==9)==1 and x**2+y**2<m**2:
#        n.append(x**2+y**2)
#print(len(n),min(n))

#a=[int(x) for x in open('17_8.txt')]
#n=[]
#m=min(x for x in a if x%123==0)

#for x,y in zip(a,a[1:]):
#    if (x%2023>=m)+(y%2023>=m)==1:
#        n.append(x+y)
#print(len(n),max(n))

#a=[int(x) for x in open('17_9.txt')]
#n=[]
#m=max(x for x in a if x%100==13)

#for x,y,z in zip(a,a[1:],a[2:]):
#    if (100<=x<1000)+(100<=y<1000)+(100<=z<1000)==2 and (x+y+z)<=m:
#        n.append(x+y+z)
#print(len(n),max(n))

#a=[int(x) for x in open('17_10.txt')]
#n=[]
#m=max(x for x in a if abs(x)%100==25)

#for x,y,z in zip(a,a[1:],a[2:]):
#    if (1000<=abs(x)<10000)+(1000<=abs(y)<10000)+(1000<=abs(z)<10000)<=2 and (x+y+z)<=m:
#        n.append(x+y+z)
#print(len(n),max(n))

a=[int(x)for x in open('17_11.txt')]
n=[]
a1 = [x for x in a if x%2!=0]
m = sum(a1)/len(a1)

for x,y in zip(a,a[1:]):
   if (abs(x)%100==11)+(abs(y)%100==11)==1 and (x+y)>=m:
       n.append(x+y)
print(len(n),max(n))
       
