#a = 4**644+4**322+16**35-64**3
#
#k=0
#
#while a>0:
#    if a%4 == 3:
#        k+=1
#
#    a=a//4
#
#print(k)


#a = 6*512**180+7*64**181+3*8**184+5*8**125-65
#
#k = 0
#
#while a>0:
#
#    if a%64 == 0 : k+=1
#
#    a=a//64
#print(k)

#a = 2197**50-169**35-26
#
#k=0
#
#while a>0:
#
#    if a%13 == 12: k+=1
#
#    a=a//13
#print(k)


#a = 3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 - 4*3**2024 - 2029
#
#k = 0
#
#while a>0:
#    if a%27>9:
#        k += 1
#    a = a//27
#print(k)

#a=5*216**3031+4*36**3042-3*6**3053-3064
#
#k=0
#
#while a>0:
#    k+=a%6
#
#    a=a//6
#print(k)

#a = 5*216**1156-4*36**1147+6**1153-875
#
#k = 0
#k1=0
#
#while a>0:
#    if a%6 == 5:k+=1
#    if a%6 == 0:k1+=1
#
#    a=a//6
#print(k-k1)


#for x in range(5555,1,-1):
#    a = 5**150+5**135-x
#    k = 0
#    while a>0:
#        if a%5==4:
#            k += 1
#        a = a//5
#    if k==134:
#        print(x)

#for x in range(1,1000):
#    a = 9**1942 + 9*6**971 + 214 - x
#    k8 = 0
#    k2 = 0
#    while a>0:
#        if a%9==8:
#            k8+=1
#        if a%9==2:
#            k2+=1
#        a = a//9
#    if k8-k2==471:
#        print(x)

#for x in range(1,100):
#    a = 81**20 - 9**x + 50
#    s = 0
#    while a>0:
#        s += a%9
#        a = a//9
#    if s==138:
#       print(x)
#
#for x in range(1,100):
#    a = 81**20 - 9**x + 50
#    k=0
#
#    while a>0:
#        k+=a%9
#        a=a//9
#
#        if k == 138:
#            print(x)
#
#for x in range(2025,2,-1):
#    a = 5**2025 + 5**200 - x
#    k=0
#
#    while a>0:
#        if a%5 == 4: k +=1
#        a=a//5
#    if k == 199: 
#        print(x)
#        break

#def oke(x,n):
#    a = []
#    while x>0:
#        a = [x%n]+a
#        x = x//n
#    return a

#for n in range(2,20):
#    print(n,oke(41,n),oke(131,n))
#
#def cc(x,n):
#   a = []
#   while x>0:
#       a = [x%n]+a
#       x = x//n
#   return a
#
#for n in range(2,50):
#    print(n,cc(n,6),cc(n,5),cc(n,11))
#
#def cc(x,n):
#   a = []
#   while x>0:
#       a = [x%n]+a
#       x = x//n
#   return a
#
#for n in range(125,300):
#    print(n,cc(n,5),cc(n,3),f'{n:x}')
#


#from string import *
#
#for x in printable[:19]:
#    a = int(f'98897{x}21',19)+int(f'2{x}923',19)
#    if a%18==0:
#        print(x,a//18)

#from string import *
#
#for x in printable[:29]:
#    a = int(f'923{x}874',29) + int(f'524{x}6152',29)
#    if a%28==0:
#        print(x,a//28)

#from string import *
#
#for x in printable[:24]:
#    a = int(f'4M{x}F',24) + int(f'265AFDN{x}',24) + int(f'N4{x}931B3L',24)+ int(f'NG{x}4F',24)+ int(f'FKJB5{x}IK',24)
#    if a%23==0:
#        print(a//23)

#
#from string import *
#
#for x in printable[:21]:
#    for y in printable[:21]:
#        a = int(f'32{y}{x}a',21)+int(f'16{y}18',21)
#        if a%12==0:
#            print(x,y,a//12)

#def to10(a,n):
#    a = a[::-1]
#    s=0
#
#    for i in range(len(a)):
#        s= s + a[i]*n**i
#    return s
#
#for x in range(37):
#    a = to10([9,8,x,3,1],37)+to10([1,x,9,2,4],37)
#    if a%21 == 0:
#        print(x,a//21)
#
#def to10(a,n):
#    a=a[::-1]
#    s=0
#    for i in range(len(a)):
#        s = s+a[i]*n**i
#    return s
#
#for x in range(68):
#    a=to10([1,2,3,x,5],68)+to10([1,x,2,3,3],68)
#    if a%12==0:
#        print(x,a//12)
#
#def to10(a,n):
#    a=a[::-1]
#    s=0
#    for i in range(len(a)):
#        s=s+a[i]*n**i
#    return s
#
#for x in range(37):
#    a = to10([12,5,9,x,11,10,9,8,15],37)*to10([14,3,x,5,13,10,9,12,6],37)
#    if a%36==0:
#        print(x,to10([2,x,1],37))

#
#for x in range(4,37):
#    if int('21',x)*int('13',x)==int('313',x):
#        print(x)
#
#
#for x in range(5,36):
#    if int('132',x)+ int('13',8)==int('124',x+1):
#        print(x)
#
#
#for x in range(2,10000):
#    if x**2+x==39800:
#        print(x)
#
#for x in range(8,37):
#    a= int('11353712',x)+int('135421',x)
#    if a%31==0:
#        print(x,a//31)
#
#
#def to10(a,n):
#    a = a[::-1]
#    s = 0
#    for i in range(len(a)):
#        s = s + a[i]*n**i
#    return s
#
#for p in range(7,50):
#    for x in range(1,p):
#        for y in range(1,p):
#            for z in range(0,p):
#
#                if to10([y,4,y],p)+to10([y,6,5],p)==to10([x,z,3,3],p):
#                    print(to10([x,y,z],p))


def to10(a,n):
    a = a[::-1]
    s = 0
    for i in range(len(a)):
        s = s + a[i]*n**i
    return s

for p in range(5,50):
    for q in range(5,50):
        if to10([2,4,3,5,1],p) == to10([1,4,3,2,5],q):
            print(p, q, to10([1,4,3,2,5],q))