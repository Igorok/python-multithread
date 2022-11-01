import threading
import time
import datetime

def get_data(data):
    for i in range(10):
        print(f'[{threading.current_thread().name}] - {data} - {i}')
        time.sleep(0.5)

thr_list = []

for i in range(3):
    now = datetime.datetime.now()
    thr = threading.Thread(target=get_data, args=(now,), name=f'thr-{i}')
    thr_list.append(thr)
    thr.start()

for t in thr_list:
    t.join()

print('thr_list', thr_list)









