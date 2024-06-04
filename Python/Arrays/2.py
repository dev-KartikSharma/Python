import array as arr
a = arr.array('i',[1,2,3,4,5])
# print(a)
# print(type(a))
print(f'Array before inserting : {a}')
for i in range(0,3):
    print(a[i], end='')
a.insert(1,6) # this will insert 6 at index value 1 
# print(f'Array after inserting : {a}')

b = arr.array('d', [2.5, 3.2, 3.3])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
print()
# b.insert(1,4.4) 
b.append(4.4) # this will add the value to the end of the array
print("Array after insertion : ", end=" ")
for i in (b):
    print(i, end=" ")
print('\r')