import math


class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am shape")


class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return 2 * self.width + 2 * self.length


class Square(Shape):
    square_list = []

    def __init__(self, w):
        self.side = w
        self.square_list.append(self.side)
        print("""{} на {} на {} на {}""".format(self.side, self.side, self.side, self.side))

    def calculate_perimeter(self):
        return 4 * self.side

    def change_size(self, val):
        self.side += val


def thesame(obj1, obj2):
    return obj1 is obj2


s = Square(60)
print(s.calculate_perimeter())
s1 = Square(60)

s0 = s

print(thesame(s, s0))
print(thesame(s, s1))
