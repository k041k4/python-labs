# multiprocessing
import multiprocessing
import os

def whoami(what):
    print("process %s says: %s" % (os.getpid, what))

if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(5):
        p = multiprocessing.Process(target=whoami,
                                    args = ("I'm function %s" % n,))
        p.start()