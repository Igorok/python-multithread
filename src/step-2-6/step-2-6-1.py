import time
import multiprocessing
from multiprocessing import Pipe, Process


def get_data_1(conn):
    conn.close()
    conn.send('Hello 1')


def get_data_2(conn):
    for i in range(4):
        conn.send('Hello 2')


if __name__ == '__main__':
    output_c, input_c = Pipe()
    Process(target=get_data_1, args=(input_c,)).start()
    Process(target=get_data_2, args=(input_c,)).start()

    print('output_c:', output_c.recv())
    print('output_c:', output_c.recv())
    print('output_c:', output_c.recv())

