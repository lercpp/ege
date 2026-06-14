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

s = open('24_12.txt').readline()

s = s.replace('B','A').replace('C','A')

while 'AAA' in s: s=s.replace('AAA','AA AA')

print(max(len(c) for c in s.split()))
