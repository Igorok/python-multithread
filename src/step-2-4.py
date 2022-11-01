import random
import multiprocessing
import time

event = multiprocessing.Event()


'''
def test_event():
    print('test_event launched')
    while True:
        event.wait()
        print('test_event while True')
        time.sleep(1)


def test_event_set():
    while True:
        time.sleep(5)
        event.set()
        print('Event true')
        time.sleep(5)
        event.clear()
        print('Event false')


multiprocessing.Process(target=test_event).start()
multiprocessing.Process(target=test_event_set).start()
'''


cond = multiprocessing.Condition()


def f_1():
    while True:
        with cond:
            cond.wait()
            print('Receive event')


def f_2():
    for i in range(100):
        if i % 10 == 0:
            with cond:
                cond.notify()
        else:
            print('i', i)
        time.sleep(1)


multiprocessing.Process(target=f_1).start()
multiprocessing.Process(target=f_2).start()












