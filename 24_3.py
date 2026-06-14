#s=open('24.txt').readline()

#m=0
#c=''
#for r in range(len(s)):
#    c+=s[r]
#    while c.count('D')>2:c=c[1:]
#    m = max(m,len(c))
#print(m)

#s=open('24_2.txt').readline()

#kx = ky = 0

#m = 0
#l = 0

#for r in range(len(s)):
#    if s[r]=='X': kx+=1
#    if s[r]=='Y': ky+=1
#    while kx>1 or ky>1:
#        if s[l]=='X': kx-=1
#        if s[l]=='Y': ky-=1
#        l+=1
#    if kx==1 and ky==1:
#        m = max(m,r-l+1)
#print(m)

#s=open('24_3.txt').readline()
#kt = 0

#m = []
#l = 0

#for r in range(len(s)):
#    if s[r]=='T': kt+=1
#    while kt>100:
#        if s[l]=='T':kt-=1
#        l+=1
#    if kt==100: m.append(r-l+1)
#print(max(m))

#s=open('24_1.txt').readline()
#m=0
#c=''
#for r in range(len(s)):
#    c+=s[r]
#    while 'G' in c or 'W' in c or 'P' in c: c = c[1:]
#    m = max(m,len(c))
#print(m)

#s=open('24_22.txt').readline()
#m=0
#c=''
#for r in range(len(s)):
#    c+=s[r]
#    while 'XZZY' in c:c=c[1:]
#    m=max(m,len(c))
#print(m)

#s = open('24_33.txt').readline()

#m = 0
#c = ''

#for r in range(len(s)):
#    c+=s[r]
#    while 'PR' in c and 'ST' in c: c = c[1:]
#    m = max(m,len(c))
#print(m)

#s = open('24_44.txt').readline()
#for c in '2468': s =s.replace(c,'0')
#for c in '3579': s =s.replace(c,'1')

#m = 0
#c = ''

#for r in range(len(s)):
#    c+=s[r]
#    while '00' in c or '11' in c: c = c[1:]
#    m = max(m,len(c))
#print(m)

#s=open('24_55.txt').readline()
#m = 0
#c = ''

#for r in range(len(s)):
#    c+=s[r]
#    while not all(x<=y for x,y in zip(c,c[1:])): c = c[1:]
#    m = max(m,len(c))
#print(m)

#s=open('24_66.txt').readline()
#m = 0
#c = ''

#for r in range(len(s)):
#    c+=s[r]
#    while c.count('AB')>100: c = c[1:]

#    if c.count('AB')==100: m = max(m,len(c))

#print(m)


#s = open('24_77.txt').readline()
#m = 0
#c = ''

#for r in range(len(s)):
#    c+=s[r]
#    while c.count('X')>1 or c.count('Y')>1: c = c[1:]

#    if c.count('X')==1 and c.count('Y')==1: m = max(m,len(c))
#print(m)

#s = open('24_888.txt').readline()
#for c in 'EIOUY': s=s.replace(c,'A')
#m = 0
#c = ''

#for r in range(len(s)):
#    c+=s[r]
#    while c.count('.')>0 or c.count('A')>7: c=c[1:]
#    m = max(m,len(c))

#print(m)

#s = open('24_99.txt').readline()
#m = 0
#c = ''

#for r in range(len(s)):
#    c+=s[r]
#    if c[-4:]=='2025':
#        while c.count('2025')>50: c=c[1:]
#        if c.count('2025')==50 and c.count('Y')>=140:
#            m = max(m,len(c))
#print(m)


#s = open('24_100.txt').readline()
#m = 0
#c = ''

#for r in range(len(s)):
#    c+=s[r]
#    while c.count('WWF')>120 or 'WSFWW' in c: c = c[1:]
#    m = max(m,len(c))
#print(m)

#s = open('24_111.txt').readline()
#m = 10**6
#c = ''

#for r in range(len(s)):
#    c+=s[r]
#    while c.count('W')==90:
#        if c.count('2025')>=110: m = min(m,len(c))
#        c = c[1:]
#print(m)

#s = open('24_122.txt').readline()
#m = 10**6
#c = ''

#for r in range(len(s)):
#    c+=s[r]
#    if c[-1]!='Q':
#        while c.count('RSQ')==130:
#            m = min(m,len(c))
#            c = c[1:]
#print(m)

