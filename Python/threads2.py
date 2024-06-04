import logging
import threading
import time

def thread_function(name):
    logging.info('Thread %s : starting' % name)
    time.sleep(5)
    logging.info('Thread %s : finishing' % name)

if __name__ == "__main__":
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main : ")