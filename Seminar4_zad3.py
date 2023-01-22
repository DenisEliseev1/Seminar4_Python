# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


def seqnumbers (x):
    arr = []
    for i in range (x):
        arr.append (randint (1, 9))
    return arr

def originalnumber(arr):
    orig_num = []
    for i in range (len (arr)):
        s = 0        
        for j in range (len (arr)):
            #print (arr[i], arr[j])
            if arr [i] == arr [j] and i != j:
                s += 1
            #    print (arr[i], arr[j], s)
        if s == 0:
            orig_num.append (arr[i]) 
            #print (orig_num)        
    return orig_num

try:
    n = int (input ('Задайте размер последовательности  N='))
    seqnum = seqnumbers (n)
    print (f'Ваша последовательность {seqnum}')
    orignum = originalnumber (seqnum)
    print (f'Неповторяющиеся значения последовательности: {orignum}')
except:
    print ('Введите целое число')