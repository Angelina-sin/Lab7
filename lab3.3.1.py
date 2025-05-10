import math

class Figure:
    def dimention(self):
        raise NotImplementedError("Цей метод має бути реалізований у підкласі")

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        raise NotImplementedError("Цей метод має бути реалізований у підкласі")

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def dimention(self):
        return 2

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        s = self.perimetr() / 2
        if s > self.a and s > self.b and s > self.c:
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        else:
            raise ValueError(f"Не можна побудувати трикутник з такими сторонами: {self.a}, {self.b}, {self.c}")

    def volume(self):
        return self.square()

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def volume(self):
        return self.square()

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def dimention(self):
        return 2

    def perimetr(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        try:
            h = math.sqrt(self.c**2 - ((self.b - self.a)**2 + self.c**2 - self.d**2) / (2 * (self.b - self.a)))
            return ((self.a + self.b) / 2) * h
        except ValueError:
            raise ValueError(f"Некоректні розміри для трапеції: {self.a}, {self.b}, {self.c}, {self.d}")

    def volume(self):
        return self.square()

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

    def volume(self):
        return self.square()

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2

    def volume(self):
        return self.square()

class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return 3

    def squareSurface(self):
        return 4 * math.pi * self.r ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.r ** 3

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimention(self):
        return 3

    def squareBase(self):
        return super().square()

    def squareSurface(self):
        l = math.sqrt((self.a / 2) ** 2 + self.h ** 2)
        return 3 * (self.a * l / 2)

    def height(self):
        return self.h

    def volume(self):
        return (1 / 3) * self.squareBase() * self.h

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimention(self):
        return 3

    def squareBase(self):
        return super().square()

    def squareSurface(self):
        l_a = math.sqrt((self.a / 2) ** 2 + self.h ** 2)
        l_b = math.sqrt((self.b / 2) ** 2 + self.h ** 2)
        return self.a * l_b + self.b * l_a

    def height(self):
        return self.h

    def volume(self):
        return (1 / 3) * self.squareBase() * self.h

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimention(self):
        return 3

    def squareSurface(self):
        return 2 * (self.a * self.b + self.a * self.c + self.b * self.c)

    def squareBase(self):
        return super().square()

    def height(self):
        return self.c

    def volume(self):
        return self.a * self.b * self.c

class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h

    def dimention(self):
        return 3

    def squareBase(self):
        return super().square()

    def squareSurface(self):
        l = math.sqrt(self.r ** 2 + self.h ** 2)
        return math.pi * self.r * (self.r + l)

    def height(self):
        return self.h

    def volume(self):
        return (1 / 3) * super().square() * self.h

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def dimention(self):
        return 3

    def squareBase(self):
        return super().square()

    def squareSurface(self):
        return 2 * super().square() + (self.a + self.b + self.c) * self.h

    def height(self):
        return self.h

    def volume(self):
        return super().square() * self.h

def read_file(filename):
    figures = []
    with open(filename, 'r') as f:
        for line in f:
            info = line.strip().split()
            if not info:
                continue
            figure = info[0]
            parameters = list(map(float, info[1:]))
            if figure == "Triangle":
                figures.append(Triangle(*parameters))
            elif figure == "Rectangle":
                figures.append(Rectangle(*parameters))
            elif figure == "Trapeze":
                figures.append(Trapeze(*parameters))
            elif figure == "Parallelogram":
                figures.append(Parallelogram(*parameters))
            elif figure == "Circle":
                figures.append(Circle(*parameters))
            elif figure == "Ball":
                figures.append(Ball(*parameters))
            elif figure == "TriangularPyramid":
                figures.append(TriangularPyramid(*parameters))
            elif figure == "QuadrangularPyramid":
                figures.append(QuadrangularPyramid(*parameters))
            elif figure == "RectangularParallelepiped":
                figures.append(RectangularParallelepiped(*parameters))
            elif figure == "Cone":
                figures.append(Cone(*parameters))
            elif figure == "TriangularPrism":
                figures.append(TriangularPrism(*parameters))
    return figures

if __name__ == "__main__":
    files = ['input01.txt', 'input02.txt', 'input03.txt']
    files = ["C:/Users/Asus/Downloads/input01.txt", "C:/Users/Asus/Downloads/input02.txt", "C:/Users/Asus/Downloads/input03.txt"]

    for file in files:
        figures = read_file(file)
        for figure in figures:
            try:
                print(f"Фігура: {figure.__class__.__name__}")
                print(f"Об'єм або площа: {figure.volume()}")
            except ValueError as e:
                print(f"Помилка: {e}")
            print("------")
