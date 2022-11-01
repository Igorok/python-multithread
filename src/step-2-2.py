import multiprocessing
import random
import time

'''
# Lock - можно разблокировать из любого процесса, например из главного разблокировать дочерние, пока они в работе
# lock = multiprocessing.Lock()

# RLock - может разблокировать только тот процесс, который заблокировал
lock = multiprocessing.RLock()

def get_value(l):
    l.acquire()
    p_name = multiprocessing.current_process().name
    print(p_name, ' - started')

for i in range(2):
    prc = multiprocessing.Process(target=get_value, args=(lock,))
    prc.start()
'''

'''
lock = multiprocessing.Lock()
arr = multiprocessing.Array('i', [0 for i in range(10)])

print(1, list(arr))

def add_value(locker, array, index, value):
    # with locker:
    c_time = time.ctime()
    array[index] += value
    print(
        multiprocessing.current_process().name,
        'index', index,
        'value', value,
        'c_time', c_time,
    )

prc_list = []
for i in range(10):
    prc_1 = multiprocessing.Process(target=add_value, args=(lock, arr, i, 1))
    prc_2 = multiprocessing.Process(target=add_value, args=(lock, arr, i, 2))
    prc_3 = multiprocessing.Process(target=add_value, args=(lock, arr, i, 3))
    prc_4 = multiprocessing.Process(target=add_value, args=(lock, arr, i, 4))
    prc_5 = multiprocessing.Process(target=add_value, args=(lock, arr, i, 5))
    prc_list.append(prc_1)
    prc_list.append(prc_2)
    prc_list.append(prc_3)
    prc_list.append(prc_4)
    prc_list.append(prc_5)
    prc_5.start()
    prc_4.start()
    prc_3.start()
    prc_2.start()
    prc_1.start()

for prc in prc_list:
    prc.join()

print(2, list(arr))
'''

# QUEUE
queue = multiprocessing.Queue()


def get_text(q):
    val = random.randint(0, 10)
    q.put(str(val))


prc_list = []
for _ in range(10):
    prc = multiprocessing.Process(target=get_text, args=(queue,))
    prc_list.append(prc)
    prc.start()


for prc in prc_list:
    prc.join()


# for el in iter(queue.get, None):
#     print('el', el)

queue_el = queue.get()
while queue_el != None:
    print('queue_el', queue_el)
    queue_el = queue.get()
