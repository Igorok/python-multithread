import time
from multiprocessing.managers import BaseManager


def get_time():
    return time.ctime()


BaseManager.register('get_time_callable', callable=get_time)
manager = BaseManager(address=('127.0.0.1', 3100), authkey=b'pass')
server = manager.get_server()
print('start server')
server.serve_forever()

