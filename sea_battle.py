# Морской бой
import random

field = []
field_size = 3
empty_line0 = ['♠'] * field_size
empty_line1 = ['♠'] * field_size
empty_line2 = ['♠'] * field_size

field = [empty_line0, empty_line1, empty_line2]


def print_field():
    print(" ", end=" ")
    for k in range(field_size):
        print(f'{k+1}', end=" ")
    print()
    for i in range(field_size):
        print(f'{i+1}', end=" ")
        for j in range(field_size):
            print(field[i][j], end=" ")
        print()
print_field()

x_coordinate_ship = random.randint(1, field_size)
y_coordinate_ship = random.randint(1, field_size)

x_coordinate_strike = 0
y_coordinate_strike = 0

while x_coordinate_ship != x_coordinate_strike and  y_coordinate_ship != y_coordinate_strike:
    x_coordinate_strike = int(input('Введиет координаты по высоте: '))
    y_coordinate_strike = int(input('Введите координаты по ширине: '))