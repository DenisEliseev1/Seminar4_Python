 #Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from random import randint

def mult_prime (x):
    mult = []
    i = 1
    while x >= i:
        if x%i == 0:
            mult.append (i)
            x = x/i
        i += 1   
    return mult
        

n=randint (1, 100 )
print (f'Заданное число N: {n}')
mult_prime_list = mult_prime (n)
print (f'Список простых множителей числа N: {mult_prime_list}')
