#Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

a = list(map(int, input('Введите координаты точки А, через пробел: ').split()))
b = list(map(int, input('Введите координаты точки B, через пробел: ').split()))
x = ((b[0]-a[0])**2+(b[1]-a[1])**2)**0.5
print(x)