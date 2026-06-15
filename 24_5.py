#s = open('24.txt').readline()

#s = s.replace('A',' ').replace('E',' ')

#print(max(len(c) for c in s.split()))


#s = open('24_2.txt').readline()

#s = s.replace('W',' ').replace('R',' ').replace('Q',' ')

#print(max(len(c) for c in s.split()))


#s=open('24_3.txt').readline()

#s=s.replace('PP','P P')
#print(max(len(c) for c in s.split()))


#s = open('24_4.txt').readline()

#s = s.replace('XYZ','XY YZ')

#print(max(len(c) for c in s.split()))


#s = open('24_5.txt').readline()

#while 'DD' in s: s=s.replace('DD','D D')

#print(max(len(c) for c in s.split() if 'FE' in c))


#s = open('24_6.txt').readline()

#print(23*'DBAC'+'DBA' in s)
#print(len(23*'DBAC'+'DBA'))

#s=open('24_7.txt').readline()
#print('MN'+45*'KLMN' in s)
#print(len('MN'+45*'KLMN'))

#s = open('24_8.txt').readline()

#print('YZ'+22*'XYZ'+'X' in s)
#print(len('YZ'+22*'XYZ'+'X'))

#s = open('24_9.txt').readline()

#m = 2

#for l in range(len(s)):
#    for r in range(l+m,len(s)):
#        c = s[l:r]
#        if 'A' in c or 'B' in c or 'C' in c: break
#        if all(x<=y for x,y in zip(c,c[1:])): m =max(m,len(c))
#print(m)

#s=open('24_10.txt').readline()
#m=2
#for l in range(len(s)):
#    for r in range(l+m,len(s)):
#        c=s[l:r]
#        if all(x<=y for x,y in zip(c,c[1:])): m =max(m,len(c)) #10
#        else:break
#print(m)

#s = open('24_11.txt').readline()

#c = ''
#m = 0

#for r in range(len(s)):
#    c+=s[r]
#    if len(c)>=3 and c[-3]==c[-2]==c[-1]: c = c[-2:]
#    m = max(m, len(c))
#print(m)

#s = open('24_12.txt').readline()

#s = s.replace('B','A').replace('C','A')

#while 'AAA' in s: s=s.replace('AAA','AA AA')

#print(max(len(c) for c in s.split()))


#s=open('24_13.txt').readline()
#s=s.replace('R','Q').replace('W','Q').replace('2','1').replace('4','1')

#while 'QQ' in s:s=s.replace('QQ','Q Q')
#while '11' in s:s=s.replace('11','1 1')
#print(max(len(c) for c in s.split()))


#from re import *

#s = open('24_14.txt').readline()

#reg = r'(AB|AC)+'

#m = max(len(x.group()) for x in finditer(reg,s))
#print(m//2)

#from re import *

#s=open('24_15.txt').readline()
#reg=f'(ZXY|ZYX)+'
#m=max(len(x.group()) for x in finditer(reg,s))
#print(m//3)

#from re import *

#s = open('24_16.txt').readline()
#while 'XXXX' in s: s=s.replace('XXXX','XXX XXX')
#while 'YYYY' in s: s=s.replace('YYYY','YYY YYY')
#while 'ZZZZ' in s: s=s.replace('ZZZZ','ZZZ ZZZ')

#reg = r'(?=((XX|YY|ZZ)+))'

#m = max(len(x.group(1)) for x in finditer(reg,s))
#print(m)

#from re import *

#s = open('24_17.txt').readline()

#reg = r'([AB][12])+'

#m = max(len(x.group()) for x in finditer(reg,s))
#print(m//2)

#from re import *

#s = open('24_18.txt').readline()

#reg = r'(?=((X.X|Y.Y)+))'

#m = max(len(x.group(1)) for x in finditer(reg,s))
#print(m//3)

#from re import *

#s=open('24_19.txt').readline()
#reg=r'(AB|CAC)+'
#m=max(len(x.group())for x in finditer(reg,s))
#print(m)


