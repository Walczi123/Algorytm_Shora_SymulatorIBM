import datetime
from os import stat
import time
from algorithms.shor import find_factor
from cirq_shor import find_factor_cirq, naive_order_finder, quantum_order_finder


NUMBER_SET = [6, 8, 9, 12, 13, 15, 18, 20, 21, 25, 35]
CORRECT_ANS_SET = [[2, 3], [2, 2, 2], [3, 3], [2, 2, 3], [13],
                   [3, 5], [3, 3, 2], [5, 2, 2], [7, 3], [5, 5], [5, 3, 2]]


stats = list()
for number, ans in zip(NUMBER_SET, CORRECT_ANS_SET):
    # run shor's algorithm
    start_time = datetime.datetime.now()
    alg_ans = find_factor(number, 7, 8, False, 100)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    s1 = ("qiskit", number, alg_ans, ans, execution_time)
    stats.append(s1)
    print(s1)

    # run shor's algorithm
    start_time = datetime.datetime.now()
    alg_ans = find_factor_cirq(number, quantum_order_finder, False)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    s2 = ("cirQ_quantum", number, alg_ans, ans, execution_time)
    stats.append(s2)
    print(s1)

    # run shor's algorithm
    start_time = datetime.datetime.now()
    alg_ans = find_factor_cirq(number, naive_order_finder, False)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    s3 = ("cirQ_naive", number, alg_ans, ans, execution_time)
    stats.append(s3)
    print(s3)
