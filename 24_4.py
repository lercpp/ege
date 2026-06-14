#s = open('24.txt').readline()

#m = 1

#for l in range(len(s)):
#    for r in range(l+m, len(s)):
#        c = s[l:r]
#        if 'G' in c or 'W' in c or 'P' in c: break
#        m = max(m,len(c))
#print(m)

#s=open('24_2.txt').readline()

#m=1

#for l in range(len(s)):
#    for r in range(l+m,len(s)):
#        c=s[l:r]
#        if 'XZZY' in c:break
#        m=max(m,len(c))
#print(m)

#s=open('24_3.txt').readline()

#m=1

#for l in range(len(s)):
#    for r in range(l+m,len(s)):
#        c=s[l:r]
#        if c.count('AB')>100:break
#        if c.count('AB')==100:
#            m=max(m,len(c))
#print(m)

#s=open('24_4.txt').readline()

#m=1

#for l in range(len(s)):
#    for r in range(l+m,len(s)):
#        c=s[l:r]
#        if c.count('X')>1 or c.count('Y')>1:break
#        if c.count('X')==1 and c.count('Y')==1:
#            m=max(m,len(c))
#print(m)


#s=open('24_5.txt').readline()
#for c in 'EIOUY': s=s.replace(c,'A')

#m=1

#for l in range(len(s)):
#    for r in range(l+m,len(s)):
#        c=s[l:r]
#        if '.' in c or c.count('A')>7:break
#        m=max(m,len(c))
#print(m)

#s = open('24_6.txt').readline()

#m = 1

#for l in range(len(s)):
#    for r in range(l+m,len(s)):
#        c = s[l:r]
#        if c.count('2025')>50: break
#        if c[-4:]=='2025' and c.count('Y')>=140 and c.count('2025')==50:
#            m = max(m,len(c))
#print(m)

#s=open('24_7.txt').readline()

#m=1

#for l in range(len(s)):
#    for r in range(m+l,len(s)):
#        c=s[l:r]
#        if c.count('WWF')>120 or 'WSFWW' in c:break
#        m=max(m,len(c))
#print(m)

#s = open('24_8.txt').readline()

#m = 10000

#for l in range(len(s)):
#    for r in range(l+m,l,-1):
#        c=s[l:r]
#        if c.count('2025')<110 or c.count('W')<90: break
#        if c.count('W')==90: m=min(m,len(c))
#print(m)

#s = open('24_9.txt').readline()

#m = 10000

#for l in range(len(s)):
#    for r in range(l+m,l,-1):
#        c = s[l:r]
#        if c.count('RSQ')<130: break
#        if c[-1]!='Q' and c.count('RSQ')==130: m = min(m,len(c))
#print(m)


#s = open('24_10.txt').readline()

#for c in 'QWERTYUIOPSDFGHJKLZXCVNM': s = s.replace(c,' ')

#m = 1

#for l in range(len(s)):
#    for r in range(l+m, len(s)):
#        c = s[l:r]
#        if c[0]=='0' or ' ' in c: break
#        m = max(m, len(c))
#print(m)


s = open('24_11.txt').readline()

for c in 'QWERTYUIOPSDFGHJKLZXCVNM': s = s.replace(c,' ')

m = 1
d = []

for l in range(len(s)):
    for r in range(l+m, len(s)):
        c = s[l:r]
        if c[0]=='0' or ' ' in c: break
        if int(c,12)%2!=0:
            m = max(m, len(c))
            d.append([int(c,12),c])

ms = max(d)[1]
print(s.find(ms))
