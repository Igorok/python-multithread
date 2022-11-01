import time
import multiprocessing

def test_process():
    for i in range(10):
        print(
            multiprocessing.current_process().name,
            time.ctime()
        )
        time.sleep(1)

prc_1 = multiprocessing.Process(target=test_process)
prc_1.start()
prc_2 = multiprocessing.Process(target=test_process)
prc_2.start()
prc_3 = multiprocessing.Process(target=test_process)
prc_3.start()

print(
    prc_1.name, prc_1.pid, '\n',
    prc_2.name, prc_2.pid, '\n',
    prc_3.name, prc_3.pid, '\n',
)

'''
time.sleep(10)
prc_1.terminate()
prc_2.terminate()
prc_3.terminate()
'''

prc_1.join()
prc_2.join()
prc_3.join()

print('all processes finished')








