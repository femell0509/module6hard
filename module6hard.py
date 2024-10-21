import math
class Figure:
    Sides_count = 0
    def __init__(self, sides, color: list):
        self.__sides = sides #if len(sides) == self.Sides_count else [1] * self.Sides_count
        self.__color = color #if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = False
    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 and isinstance(r, int) and isinstance(g, int) and isinstance(b, int)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else: return None

    def __is_valid_sides(self, *sides_new):
        for i in sides_new:
            if isinstance(i, float) or i <= 0:
                return False
        return (len(sides_new) == self.Sides_count)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    Sides_count = 1

    def __init__(self, sides, color):
        super().__init__(sides, color)
        self.__radius = self.get_sides()[0] / (2*math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    Sides_count = 3
    def __init__(self, sides, color):
        super().__init__(sides, color)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    Sides_count = 12
    def __init__(self, sides, color):
        if len(sides) != 1:
            sides = [1]
        sides = sides * self.Sides_count
        super().__init__(sides, color)

    def get_volume(self):
        volume = self.get_sides()[0]
        return volume ** 3



circle1 = Circle([10], [200, 200, 100]) # (Цвет, стороны)
cube1 = Cube([6], [222, 35, 130])

# Проверка на изменение цветов:
print(circle1.get_color())

print(circle1.set_color(55, 66, 77)) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

 # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
print(len(circle1))
#
# # Проверка объёма (куба):
print(cube1.get_volume())

