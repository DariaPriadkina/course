class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    @staticmethod
    def new_rectangle(square):
        for width in range(1, square + 1):
            if square % width == 0:
                height = square // width
                return width, height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        square = self.get_square() + other.get_square()
        width, height = self.new_rectangle(square)
        return Rectangle(width, height)

    def __mul__(self, n):
        square = self.get_square() * n
        width, height = self.new_rectangle(square)
        return Rectangle(width, height)

    def __str__(self):
        return f'Rectangle with height {self.height}, and width {self.width} has an area {self.get_square}'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
print(r1.get_square()) # == 8, 'Test1'
print(r2.get_square()) # == 18, 'Test2'

r3 = r1 + r2
print(r3.get_square()) # == 26, 'Test3'

r4 = r1 * 4
print(r4.get_square()) # == 32, 'Test4'

print(Rectangle(3, 6)) # == Rectangle(2, 9), 'Test5'
