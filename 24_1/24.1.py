#s = open('24.txt').readline()

#print(23*'DBAC'+'DBA' in s)
#print(len(23*'DBAC'+'DBA'))

#s=open('24_1.txt').readline()

#print('Q'+17*'RSQ'+'RS' in s)
#print(len('Q'+17*'RSQ'+'RS'))

#s = open('24_2.txt').readline()
#s = s.replace('ad','a d').replace('da','d a')
#print(max(len(c) for c in s.split()))

#s=open('24_3.txt').readline()
#s = s.replace('XZZY','XZZ ZZY')
#print(max(len(c) for c in s.split()))

#s = open('24_4.txt').readline()

#while 'DD' in s: s = s.replace('DD','D D')
#print(max(len(c) for c in s.split() if 'FE' in c))

#s=open('24_5.txt').readline()
#s = s.replace('AB','*').replace('AC','*').replace('A',' ').replace('B',' ')\
#    .replace('C',' ')

#print(max(len(c) for c in s.split()))

#s=open('24_6.txt').readline()
#s=s.replace('ZXY','*').replace('ZYX','*').replace('Z',' ').replace('Y',' ').replace('X',' ')
#print(max(len(c) for c in s.split()))

#s=open('24_7.txt').readline()
#s=s.replace('2','1').replace('B','A').replace('11A','*').replace('1',' ').replace('A',' ')
#print(max(len(c) for c in s.split()))

#s = open('24_8.txt').readline()
#
#s = s.replace('XYZY','XYZ YZY').replace('Z','X').replace('XY','*')\
#    .replace('X',' ').replace('Y',' ')
#print(max(len(c) for c in s.split()))

#s = open('24_9.txt').readline()
#s = s.replace('R','Q').replace('W','Q').replace('2','1').replace('4','1')
#while 'QQ' in s: s = s.replace('QQ','Q Q')
#while '11' in s: s = s.replace('11','1 1')

#print(max(len(c) for c in s.split()))

#s = open('24_10.txt').readline()

#s = s.replace('EA','**').replace('NPC','***')

#for c in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
#    s = s.replace(c,' ')
#print(max(len(c) for c in s.split()))

s = open('24_11.txt').readline()

s = s.replace('E','A')
for c in 'CDFGH': s = s.replace(c,'B')
s = s.replace('BBA','BBA BBA')

print(max(len(c) for c in s.split() if c.count('BBA')==2))
