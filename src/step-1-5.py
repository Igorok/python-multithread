from random import randint
import threading
import time

# BoundedSemaphore - пул потоков, ограничивает множетсво одновременных потоков
'''
pool = threading.BoundedSemaphore(value=5)

def test_pool():
    for i in range(100):
        randomTime = randint(1, 5)

        with pool:
            print(
                threading.current_thread().name,
                'some action',
                'i', i,
                'randomTime', randomTime
            )
            time.sleep(randomTime)

for i in range(15):
    threading.Thread(target=test_pool).start()
'''

# Barrier - ожидает запуска определенного количества потоков
def test_barrier(barrier):
    randomTime = randint(1, 5)
    time.sleep(randomTime)

    print(
        threading.current_thread().name,
        'launched',
        time.ctime()
    )

    barrier.wait()

    print(
        threading.current_thread().name,
        'continue',
        time.ctime()
    )

barrier = threading.Barrier(5)

for i in range(20):
    threading.Thread(target=test_barrier, args=(barrier,)).start()
