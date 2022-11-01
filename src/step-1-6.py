import threading
import time

event = threading.Event()

'''
def test_event():
    for i in range(20):
        event.wait()
        print('test_event')
        time.sleep(2)

event.clear() # event - false
threading.Thread(target=test_event).start()
'''

# Все потоки ожидающие евента - event.wait()
# Срабатывают при его установке - event.set()
# Например происходит обработка картинок, после обработки 10, срабатывает их загрузка
'''
def image_handler():
    thr_name = threading.current_thread().name
    print('Image processing...', thr_name)
    event.wait()
    print('Image sended', thr_name)

for i in range(10):
    thr = threading.Thread(target=image_handler)
    thr.start()
    print('Thread started', thr.name)
    time.sleep(1)

if threading.active_count() >= 10:
    event.set()
'''

'''
Event блокируется и разблокируется вручную
Condition после оповещения, блокируется снова, и останавливается на cond.wait()
'''
cond = threading.Condition()

def f_1():
    while True:
        with cond:
            cond.wait()
            print('Receive condition')

def f_2():
    for i in range(100):
        if i % 10 == 0:
            with cond:
                cond.notify()
        else:
            print('f_2', i)

threading.Thread(target=f_1).start()
threading.Thread(target=f_2).start()