#s=open('24_20.txt').readline()

#m=1

#for l in range(len(s)):
#    for r in range(l+m,len(s)):
#        c=s[l:r]
#        if '.' in c:break
#        if c.count('A')>=3 and '.' not in c:
#            m=max(m,len(c))
#print(m)


#s=open('24_21.txt').readline()
#m=1

#for l in range(len(s)):
#    for r in range(m+l,len(s)):
#        c=s[l:r]
#        if c.count('T')>100:break
#        if c.count('T')==100:m=max(m,len(c))
#print(m)

#s=open('24_22.txt').readline()
#m=1


#for l in range(len(s)):
#    for r in range(l+m,len(s)):
#        c=s[l:r]
#        if c.count('M')>278:break
#        m=max(m,len(c))
#print(m)

#s=open('24_23.txt').readline()
#m=1
#for l in range(len(s)):
#    for r in range(m+l,len(s)):
#        c=s[l:r]
#        if c.count('C')>2 or c.count('D')>2:break
#        m=max(m,len(c))
#print(m)

#s=open('24_24.txt').readline()
#m=1
#for l in range(len(s)):
#    for r in range(l+m,len(s)):
#        c=s[l:r]
#        if c.count('AB')>50:break
#        if c.count('AB')==50:
#            m=max(m,len(c))
#print(m)

#s = open('24_25.txt').readline()
#s = s.replace('O','A').replace('D','C').replace('F','C')

#c = ''
#m = 0

#for r in range(len(s)):
#    c+=s[r]
#    while c.count('CA')>5: c=c[1:]
#    m=max(m,len(c))
#print(m)

#s=open('24_26.txt').readline()
#m=1
#for l in range(len(s)):
#    for r in range(l+m,len(s)):
#        c=s[l:r]
#        if c.count('RO')>21 or 'ORO' in c or 'ROR' in c:break
#        if c.count('RO')==21:
#            m=max(m,len(c))
#print(m)

#s=open('24_27.txt').readline()

#c = ''
#k = 0
#m = 0

#for r in range(len(s)):
#    c+=s[r]
#    if c[-3:]=='WWF': k+=1
#    while k>120 or 'WSFWW' in c:
#        if c[:3]=='WWF':k-=1
#        c=c[1:]
#    m=max(m,len(c))
#print(m)

#s = open('24_28.txt').readline()

#c = ''
#m = 0

#for r in range(len(s)):
#    c+=s[r]
#    if c[-4:]=='2025':
#        while c.count('2025')>50: c=c[1:]
#        if c.count('Y')>=140: m = max(m,len(c))
#print(m)


#s=open('24_29.txt').readline()

#s = s.replace('E','A').replace('U','A')
#s = s.replace('C','B').replace('D','B').replace('F','B')

#c = ''
#m = 0
#k = 0

#for r in range(len(s)):
#    c+=s[r]
#    if c[-3:]=='BAB': k+=1
#    while k>2:
#        if c[:3]=='BAB': k-=1
#        c=c[1:]
#    if k==2: m=max(m,len(c))
#print(m)

#s = open('24_30.txt').readline()

#c = ''
#m = 10**6

#for r in range(len(s)):
#    c+=s[r]
#    while c.count('BAD')+c.count('FAT')==3:
#        m = min(m,len(c))
#        c = c[1:]
#print(m)


#s = open('24_31.txt').readline()

#m = 1000

#for l in range(len(s)):
#    for r in range(l+m,l,-1):
#        c = s[l:r]
#        if c[0]!='A' or c.count('F')==0 or len(c)==2: break
#        if c[0]=='A' and c[-1]=='F': m = min(m,len(c))
#print(m)

#s=open('24_32.txt').readline()
#c = ''
#m = 10**6

#for r in range(len(s)):
#    c+=s[r]
#    if c[-1]=='D':
#        if c[0]==c[-1] and len(c)>2: m = min(m,len(c))
#        c = 'D'
#print(m)


