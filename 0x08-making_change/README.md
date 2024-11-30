# Project: 0x08. Making Change

Concepts Needed:
Greedy Algorithms:

Understanding how greedy algorithms work and why they are suitable for the coin change problem.
Recognizing the limitations of greedy algorithms and scenarios where they might not provide the optimal solution.
Dynamic Programming:

Basic principles of dynamic programming as a method to solve optimization problems.
The concept of overlapping subproblems and optimal substructure in the context of the coin change problem.
Algorithmic Complexity:

Analyzing the time and space complexity of algorithms.
Striving for solutions with lower complexity to meet runtime constraints.
Problem-Solving Strategies:

Breaking down the problem into smaller, manageable sub-problems.
Iterative vs recursive approaches to dynamic programming.
Python Programming:

Manipulating lists and using list comprehensions.
Implementing functions with efficient looping and conditional statements.

## Result
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$

## Tasks

| Task | File |
| ---- | ---- |
| 0. Change comes from within | [0-making_change.py](./0-making_change.py) |
