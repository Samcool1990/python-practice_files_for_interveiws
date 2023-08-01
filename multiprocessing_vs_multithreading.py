###Multiprocessing#################################################
import multiprocessing

def prit_cube(num):
    return(num * num * num)

def print_square(num):
    return(num * num)

if __name__ == "__main__":
    #Creating process
    p1 = multiprocessing.Process(target=print_square,args=(10,))
    p2 = multiprocessing.Process(target=prit_cube, args=(10,))
    p1.start()
    p2.start()

    #wait untill process 1 is finished
    p1.join()
    p2.join()

    #Both process finish
    print("Done!!!!")

###Multithreading###################################################
import time
from threading import Thread

num = 0

#The bottleneck of code which is CPU-bound
def upgrade(num):
    while num < 400:
        num += 1

#Creation of multithreads
t1 = Thread(target=upgrade,
             args=(num//2,))
t2 = Thread(target=upgrade, args=(num//2,))

#multithread architecture recording time
start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print("Time Taken ", end - start)