#Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет
n=int(input('Введите число: '))
if (0<n<6):
    print('нет')
elif (5<n<8):
    print('да')
else: 
    print('Введите число от 1 до 7!.')