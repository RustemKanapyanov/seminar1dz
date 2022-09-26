# Напишите программу, которая принимает на вход
# двух точек и находит расстояние между ними в 2D пространстве.
# https: //ru.onlinemschool.com/math/Library/analytic_geometry/point_Length/

x_1 = int(input('Введите координату'))
y_1 = int(input('Введите координату'))
x_2 = int(input('Введите координату'))
y_2 = int(input('Введите координату'))
print(f"{((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2 )** 0.5:04}")