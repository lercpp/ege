#prog = {
#    (' ',0): (' ',-1,1),
#    (' ',1): (' ',2,1),
#    ('1',1): ('0',-1,1),
#    ('0',1): ('1',-1,1)
#}

#def mt(s):
#    s = list(' '+s+' ')
#    i = -1
#    q = 0
#    while True:
#        cmd = prog[(s[i],q)]
#        s[i] = cmd[0]
#        if cmd[1]==2: break
#        i += cmd[1]
#        q = cmd[2]
#    return ''.join(s)

#res = mt(f'{135:b}')
#print(res, int(res,2))

#p={
#    (' ',0): (' ',-1,1),
#    (' ',2): (' ',2,2),
#    (' ',3): (' ',2,3),
#    ('1',1): ('1',-1,3),
#    ('1',2): ('0',-1,1),
#    ('1',3): ('1',-1,2),
#    ('0',1): ('0',-1,3),
#    ('0',2): ('1',-1,3),
#    ('0',3): ('1',-1,2)
#}

#def mt(s):
#    s=list(' '+s+' ')
#    i=-1
#    q=0
#    while True:
#        cmd=p[(s[i],q)]
#        s[i] = cmd[0]
#        if cmd[1]==2:break
#        i+=cmd[1]
#        q=cmd[2]
#    return ''.join(s)
#res =mt(221*'1')
#print(res.count('1'))


#p={
#    (' ',0):(' ',-1,1),
#    (' ',1):(' ',2,1),
#    (' ',2):(' ',2,2),
#    (' ',3):(' ',2,3),
#    ('1',1):('0',-1,3),
#    ('1',2):('0',-1,1),
#    ('1',3):('1',-1,2),
#    ('0',1):('1',-1,2),
#    ('0',2):('0',-1,3),
#    ('0',3):('1',-1,1)
#}

#def mt(s):
#    s=list(' '+s+' ')
#    i=-1
#    q=0
#    while True:
#        cmd = p[(s[i],q)]
#        s[i]=cmd[0]
#        if cmd[1]==2:break
#        i+=cmd[1]
#        q=cmd[2]
#    return ''.join(s)
#res=mt(45*'0'+21*'1')
#print(res.count('0'))

#p={
#    (' ',0):(' ',-1,1),
#    (' ',1):(' ',2,1),
#    (' ',2):(' ',2,1),
#    (' ',3):(' ',2,1),
#    (' ',4):(' ',2,1),
#    ('0',1):('1',-1,2),
#    ('0',2):('0',-1,3),
#    ('0',3):('0',-1,4),
#    ('0',4):('0',-1,1),
#    ('1',1):('0',-1,3),
#    ('1',2):('1',-1,3),
#    ('1',3):('1',-1,4),
#    ('1',4):('1',-1,1)
#}

#def mt(s):
#    s=list(' '+s+' ')
#    i=-1
#    q=0
#    while True:
#        cmd=p[(s[i],q)]
#        s[i]=cmd[0]
#        if cmd[1]==2:break
#        i+=cmd[1]
#        q=cmd[2]
#    return ''.join(s)
#res=mt(1000*'0'+500*'1')
#print(res.count('1'))


#p={
#    (' ',0):(' ',-1,1),
#    (' ',2):(' ',2,2),
#    (' ',3):(' ',2,3),
#    ('1',1):('0',-1,2),
#    ('1',2):('1',-1,3),
#    ('1',3):('0',-1,2),
#    ('0',1):('1',-1,2),
#    ('0',2):('1',-1,2),
#    ('0',3):('0',-1,3)
#}

#def mt(s):
#    s=list(' '+s+' ')
#    i=-1
#    q=0
#    while True:
#        cmd=p[(s[i],q)]
#        s[i]=cmd[0]
#        if cmd[1]==2:break
#        i+=cmd[1]
#        q=cmd[2]
#    return ''.join(s)
#res=mt(f'{992:b}')
#print(int(res,2))

#p={
#    (' ',0):(' ',1,1),
#    (' ',1):(' ',2,1),
#    ('1',1):('0',1,1),
#    ('0',1):('1',1,1),
#}

#def mt(s):
#    s=list(' '+s+' ')
#    i=0
#    q=0
#    while True:
#        cmd=p[(s[i],q)]
#        s[i]=cmd[0]
#        if cmd[1]==2:break
#        i+=cmd[1]
#        q=cmd[2]
#    return ''.join(s)
#for x in range(1,1000):
#    res=mt(f'{x:b}')
#    if int(res,2)==63:
#        print(x)

