# Напишите программу, 
# которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

NumList = 65487

# def Sum (n):
#     sum = 0
#     while n > 0:
#         digit = n % 10
#         n = n // 10
#         sum = sum+digit
#     return sum

# print(Sum(NumList))

def Sum(num):
    sum = 0
    for i in str(num):
        sum+=int(i)
    return sum

print(Sum(NumList))
