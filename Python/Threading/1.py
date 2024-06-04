# Write a Python program to create multiple threads and print their names.

import threading
def print_thread_names():
    print('current thread name is : ', threading.current_thread().name)

threads = []
# to create multiple threads
for i in range(7):
    thread = threading.Thread(target=print_thread_names)
    threads.append(thread)
    thread.start()

# to join all the threads formed earlier
for thread in threads:
    thread.join()