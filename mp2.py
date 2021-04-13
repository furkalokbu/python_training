import multiprocessing as mp
import time
import os

def whoami(name):
    print("I'm %s, in process %s" % (name, os.getpid()))

def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for num in range(start, stop):
        print("\tNumber %s of %s. Honk!" % (num, stop))
        time.sleep(0.1)

if __name__ == "__main__":
    whoami("main")
    p = mp.Process(target=loopy, args=("loopy",))
    p.start()
    time.sleep(5)
    p.terminate()   
