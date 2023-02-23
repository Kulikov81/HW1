# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
# за проезд и получали билет с номером. Счастливым билетом называют такой
# билет с шестизначным номером, где сумма первых трех цифр равна сумме
# последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

print("Введите шестизначное число")
a = int(input())
if (a // 100000) + ((a // 10000) % 10) + ((a // 1000) % 10) == ((a // 100) % 10) + (
    (a // 10) % 10
) + (a % 10):
    print("YES")
else:
    print("NO")
