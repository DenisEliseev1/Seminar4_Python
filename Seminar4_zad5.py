# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

# -Создание двух многочленов-
def multiple1 ():
    k = randint (0, 10)
    mlist = str (randint(0,100))
    if k != 0:
        for i in range (1,k+1):
            km = str (randint (0,100))
            mlist=  km +'*x^'+ str (i) + '+' + mlist
    return mlist
mlist1 = multiple1 ()
#print (f'Полученный многочлен1: {mlist1}')
data = open ('multiple1.txt', 'w')
data.writelines (mlist1)
data.close ()
mlist2 = multiple1 ()
#print (f'Полученный многочлен2: {mlist2}')
data = open ('multiple2.txt', 'w')
data.writelines (mlist2)
data.close ()

def writefiles (path):
    data = open (path, 'r')
    for m in data:
        break
    data.close ()
    return m

def multiple (mlist):
    mlist1 = str (mlist [0])
    for i in range (1, len(mlist)):
        km = str (mlist [i])
        mlist1=  km +'*x^'+ str (i) + '+' + mlist1
    return mlist1
# -Сложение многочленов-
# Создание строк из фалов

m1 =  writefiles ('multiple1.txt') 
print (f'многочлен №1 - {m1}')
m1 = '+' + m1
m2 = writefiles ('multiple2.txt') 
print (f'многочлен №2 - {m2}')
m2 = '+' + m2

def koefm (sum = [], l = 1, m = ''):
    while l > 0:
        s = int  (m[m.rfind('+',0,l-1) : m.rfind('*',0,l-1)])
        sum.append (s) 
        l = m.rfind('+',0,l-1)
    return sum
            
l1m1 = m1.rfind ('+')
l1m2 = m2.rfind ('+')
sumlist1 = [int (m1 [l1m1+1:])]
sumlist2 = [int (m2 [l1m2+1:])]
# print (l1m1, l1m2, sumlist1, sumlist2)
sumlist1 = koefm (sumlist1, l1m1, m1)
sumlist2 = koefm (sumlist2, l1m2, m2)
if len(sumlist1) > len (sumlist2):
    for i in range (len (sumlist1)-len (sumlist2)):
        sumlist2.append (0)
# print (sumlist1)
# print (sumlist2)
for i in range (len (sumlist1)):
    sumlist1 [i] = sumlist1 [i] + sumlist2 [i]
#print (sumlist1)
m = multiple (sumlist1)
#print (m)
data = open ('multiplesum.txt', 'w')
data.writelines ('Sum multiple ---->  ' + m)
data.close ()
# Выделение коэффициентов из многочлена
# сложение коэффициентов
# создание и вывод нового многочлена

