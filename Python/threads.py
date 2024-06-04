import threading
import time
# import os 
def print_cube(num):
    print('Cube of number : {}'.format(num**3))
    time.sleep(2)
def print_square(num):
    time.sleep(1)
    print('Square of number : {}'.format(num**2))
if __name__ == "__main__":
    t1 = threading.Thread(target=print_cube, args=(10,))
    t2 = threading.Thread(target=print_square, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Done')