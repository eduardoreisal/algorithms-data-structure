"""
Whats Big O?
Big O is the language and metric we use to describe the efficiency of algorithms

Types:
    O(N); O(N^2), O(2^N)


Complexity          Name            Sample
O(1)                Constant        Accessing a specific element in array
O(N)                Linear          Loop through array of elements
O(LogN)             Logarithmic     Find an element in sorted array
O(N^2)              Quadratic       Looking at every index in the array twice
O(2^N)              Exponential     Double recursion in Fibonacci


How to Measure Code using Big O?

No          Description                                                                                 Complexity
Rule 1      Any assignment statments and if statments that are executed once regardless of the size     O(1)
            of the problem
Rule 2      A simple "for" loop from 0 to n (with no internal loops)                                    O(n)
Rule 3      A nested loop of the same type takes quadratic time complexity                              O(n^2)
Rule 4      A loop, in which the controlling parameter is divided by two at each step                   O(log n)
Rule 5      When dealing with multiple statments, just add them up                                      
"""
