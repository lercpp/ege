#k=0
#for s in open('9_1.txt'):
#    a=sorted([int(x) for x in s.split()])
#    if (min(a)+max(a))**2 > a[1]**2+a[2]**2+a[3]**2:
#        k+=1
#print(k)


#k=0
#for s in open('9_2.txt'):
#    a=sorted([int(x) for x in s.split()])
#    if max(a)*min(a)>=a[1]*a[2]:
#        k+=1
#print(k)

#k=0
#for s in open('9_3.txt'):
#    a=sorted([int(x)for x in s.split()])
#    a2=[x for x in a if a.count(x)>1]
#    if len(a2)==0 and max(a)**2<a[0]**2+a[1]**2:
#        k+=1
#print(k)

#k=0
#m=[]
#for s in open('9_4.txt'):
#    a=sorted([int(x) for x in s.split()])
#    k+=1
#    if len(set(a))==5 and 2*(min(a)+max(a))==3*(a[1]+a[2]+a[3]):
#        m.append(k)
#print(max(m))

#k=0
#for s in open('9_5.txt'):
#    a=sorted([int(x) for x in s.split()])
#    a1=[x for x in a if a.count(x)==1]
#    a3=[x for x in a if a.count(x)==3]
#    if (max(a)+min(a))**2>a[1]**2+a[2]**2+a[3]**2+a[4]**2 or len(a1)== 3 and len(a3)==3:
#        k+=1
#print(k)

#k=0
#for s in open('9_6.txt'):
#    a=sorted([int(x) for x in s.split()])
#    a1=[x for x in a if a.count(x)==1]
#    a2=[x for x in a if a.count(x)==2]
#    if len(a1)== 2 and len(a2)== 4 and max(a2)**2>a1[0]*a1[1]:
#        k+=1
#print(k)

#k=0
#for s in open('9_7.txt'):
#    a=sorted([int(x) for x in s.split()])
#    a1 = [x for x in a if a.count(x)==1]
#    a2 = [x for x in a if a.count(x)>1]
#     if len(a1)>0 and len(a2)>0 and sum(a1)/len(a1)<sum(a2)/len(a2):
#        k+=1
#print(k)

#k=0
#for s in open('9_8.txt'):
#    a=sorted([int(x) for x in s.split()])
#    a1 = [x for x in a if a.count(x)==1]
#    a2 = [x for x in a if a.count(x)==2]
#    if len(a1)==3 and len(a2)==4 and sum(a2)/len(a2)<sum(a)/len(a):
#        k+=1
#print(k)

#k=0
#for s in open('9_9.txt'):
#    a=sorted([int(x) for x in s.split()])
#    a2 = [x for x in a if a.count(x)==2]
#    a1 = [x for x in a if a.count(x)==1]
#    if len(a2)==6 and len(a1)==1 and (min(a2)+max(a2))/2<a1[0]:
#        k+=1
#print(k)

#k=0
#for s in open('9_10.txt'):
#    a=sorted([int(x) for x in s.split()])
#    a2 = [x for x in a if a.count(x)>1]
#    a1 = [x for x in a if x%2!=0]
#    if (len(a2)>0) + (len(a1)==3)==1:
#        k+=1
#print(k)

#m=[]
#for s in open('9_11.txt'):
#    a=[int(x) for x in s.split()]
#    a2 = [x for x in a if a.count(x)==3]
#    a1 = [x for x in a if a.count(x)==1]
#    if len(a2)==3 and len(a1)==4 and sum(a1)/len(a1)<=a2[0]:
#        m.append(sum(a))
#print(m[-1])

#k = 0
#m = []
#for s in open('9_12.txt'):
#    a = [int(x) for x in s.split()]
#    k += 1
#    a2 = [x for x in a if a.count(x)==2]
#    a1 = [x for x in a if a.count(x)==1]
#    if len(a2)==6 and len(a1)==2 and \
#       (max(a2)-min(a2))**2 > 2*(a1[0]**2 + a1[1]**2):
#        m.append(k)
#print(m[-1])

k = 0
m = []

for s in open('9_13.txt'):
    a = sorted([int(x) for x in s.split()])
    k += 1
    if (a[0]+a[3])**2 > a[1]**3+a[2]**3 and a[0]+a[3]!=a[1]+a[2]:
        m.append(k)
print(sum(m))
