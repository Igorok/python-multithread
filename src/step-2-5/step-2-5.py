import time
import random
import  multiprocessing

# Barrier - stops and waits a limit of processes, and when a count is equal to limit, executes them parallel
'''
bar = multiprocessing.Barrier(5)


def f_1(bar):
    sleep = random.randint(1, 10)
    prc_name = multiprocessing.current_process().name
    print(prc_name, 'sleep', sleep)
    time.sleep(sleep)

    bar.wait()

    print(
        multiprocessing.current_process().name,
        'launched'
    )


for _ in range(12):
    multiprocessing.Process(target=f_1, args=(bar,)).start()
'''

# multiprocessing.Manager позволяет расшаривать списки и объекты между процессами
def f_2(m_dict, m_array):
    m_dict['version'] = 2
    m_dict['description'] = 'test multiprocessing.'

    m_array.append(1)
    m_array.append(2)
    m_array.append(3)


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        d = manager.dict()
        l = manager.list()

        prc = multiprocessing.Process(target=f_2, args=(d, l,))
        prc.start()
        prc.join()

        print(
            'd', d,
            'l', l,
        )































