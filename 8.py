#r=0
#
#for a1 in "ЭЮЯ":
#    for a2 in "АБВГ":
#       for a3 in "АБВГ":
#            for a4 in "АБВГ":
#                for a5 in "ЭЮЯ":
#                    s = a1+a2+a3+a4+a5
#                    r += 1
#
#print(r)

#r = 0

#for a1 in 'АБВГДЯ':
#    for a2 in 'АБВГДЯ':
#        for a3 in 'АБВГДЯ':
#            for a4 in 'АБВГДЯ':
#                for a5 in 'АБВГДЯ':
#                    s = a1+a2+a3+a4+a5
#                    if s.count('Я') == 3:
#                        r += 1
#print(r)

#r = 0

#for a1 in 'КАТЕР':
#    for a2 in 'КАТЕР':
#        for a3 in 'КАТЕР':
#            s = a1+a2+a3
#            if s.count('Р') >= 2:
#                r += 1

#print(r)


#r = 0
#
#for a1 in 'ДЖОБС':
#    for a2 in 'ДЖОБС':
#        for a3 in 'ДЖОБС':
#            for a4 in 'ДЖОБС':
#                for a5 in 'ДЖОБС':
#                    for a6 in 'ДЖОБС':
#                            s = a1+a2+a3+a4+a5+a6
#                            if s.count('Д') == 1 and s.count('С') == 1 and s.count('О') == 1 and s.count('Ж')<= 2 :
#                                r += 1
#
#print(r)#840


#k =  0
#
#for a1 in '246':
# for a2 in '0123456':
#  for a3 in '0123456':
#   for a4 in '0123456':
#    for a5 in '3456':
#     s = a1+a2+a3+a4+a5
#     if s.count('4') <= 1:
#      k+=1
#print(k)

#k =  0
#
#for a1 in '1234567':
# for a2 in '01234567':
#  for a3 in '01234567':
#   for a4 in '01234567':
#    for a5 in '1234567':
#        s = a1+a2+a3+a4+a5
#        s = s.replace('3','1').replace('5','1').replace('7','1')
#        if s.count('6') == 1 and '16' not in s and '61' not in s:
#            k+=1
#
#print(k)


#k = 0

#for a1 in '123456':
#    for a2 in '0123456':
#        for a3 in '0123456':
#            for a4 in '0123456':
#                for a5 in '0123456':
#                    for a6 in '0123456':
#                        s = a1+a2+a3+a4+a5
#                        if s.count('6') == 1:
#                            s = s.replace('3','1').replace('5','1').replace('2','0').replace('4','0').replace('6','0')
#                        
#                            if '00' not in s and '11' not in s:
#                                k+=1

#print(k)

#k = 0
#for a1 in 'АВОРТ':
#    for a2 in 'АВОРТ':
#        for a3 in 'АВОРТ':
#            for a4 in 'АВОРТ':
#                for a5 in 'АВОРТ':
#                    for a6 in 'АВОРТ':
#                        s = a1+a2+a3+a4+a5+a6
#                        k += 1
#                        if s == 'ВОРОТА':
#                            print(k,s)
                            
#k = 0

#for a1 in 'АЛПЦЯ':
#    for a2 in 'АЛПЦЯ':
#        for a3 in 'АЛПЦЯ':
#            for a4 in 'АЛПЦЯ':
#                for a5 in 'АЛПЦЯ':
#                    s = a1+a2+a3+a4+a5
#                    k+=1
#
#                    if s.count('А')<=1 and s.count('Ц') == 2 and s.count('Л') ==0:
#                        print(k,s)
#                        break

#k = 0

#for a1 in sorted('АГИЛМОРТ'):
#    for a2 in sorted('АГИЛМОРТ'):
#        for a3 in sorted('АГИЛМОРТ'):
#            for a4 in sorted('АГИЛМОРТ'):
#                for a5 in sorted('АГИЛМОРТ'):
#                    s = a1+a2+a3+a4+a5
#                    k+=1
#                    if k%2 == 0 and s[0] != 'А' and s[0] !='Г' and s.count('Р')>= 2:
#                        print(k,s)
   
#k = 0

#for a1 in ('ABCD'):
#    for a2 in ('ABCD'):
#        for a3 in ('ABCD'):
#            for a4 in ('ABCD'):
#                s = a1+a2+a3+a4
#                if a1<=a2<=a3<=a4:
#                    k+=1
#print(k)

