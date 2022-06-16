cars = ["Buick", "BMW", "Crysler", "Jeep", "GMC"]
print(cars)
cars.append("Lada")
print(cars)

for i in range(len(cars)):
    print(i, cars[i])

print(" ")
cars[3] = "Lamborghini"

for i in range(len(cars)):
    print(i, cars[i])

print(" ")

cars.pop()

for i in range(len(cars)):
    print(i, cars[i])

car = str(input())
if car in cars:
    print(car, "In list")

if car not in cars:
    print(car, "Not In list")
