# Arrays are not supported by python but we can use lists the same way as we use arrays

array = []
cars = ['volvo','ford','bmw']
for i in cars:
    print(i) 

x = cars[0] # volvo is assigned to the variable x 
print(x)
cars[0] = 'Toyota'
print(x)
print(cars)
cars.append('Audi')
cars.remove('bmw')
print(cars)
# cars.clear()
cars.sort()
print(cars)