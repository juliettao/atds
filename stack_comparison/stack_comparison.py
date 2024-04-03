#!/usr/bin/env python3
"""
stack_comparison.py
the module containing all of the data structures used in ATCS at poly.
"""
__author__ = "Juliet Lord" 
__version__ = "2024-03-04"

from atds import *
import time
import matplotlib.pyplot as plt


def main():
    MIN_TEST_SIZE = 10000
    MAX_TEST_SIZE = 1000000
    test_sizes = []
    stack_test_times = []
    uls_test_times = []
    print("Testing Stack class")
    for test_size in range(MIN_TEST_SIZE, MAX_TEST_SIZE, int(MAX_TEST_SIZE / 10)):
        s = Stack()
        start_time = time.time()
        for i in range(test_size):
            s.push
        for i in range(test_size):
            s.pop()
        stop_time = time.time()
        test_sizes.append(test_size)
        stack_test_times.append(stop_time - start_time)
        
    print("Testing UnorderedListStack class")
    for test_size in range(MIN_TEST_SIZE, MAX_TEST_SIZE, int(MAX_TEST_SIZE / 10)):
        uls = UnorderedListStack()
        start_time = time.time()
        for i in range(test_size):
            uls.push
        for i in range(test_size):
            uls.pop()
        stop_time = time.time()
        uls_test_times.append(test_size, stop_time-start_time)

        fig = plt.figure()
        fig, ax = plt.subplots()
        plt.title("Later")
        plt.ylabel("Time to run (s)")
        plt.xlabel("Stack size (n)")
        ax.scatter(test_sizes, stack_test_times, label="Stack", marker='o', color='r')
        ax.scatter(test_sizes, uls_test_times, label='ULStack', marker="o", color="b")
        ax.legend()
        plt.show()




if __name__ =="__main__":
    main ( )


