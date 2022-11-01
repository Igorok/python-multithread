import threading
import time

# Timer
'''
def test_1():
    for i in range(20):
        print('thread', i)
        time.sleep(1)

# timer - 10 sec
thr_timer_1 = threading.Timer(5, test_1)
thr_timer_1.start()

for i in range(2):
    print('main', i)
    time.sleep(1)

# cancel only if thread not started
thr_timer_1.cancel()
print('finish')
'''

data = threading.local()

def get():
    for i in range(10):
        print(threading.current_thread().name, data.value)
        time.sleep(1)

def t_1():
    data.value = '111'
    get()

def t_2():
    data.value = '222'
    get()

thr_1 = threading.Thread(target=t_1, name='thr_1')
thr_2 = threading.Thread(target=t_2, name='thr_2')

thr_1.start()
thr_2.start()

time.sleep(5)
# main thread has no data.value
print('data.value', data.value)












