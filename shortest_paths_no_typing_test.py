from shortest_paths_no_typing import shortest_paths

import sys
import threading

import os

sys.setrecursionlimit(10 ** 9)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

os.chdir("C:\\Users\\ksuzu2\\PycharmProjects\\Algorithms on Graphs\\week4_paths2\\3_shortest_paths")

cwd = os.getcwd()

test_dir = 'tests'
files = os.listdir(cwd + '\\' + test_dir)


print(os.listdir())

test_inputs = files[::2]
test_outputs = files[1::2]

test_input_and_output = list(zip(test_inputs, test_outputs))

for test_input, test_output in test_input_and_output:
    print(f"test_input={test_input} test_output={test_output}")
    input_file = open(test_dir + '\\' + test_input)
    output_file = open(test_dir + '\\' + test_output)

    input_contents = input_file.read()
    data = list(map(int, input_contents.split()))
    print(f"all data={data}")
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    # data = data[3 * m:]
    adj = [[] for _ in range(n)]
    # cost = [[] for _ in range(n)]
    cost = [dict() for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        # cost[a - 1].append(w)
        cost[a - 1][b - 1] = w

    data = data[3 * m:]
    s = data[0]
    s -= 1

    print(f"adj={adj}")
    print(f"cost={cost}")
    print(f"s={s}")

    distance = [float('inf')] * n
    # reachable = [0] * n
    reachable = set()
    # shortest = [1] * n
    shortest = set()
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    print(f"adj={adj}")
    print(f"cost={cost}")
    print(f"s={s}")
    print(f"distance={distance}")
    print(f"reachable={reachable}")
    print(f"shortest={shortest}")

    for x in range(n):
        # if x not in reachable:
        if distance[x] == float("inf"):
            actual_result = '*'
        elif x in shortest:
            actual_result = '-'
        else:
            actual_result = str(distance[x])

        expected_result = output_file.readline().strip()
        print(f"expected_result=={expected_result}; actual_result=={actual_result}")
        assert actual_result == expected_result