#k=0
#
#for a1 in 'ЧОАНИМЕ':
#    for a2 in 'ЧОАНИМЕ':
#        for a3 in 'ЧОАНИМЕ':
#            for a4 in 'ЧОАНИМЕ':
#                s = a1+a2+a3+a4
#                if s.count('М') == 3:
#                    k+=1
#for a1 in 'ЧОАНИМЕ':
#    for a2 in 'ЧОАНИМЕ':
#        for a3 in 'ЧОАНИМЕ':
#            for a4 in 'ЧОАНИМЕ':
#                for a5 in 'ЧОАНИМЕ':
#                    s = a1+a2+a3+a4+a5
#                    if s.count('М') == 3:
#                        k+=1 
#
#for a1 in 'ЧОАНИМЕ':
#    for a2 in 'ЧОАНИМЕ':
#        for a3 in 'ЧОАНИМЕ':
#            for a4 in 'ЧОАНИМЕ':
#                for a5 in 'ЧОАНИМЕ':
#                    for a6 in 'ЧОАНИМЕ':
#                        s = a1+a2+a3+a4+a5+a6
#                        if s.count('М') == 3:
#                            k+=1 
#    
#print(k)


#k = 0

#for a1 in '12345678':
#    for a2 in '012345678':
#        for a3 in '012345678':
#            for a4 in '012345678':
#                for a5 in '012345678':
#                    for a6 in '012345678':
#                        for a7 in '012345678':
#                            s =a1+a2+a3+a4+a5+a6+a7
#                            if s[0] != '3' and s[0] != '7' and s.count('11') ==0 and s.count('22')==0 and s.count('33')==0 and s.count('44')==0 and s.count('00')==0 and s.count('55')==0 and s.count('66')==0 and s.count('77')==0 and s.count('88')==0:
#                                k+=1

#print(k)


#from itertools import *

#k = 0

#for x in product('WXYZ', 'ABC', 'ABC', 'ABC', 'ABC', 'WXYZ' ):
#    s = ''.join(x)
#    k+=1
#print(k)    
    


#from itertools import *

#k =0

#for x  in product('246', '01234567', '01234567', '01234567', '013457'):
#    s = ''.join(x)
#    if s.count('7') <=2:
#        k+=1

#print(k)
    

#from itertools import *

#k = 0
#for x in product('ГЕПАРД', repeat = 5):
#    s = ''.join(x)
#
#    if s.count('Г') ==1 and s[0] != 'А' and s[-1] != 'Е':
#        k+=1

#print(k)




#from itertools import *

#k=0

#for x in product('АРБУЗ', repeat = 6):
#    s = ''.join(x)
#    if s.count('А') == 3 and 'АА' in s and 'ААА' not in s:
#        k+=1
#print(k)

#from itertools import *

#k =0
#for x in product('ПОЛИНА',repeat = 8):
#    s = ''.join(x)
#    s = s.replace('Л','П').replace('Н','П').replace('А','О').replace('И','О')
#    if s.count('П')>s.count('О'):
#        k+=1

#print(k)


#from itertools import *

#k=0

#for x in permutations('КАЛИЙ',5):
#    s = ''.join(x)
#
#    if s[0] != 'Й' and s.count('ИА') == 0:
#        k+=1

#print(k)

from itertools import *

#k= 0

#for x in permutations('КОМЕТА',6):
#    s=''.join(x)
#    s = s.replace('М','К').replace('Т','К').replace('Е','О').replace('А','О')
#    if 'ОО' not in s and 'КК' not in s:
#        k+=1
#print(k)

#k=0

#for x in set(permutations('ОДЕКОЛОН',8)):
#    s=''.join(x)
#    if s.count('ОО') == 0:
#        k+=1
#print(k)

#k=0

#for x in set(permutations('СОРТИРОВКА',10)):
#    s=''.join(x)
#    s = s.replace('С','Р').replace('Т','Р').replace('В','Р').replace('К','Р').replace('И','О').replace('А','О')
    
#    if 'ООО' not in s and 'РРР' not in s:
#        k+=1
#print(k)

#k=0

#for x in permutations('01234567',7):
#    s=''.join(x)
#    if s[0] != '0':
#        s = s.replace('3','1').replace('5','1').replace('7','1')\
#            .replace('2','0').replace('4','0').replace('6','0')
#        if '00' not in s and '11' not in s:
#            k += 1
#print(k)

#k = 0

#for x in product(sorted('ЯНВАРЬ'), repeat=5):
#    s = ''.join(x)
#    k += 1
#    if s[0]!='Я' and s.count('Ь')<=1 and 'ЯЯ' not in s:
#        print(k,s)
    
#k = 0

#for x in product('ИМНСУ',repeat=4):
#    s = ''.join(x)
#    s1 = s
#    k += 1
#    s = s.replace('Н','М').replace('С','М').replace('У','И')
#    if s.count('М') >= s.count('И'):
#        print(k,s1)

k = 0
k2 = 0

for x in product('ЕЛНОСЦ',repeat=6):
    s = ''.join(x)
    k += 1
    if k%2==0 and s[0] not in 'ЕО' and s.count('Ц')==2:
        k2 += 1
print(k2)
