cars = ['BMW', 'HONDA', 'VW', 'TATA']
carsTemp= cars
carCopyS = cars.copy()

print(id(cars) == id(carCopyS)) # false because, it is shallow copy where it is a new list, but the element have same reference
print(id(carsTemp) == id(cars)) ##true beacuse, it is refernce copy

cars[2] = 'VolksWogan'
print(cars)
print(carsTemp)
print(carCopyS)

