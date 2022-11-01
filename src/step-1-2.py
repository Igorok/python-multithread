import threading
import time
import datetime

def get_data(data):
    for i in range(10):
        print(f'[{threading.current_thread().name}] - {data} - {i}')
        time.sleep(0.5)

now = datetime.datetime.now()
# a simple thread will finish after applying all functions
# thr = threading.Thread(target=get_data, args=(now,), name=f'thr-1')
# a daemon thread will finish together with main thread
thr = threading.Thread(target=get_data, args=(now,), name=f'thr-1', daemon=True)
thr.start()

time.sleep(1)
print('finish')
