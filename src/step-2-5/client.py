from multiprocessing.managers import BaseManager
import time

BaseManager.register('get_time_callable')
manager = BaseManager(address=('127.0.0.1', 3100), authkey=b'pass')

print('client connected')

manager.connect()

server_ans_1 = manager.get_time_callable()
print('server_ans_1', server_ans_1)
time.sleep(1)

server_ans_2 = manager.get_time_callable()
print('server_ans_2', server_ans_2)
