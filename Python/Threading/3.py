# Write a Python program to calculate the factorial of a number using multiple threads
import threading

def factorial(num):
    result  = 1
    for i in range(1,num+1):
        result *= i 
    print(result)

def calculate_factorial(num):
    print(f'Calculating factorial of {num} by thread ', threading.current_thread().name)
    result = factorial(num)
    print(f'Factorial of number {num} : {result}')

num = int(input('Enter your number : '))
thread1 = threading.Thread(target=calculate_factorial, args=(num,))
thread2 = threading.Thread(target=calculate_factorial, args=(num,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()