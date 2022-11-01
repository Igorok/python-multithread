import time
import threading


value = 0

'''
def inc_value_without_lock():
    global value
    for _ in range(10):
        value += 1
        print(f'{threading.current_thread().name} - {value}')

for i in range(4):
    thr = threading.Thread(target=inc_value_without_lock, name=f'thr-{i}')
    thr.start()
'''

# lock - блокирует и разблокирует любой поток
# rlock - может разблокировать только поток который его заблокировал

'''
locker = threading.Lock()

def inc_value_lock():
    global value
    for _ in range(10):
        locker.acquire()

        value += 1
        print(f'{threading.current_thread().name} - {value}')

        locker.release()

for i in range(4):
    thr = threading.Thread(target=inc_value_lock, name=f'thr-{i}')
    thr.start()
'''

r_locker = threading.RLock()

def inc_value_r_lock():
    global value
    for _ in range(10):
        r_locker.acquire()

        value += 1
        print(f'{threading.current_thread().name} - {value}')

        r_locker.release()

for i in range(4):
    thr = threading.Thread(target=inc_value_r_lock, name=f'thr-{i}')
    thr.start()

print('final value', value)