#s = open('24_133.txt').readline()
#for c in 'QWERTYUIOPSDFGHJKLZXCVNM': s = s.replace(c,' ')
#m = 0
#c = ''

#for r in range(len(s)):
#    c+=s[r]
#    while ' ' in c: c = c[1:]
#    m = max(m, len(c))
#print(m)

#s = open('24_144.txt').readline()
#for c in 'QWERTYUIOPSDFGHJKLZXCVNM': s = s.replace(c,' ')
#m = []
#c = ''

#for r in range(len(s)):
#    c+=s[r]
#    if c[-1] in '13579B':
#        while ' ' in c or c[0]=='0': c = c[1:]
#        m.append(c)

#mx = max(m, key=lambda x: int(x,12))
#print(s.index(mx))

#s = open('24_155.txt').readline()
#for c in 'QWRTYUIOPSFGHJKLZXVNM': s = s.replace(c,' ')
#m = []
#c = ''

#for r in range(len(s)):
#    c+=s[r]
#    if c[-1] in '05A':
#        while ' ' in c or len(c)>0 and c[0]=='0': c = c[1:]
#        if len(c)>0: m.append(c)

#mx = max(m, key=lambda x: int(x,15))
#print(s.index(mx)+len(mx)-1)

#s = open('24_4.txt').readline()

#kx = 0

#m = []
#l = 0

#for r in range(len(s)):
#    if s[r]=='X': kx+=1
#    if s[r]=='Y':
#        l = r+1
#        kx = 0
#    while kx>=500:
#        m.append(r-l+1)
#        if s[l]=='X': kx-=1
#        l+=1
#print(min(m))      

#s = open('24_5.txt').readline()

#k = 0
#m = []
#l = 0

#for r in range(len(s)):
#    if s[r]=='.': k+=1
#    if s[r]=='Y':
#        l = r+1
#        k = 0
#    while k>5:
#        if s[l]=='.': k-=1
#        l+=1
#    if k<=5: m.append(r-l+1)
#print(max(m))

#s = open('24_6.txt').readline()

#kr = ka = 0
#m = []
#l = 0

#for r in range(len(s)):
#    if s[r]=='R': kr+=1
#    if s[r]=='A': ka+=1
#    while ka>3:
#        if s[l]=='A': ka-=1
#        if s[l]=='R': kr-=1
#        l += 1
#    if ka<=3 and kr>=2:
#        m.append(r-l+1)
#print(max(m))

#s = open('24_7.txt').readline()

#k = 0
#m = []
#l = 0

#for r in range(3,len(s)):
#    if s[r-3]+s[r-2]+s[r-1]+s[r]=='FSRQ': k+=1

#    while k>80:
#        if s[l]+s[l+1]+s[l+2]+s[l+3]=='FSRQ': k -=1
#        l += 1
#    if k==80:
#        m.append(r-l+1)
#print(max(m))

#s = open('24_8.txt').readline()

#k = 0
#m = []
#l = 0

#for r in range(2,len(s)):
#    if s[r-2]+s[r-1]+s[r]=='BAD' or s[r-2]+s[r-1]+s[r]=='FAT': k+=1

#    while k==3:
#        m.append(r-l+1)
#        if s[l]+s[l+1]+s[l+2]=='BAD' or s[l]+s[l+1]+s[l+2]=='FAT': k-=1
#        l+=1
#print(min(m))

#s = open('24_9.txt').readline()

#k = 0
#m = []
#l = 0
#for r in range(1, len(s)):
#    if s[r-1]+s[r]=='RO': k+=1
#    if s[r-2]+s[r-1]+s[r]=='ORO':
#        l = r-1
#        k = 1
#    if s[r-2]+s[r-1]+s[r]=='ROR':
#        l = r-1
#        k = 0
#    while k>21:
#        if s[l]+s[l+1]=='RO': k-=1
#        l += 1
#    if k==21: m.append(r-l+1)
#print(max(m))


s = open('24_10.txt').readline()

d = {c:0 for c in 'QWERTYUIOPLKJHGFDSAZXCVBNM'}
m = []
l = 0

for r in range(len(s)):
    d[ s[r] ] += 1
    while all(d[c]>=1 for c in 'QWERTYUIOPLKJHGFDSAZXCVBNM'):
        m.append(r-l+1)
        d[ s[l] ] -= 1
        l += 1
print(min(m))
