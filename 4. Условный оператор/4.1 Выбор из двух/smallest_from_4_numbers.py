# Наименьшее из четырёх чисел 🌶️
# Напишите программу, которая определяет наименьшее из четырёх чисел.
#
# Формат входных данных
# На вход программе подаются четыре целых числа.
#
# Формат выходных данных
# Программа должна вывести наименьшее из четырёх чисел.
#
# Примечание. Учитывайте, что минимальные числа могут повторяться (смотрите тест №5).
# В таком случае необходимо вывести только одно из них.

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

min_num = num1

if num2 < min_num:
    min_num = num2
if num3 < min_num:
    min_num = num3
if num4 < min_num:
    min_num = num4

print(min_num)