import threading
import time
def calculation(x):
    time.sleep(5)
    result = 10+x
    print(result)


def greet_user():
    print('Hello!') 
    time.sleep(10)

if __name__ == "__main__":
    t1 = threading.Thread(target=calculation, args=(5,))
    t2 = threading.Thread(target=greet_user)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
