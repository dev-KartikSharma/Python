# Write a Python program that creates two threads to find and print even and odd numbers from 30 to 50.
import threading

def print_even_num():
    print('List of even numbers : ')
    for i in range(30,51,2):
        print(i, end=' ')

def print_odd_num():
    print('\nList of odd numbers : ')
    for i in range(31,51,2):
        print(i, end=' ')

even_thread = threading.Thread(target=print_even_num)
odd_thread = threading.Thread(target=print_odd_num)

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()