#p = {
#    (' ',0): (' ',-1,1),
#    (' ',1): (' ',2,1),
#    ('1',1): ('0',-1,1),
#    ('0',1): ('1',-1,1)
#}

#def mt(s):
#    s=list(' '+s+' ')
#    i=-1
#    q=0
#    while True:
#        cmd=p[(s[i],q)]
#        s[i]=cmd[0]
#        if cmd[1]==2:break
#        i+=cmd[1]
#        q=cmd[2]
#    return ''.join(s)
#for x in range(1,30000):
#    res=mt(f'{x:b}')
#    if int(res,2)==77:
#        print(x)

#prog = {
#    (' ',0): (' ',-1,1),
#    (' ',2): (' ',2,2),
#    ('0',2): ('1',-1,2),
#    ('1',1): ('2',0,2),
#    ('1',2): ('1',-1,1),
#    ('2',1): ('0',-1,1),
#    ('2',2): ('2',-1,2)
#    }
#def mt(s):
#    s = list(' '+s+' ')
#    i = -1
#    q = 0
#    while True:
#        cmd = prog[(s[i],q)]
#        s[i] = cmd[0]
#        if cmd[1]==2: break
#        i += cmd[1]
#        q = cmd[2]
#    return ''.join(s)
#res=mt(575*'0'+303*'1'+122*'2')
#print(sum(map(int,res.strip())))

#prog = {
#    (' ',0): (' ',-1,1),
#    (' ',1): (' ',2,1),
#    ('1',1): ('3',-1,1),
#    ('1',2): ('3',-1,1),
#    ('2',1): ('1',0,2),
#    ('3',1): ('2',-1,1)
#    }
#def mt(s):
#    s = list(' '+s+' ')
#    i = -1
#    q = 0
#    while True:
#        cmd = prog[(s[i],q)]
#        s[i] = cmd[0]
#        if cmd[1]==2: break
#        i += cmd[1]
#        q = cmd[2]
#    return ''.join(s)

#res=mt(400*'1'+250*'2'+350*'3')
#print(res.count('3'))

#prog = {
#    (' ',0): (' ',1,0),
#    (' ',1): (' ',2,1),
#    ('0',0): ('1',1,1),
#    ('0',1): ('1',1,0),
#    ('1',0): ('0',1,1),
#    ('1',1): ('0',1,0),
#    ('2',0): ('1',2,0),
#    ('2',1): ('0',2,1)
#    }
#def mt(s):
#    s = list(' '+s+' ')
#    i = 0
#    q = 0
#    while True:
#        cmd = prog[(s[i],q)]
#        s[i] = cmd[0]
#        if cmd[1]==2: break
#        i += cmd[1]
#        q = cmd[2]
#    return ''.join(s)

#res = mt(750*'1'+650*'0'+'2')
#print(res.count('1'))

#prog = {
#    (' ',0): (' ',-1,1),
#    (' ',1): (' ',2,1),
#   ('0',1): ('0',-1,1),
#    ('1',1): ('1',2,1)
#    }
#def mt(s):
#    s = list(' '+s+' ')
#    i = -1
#    q = 0
#    while True:
#        cmd = prog[(s[i],q)]
#        s[i] = cmd[0]
#        if cmd[1]==2: break
#        i += cmd[1]
#        q = cmd[2]
#    return ''.join(s)

#from itertools import *

#m = []
#for x in product('01',repeat=19):
#    s = ''.join(x)
#    res = mt(s)
#    if res.count('1')==2:
#        m.append([s.count('0'),s,res])
#print(max(m))

prog = {
    (' ',0): (' ',-1,0),
    (' ',1): ('1',2,1),
    ('0',0): ('1',2,1),
    ('0',1): ('1',2,0),
    ('1',0): ('0',-1,1),
    ('1',1): ('0',-1,1)
    }

def mt(s):
    s = list(' '+s+' ')
    i = -1
    q = 0
    while True:
        cmd = prog[(s[i],q)]
        s[i] = cmd[0]
        if cmd[1]==2: break
        i += cmd[1]
        q = cmd[2]
    return ''.join(s)

from itertools import *

m = []
for x in product('01',repeat=18):
    s = ''.join(x)
    res = mt(s)
    if res.count('0')==7:
        m.append([s.count('0'),s,res])
print(max(m))
