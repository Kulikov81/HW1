# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

print("Введите число")
a = int(input())
if a % 6 == 0:
    p = a // 6
    k = p * 4
    s = a // 6
    print (f' {p}  {k}  {s}')
else:
    print ('Не верное число')

