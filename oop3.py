class Horse:
    def __init__(self, n, num, r):
        self.name = n
        self.number = num
        self.rider = r


class Rider:
    riders = []

    def __init__(self, n):
        self.name = n
        self.riders.append(self.name)


r1 = Rider("Scott")
r2 = Rider("James")
r3 = Rider("Ben")
h = Horse("Stallion", 12, r1)

print(Rider.riders)
