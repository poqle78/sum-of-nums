from lab2 import *

# Запуск функций с вводом данных с клавиатуры
try:
    sp = sorted([int(i) for i in input("Введите список, состоящий минимум из 1 элемента: ").split()])
    num = int(input("Введите искомое число: "))

    if num not in sp or len(sp) == 0:
        print("искомое число отсутствует в списке или список оказался пустым!")
    else:
        print(fast_guess_num(num, sp))
        print(guess_num(num, sp))

except ValueError:
    print("Неверный формат данных")
