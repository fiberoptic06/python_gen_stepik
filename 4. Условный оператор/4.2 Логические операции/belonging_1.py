# Принадлежность 1
# Напишите программу, которая принимает целое число
# x
# x и определяет, принадлежит ли данное число указанному промежутку.
# -1 .... 17
# Формат входных данных
# На вход программе подаётся целое число
# x
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

x = int(input())
if x >= 0 and x <= 16:
    print("Принадлежит")
else:
    print("Не принадлежит")