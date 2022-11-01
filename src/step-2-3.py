import multiprocessing
import random


def get_value(value):
    print(
        multiprocessing.current_process().name,
        'value', value
    )
    return 1000 + value


def get_few_value(*args):
    return [
        1000 + args[0],
        1000 + args[1],
        1000 + args[2],
    ]


def end_function(result):
    print(result)


if __name__ == '__main__':
    # cpu_count = multiprocessing.cpu_count()
    with multiprocessing.Pool(4) as pool:
        # пул потоков
        # pool.map(get_value, [i for i in range(20)])

        # асинхронный пул с колбэком
        # pool.map_async(get_value, [i for i in range(20)], callback=end_function)
        # pool.close()
        # pool.join()

        values = []
        for i in range(1, 31):
            values.append(i)
            if i % 3 == 0:
                pool.apply_async(func=get_few_value, args=values, callback=end_function)
                values = []

        pool.close()
        pool.join()









