import time
from multiprocessing import Pipe, Process


def getter(pipe):
    output_c, input_c = pipe
    input_c.close()
    while True:
        try:
            print(output_c.recv())
        except Exception as err:
            print(f'Unexpected {err=}, {type(err)=}')
            break

def setter(sequence, input_c):
    for item in sequence:
        time.sleep(1)
        input_c.send(item)


def get_data_2(conn):
    for i in range(4):
        conn.send('Hello 2')


if __name__ == '__main__':
    output_c, input_c = Pipe()

    prc_get = Process(target=getter, args=((output_c, input_c),))
    prc_get.start()

    setter([i for i in range(3)], input_c)
    output_c.close()
    input_c.close()






















