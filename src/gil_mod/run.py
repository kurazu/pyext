"""
2 THREADS:
single thread calc 245.961
single thread calc_release 242.391
2 thread calc 251.481
2 thread calc_release 130.035

4 THREADS:
single thread calc 253.464
single thread calc_release 247.712
4 thread calc 251.756
4 thread calc_release 103.160

single thread calc 242.183
single thread calc_release 242.092
4 thread calc 248.529
4 thread calc_release 98.867
"""
import time
import threading
import functools

from gil import calc, calc_release

REPEAT = 100
INPUT_N = 43
EXPECTED_RESULT = 433494437
THREAD_NUMBER = 4


def measure(repeat, func, arg, expected):
    start = time.time()
    for _ in range(repeat):
        result = func(arg)
        if result != expected:
            raise AssertionError('{} != {} by func {}'.format(
                result, expected, func.__name__
            ))
        assert result == expected
    return time.time() - start


def run_single_thread():
    print('single thread calc {:.3f}'.format(
        measure(REPEAT, calc, INPUT_N, EXPECTED_RESULT)
    ))
    print('single thread calc_release {:.3f}'.format(
        measure(REPEAT, calc_release, INPUT_N, EXPECTED_RESULT)
    ))


def measure_multi_thread(func):
    repeat = REPEAT / THREAD_NUMBER
    repeat_int = int(repeat)
    assert repeat_int == repeat
    target = functools.partial(
        measure, repeat_int, func, INPUT_N, EXPECTED_RESULT
    )

    threads = [threading.Thread(target=target) for _ in range(THREAD_NUMBER)]
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return time.time() - start


def run_multi_thread():
    print('{:d} thread calc {:.3f}'.format(
        THREAD_NUMBER, measure_multi_thread(calc))
    )
    print('{:d} thread calc_release {:.3f}'.format(
        THREAD_NUMBER, measure_multi_thread(calc_release))
    )


def main():
    run_single_thread()
    run_multi_thread()


if __name__ == '__main__':
    main()
