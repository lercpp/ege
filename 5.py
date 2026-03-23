m = []
#for n in range(1,500):
#    b = f'{n:b}'
#    b = b + b[-1]
#    if b.count('1')%2==0:
#        b = b + '0'
#    else:
#        b = b + '1'
#    if b.count('1')%2==0:
#        b = b + '0'
#    else:
#        b = b + '1'
#    r = int(b,2)
#    if r>114:
#        m.append(r)
#print(min(m))


#for n in range(1,100):
#    b = f'{n:b}'
#    if b.count('1')%2==0:
#        b = b + '0'
#    else:
#        b = b + '1'
#    if b.count('1')%2==0:
#        b = b + '0'
#    else:
#        b = b + '1'
#    r = int(b,2)
#    if 64<=r<72:
#        print(n)
  
#for n in range(1,100):
#    b=f'{n:b}'
#    if n%2==0:
#        b= b+b[:2]
#
#    else:
#        b= '1'+b+'1'

#    r=int(b,2)
#    if r>130:
#        m.append(r)

#print(min(m))

#for n in range(1,100):
#    b=f'{n:b}'
#    if n%2!=0:
#        b='10'+b+'11'

#    else:
#        b='1'+b+'00'
#
#    r=int(b,2)
#    if r>1023:
#        m.append(r)
#print(min(m))

#for n in range(1,100):
#    b = f'{n:b}'
#    if b.count('1')>b.count('0'):
#        b=b+'0'

#    else:
#        b='11'+b
#    if b.count('1')>b.count('0'):
#        b=b+'0'

#    else:
#        b='11'+b

#    r=int(b,2)
#    if r>500:
#        m.append(n)
#print(min(m))

#for n in range(1,100):
#    b=f'{n:b}'
#    if b.count('1')==b.count('0'):
#        b=b+b[-1]
#    elif b.count('1')<b.count('0'):
#        b = b + '1'
#    else:
#        b = b + '0'
#
#    if b.count('1')==b.count('0'):
#        b=b+b[-1]
#    elif b.count('1')<b.count('0'):
#        b = b + '1'
#    else:
#        b = b + '0'
#
#    if b.count('1')==b.count('0'):
#        b=b+b[-1]
#    elif b.count('1')<b.count('0'):
#        b = b + '1'
#    else:
#        b = b + '0'
#
#    r = int(b,2)
#    if r%4==0 and r%8!=0:
#        print(n)
#
#for n in range(1,16):
#    b=f'{n:b}'
#    if b.count('1')%2==0:
#        b = '10' + b[2:] + '1'
#    else:
#        b = '11' + b[2:] + '0'
#    r = int(b,2)
#    m.append(r)
#print(max(m))


#for n in range(1,100):
#    b = f'{n:b}'
#    if b.count('1')%2==0:
#        b = b + '0'
#        b = '1' + b[2:]
#    else:
#        b = b + '1'
#        b = '11' + b[2:]
#    r = int(b,2)
#    if r>49:
#        m.append([r,n])
#print(min(m))

#def s3(x):
#    if x==0: return '0'
#    s = ''
#    while x>0:
#        s = str(x%3)+s
#        x//=3
#    return s
#
#for n in range(1,100):
#    b = s3(n)
#    if n%3==0:
#        b = b + b[-2]+b[-1]
#    else:
#        b = b + s3(n%3*5)
#    r = int(b,3)
#    if r>150:
#        m.append(r)
#print(min(m))
#

#def s3(x):
#    if x==0:return'0'
#    s=''
#    while x>0:
#        s=str(x%3)+s
#        x//=3
#
#    return s
#
#for n in range(4,100):
#    b = s3(n)
#    if b[-2]+b[-1] == '10':
#        b = '2'+b
#    else:
#        b = '1'+b
#    r = int(b,3)
#    if r>130:
#        m.append(n)
#print(min(m))


#def s3(x):
#    if x==0: return '0'
#    s = ''
#    while x>0:
#        s = str(x%3)+s
#        x//=3
#    return s
#
#m = []
#for n in range(1,100):
#    b = s3(n)
#    if sum(map(int,b))%3==0:
#        b = '20'+b
#    else:
#        b = '10'+b
#    r = int(b,3)
#    if r<100:
#        m.append(n)
#print(max(m))


#def s4(x):
#    if x==0: return '0'
#    s = ''
#    while x>0:
#        s = str(x%4)+s
#        x//=4
#    return s
#
#m = []
#for n in range(1,300):
#    b = s4(n)
#    if n%4==0:
#        b = b+b[0]+b[1]
#    else:
#        b = b + s4(n%4*4)
#    r = int(b,4)
#    if r>291:
#        m.append(r)
#print(min(m))
#

#from string import *
#def s12(x):
#    if x==0: return '0'
#    s = ''
#    while x>0:
#        s = printable[x%12]+s
#        x//=12
#    return s

#m = []
#for n in range(1,2000):
#    b = s12(n)
#    if n%3==0:
#        b = '1'+b+'B'
#    else:
#        b = '2'+b+'0'
#    r = int(b,12)
#    if r<1996:
#        m.append(r)
#print(max(m))


for n in range(110):
    b = f'{n:08b}'
    b = b[:2] + b[-2:]
    r = int(b,2)
    if r==7:
        print(n)

d = set()
for n in range(10,1001):
    b = f'{n:b}'
    b = b[1:]
    r = int(b,2)
    r = n - r
    d.add(r)
print(d)

for n in range(1,100):
    b = f'{n:b}'
    b1 = b[1:]
    b1 = b1.replace('0','2').replace('1','0').replace('2','1')
    b = b[0]+b1
    r = int(b,2)
    r = r+n
    if n%2!=0 and r>99:
        print(n)

m = []
for n in range(1,200):
    b = f'{n:b}'
    b = b.replace('0','2').replace('1','3')
    b = b.replace('2','01').replace('3','10')
    r = int(b,2)
    if r<256:
        m.append(r)
print(max(m))

def cc6(x):
    s = ''
    while x>0:
        s = str(x%6)+s
        x = x//6
    return s

for n in range(1,100000):
    b6 = cc6(n)
    b6 = b6 + b6[-1]
    r = int(b6,6)
    r = f'{r:b}'
    r = r.count('1')
    if r==18:
        print(n)


for n in range(2,10000):
    b = f'{n:b}'
    k1 = b[1::2].count('1')
    k2 = b[::2].count('0')
    r = abs(k2-k1)
    if r==5:
        print(n)

for n in range(1000,10000):
    d = [int(x) for x in str(n)]
    a1 = d[0]*d[1]
    a2 = d[2]*d[3]
    if a1<a2:
        r = str(a1)+str(a2)
    else:
        r = str(a2)+str(a1)
    if r=='1214':
        print(n)

for n in range(100,1000):
    d = [int(x) for x in str(n)]
    a1 = d[0]*d[1]
    a2 = d[1]*d[2]
    if a1>a2:
        r = str(a1)+str(a2)
    else:
        r = str(a2)+str(a1)
    if r=='240':
        print(n)

for n in range(800,901):
    s = str(n)
    a = [s[0]+s[1],s[0]+s[2],s[1]+s[0],s[1]+s[2],s[2]+s[0],s[2]+s[1]]
    a = [int(x) for x in a]
    a = [x for x in a if x>=10]
    r = max(a)-min(a)
    if r==30:
        print(n)

for n in range(100,1000):
    s = str(n)
    a = [int(s[0]+s[1]), int(s[1]+s[2])]
    r = max(a)+min(a)
    if r==137:
        print(n)




        




        