#s = open('24_33.txt').readline()

#c = ''
#m = 10**6

#for r in range(len(s)):
#    c+=s[r]
#    if c[-1]!='Q':
#        while c.count('RSQ')==130:
#            m = min(m,len(c))
#            c=c[1:]
#print(m)

#s = open('24_34.txt').readline()

#c = ''
#m = 10**6

#for r in range(len(s)):
#    c+=s[r]
#    if c[-1] in 'AEIOUY':
#        while c.count('20')>=26:
#            if c.count('20')==26:m=min(m,len(c))
#            c = c[1:]
#        c = ''
#print(m)

#s = open('24_35.txt').readline()

#c = ''
#m = 0

#for r in range(len(s)):
#    c+=s[r]
#    if c[-1] in '0123456789':
#        if c[0]!=c[-1] and c.count('B')==c.count('C'):
#            m = max(m,len(c))
#        c = c[-1]
#print(m)

#s = open('24_36.txt').readline()

#c = ''
#m = 0

#for r in range(len(s)):
#    c+=s[r]
#    if c[-1] in '02468':
#        if c.count(c[1])==len(c)-2: m = max(m,len(c))
#        c = c[-1]
#print(m)

#s = open('24_37.txt').readline()
#for c in 'QWRTYUIOPSGHJKLZXVNM': s=s.replace(c,' ')

#c = ''
#m = 0

#for r in range(len(s)):
#    c+=s[r]
#    while ' ' in c or len(c)>0 and c[0]=='0' or c.count('B')>10: c=c[1:]
#    if c.count('B')==10: m = max(m,len(c))
#print(m)

#from re import *

#s = open('24_38.txt').readline()

#reg = r'(?=([1-9AB][0-9AB]+[0369]))'

#m = max([x.group(1) for x in finditer(reg,s)], key=lambda x: int(x,12))

#print(s.find(m))


#from re import *

#s=open('24_39.txt').readline()


#reg = r'(?=([1-9AB][0-9AB]+[06]))'

#m = max([x.group(1) for x in finditer(reg,s)], key=lambda x: int(x,12))

#print(s.find(m)+len(m)-1)


#from re import *

#s = open('24_40.txt').readline()

#num = r'([1-9][0-9]*|0)'
#reg = rf'B{num}([-*]{num})+'

#m = max(len(x.group()) for x in finditer(reg,s))
#print(m)

#from re import *

#s=open('24_41.txt').readline()

#num=r'([1-9][0-9]*)'
#reg=rf'{num}([+*]{num}){{39}}'
#reg=rf'(?=({reg}))'

#m=max(len(x.group(1)) for x in finditer(reg,s))
#print(m)

#from re import *

#s = open('24_42.txt').readline()

#num = r'([1-9][0-9]*[05]|[05])'
#reg = rf'{num}([+*]{num})+'
#reg = rf'(?=({reg}))'

#m = max(len(x.group(1)) for x in finditer(reg,s))
#print(m)

#from re import *

#s = open('24_43.txt').readline()

#numa = r'([1-9][0-9]*[02468]|[2468])'
#numb = r'([1-9][0-9]*[13579]|[13579])'
#reg = rf'(\({numa}[+-]{numb}\))+'
#reg = rf'(?=({reg}))'

#m = max(len(x.group(1)) for x in finditer(reg,s))
#print(m)

#from re import *

#s = open('24_44.txt').readline()

#num = r'([1-9][0-9]{3}\.[0-9]+)'
#reg = rf'(?=({num}&{num}))'

#m = max(len(x.group(1)) for x in finditer(reg,s))
#print(m)

from re import *

s = open('24_45.txt').readline()

reg = r'(?=([0-9]+([A-Z]+[0-9]+){80}))'

m = max([x.group(1) for x in finditer(reg,s)],key=len)
print(s.find(m))






























