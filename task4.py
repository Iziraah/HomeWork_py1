#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

n = int(input('Введите номер четверти: '))
if (n == 1):
    print('Значения х = [0; +∞), значения у = [0; +∞).')
elif (n == 2):
    print('Значения х = [0; -∞), значения у = [0; +∞).')
elif (n == 3):
    print('Значения х = [0; -∞), значения у = [0; -∞).')
elif (n == 4):
    print('Значения х = [0; +∞), значения у = [0; -∞).')
else:
    print('Существует всего 4 четверти. Попробуйте еще раз')