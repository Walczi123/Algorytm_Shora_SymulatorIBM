import datetime
from os import stat
import time
from algorithms.shor import find_factor, find_factor_return1st
from cirq_modules.cirq_shor import find_factor_cirq, naive_order_finder, quantum_order_finder
from csv import writer




def test_function(function, number, *args):
    z = None
    n = number
    ans = []
    times = []
    while 1:
        print(f"function {str(function.__name__)}({n}) starts")
        start_time = datetime.datetime.now()
        z = function(n, *args)
        end_time = datetime.datetime.now()
        time_diff = (end_time - start_time)
        times.append(time_diff.total_seconds() * 1000)
        ans.append(z)
        if z is None or z == 1:
            break
        n = n//z
        if n == 1:
            break
    return ans, times


def run_batch_tests():
    NUMBER_SET = [6, 8, 9, 12, 13, 15, 18, 20, 21, 25, 30]
    CORRECT_ANS_SET = [[2, 3], [2, 2, 2], [3, 3], [2, 2, 3], [13],
                       [3, 5], [3, 3, 2], [5, 2, 2], [7, 3], [5, 5], [5, 3, 2]]
    TIMEOUT = 50
    stats = list()
    for r in range(10):
        for number, ans in zip(NUMBER_SET, CORRECT_ANS_SET):
            # run shor's algorithm
            alg_ans, times = test_function(find_factor_return1st,
                                           number, 2, 8, False, TIMEOUT)
            s1 = ("qiskit", number, alg_ans, ans, times)
            stats.append(s1)
            print(s1)

            # run shor's algorithm
            start_time = datetime.datetime.now()
            alg_ans, times = test_function(find_factor_cirq, number,
                                           quantum_order_finder, False)
            s2 = ("cirQ_quantum", number, alg_ans, ans, times)
            stats.append(s2)
            print(s1)

            # run shor's algorithm
            alg_ans, times = test_function(find_factor_cirq, number,
                                           naive_order_finder, False)
            s3 = ("cirQ_naive", number, alg_ans, ans, times)
            stats.append(s3)
            print(s3)

    with open('./tests_results_local.csv', 'a', newline='') as file:
        file_writer = writer(file)
        file_writer.writerows(stats)
        file.close()
