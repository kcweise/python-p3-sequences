#!/usr/bin/env python3

def print_fibonacci(length):
    if length < 0:
        print("Pick positive integer")
    elif length == 0:
        print ([])
    elif length == 1:
        print([0])
    else:
        fib = [0,1]
        for i in range(2, length):
            nex = fib[-1]+fib[-2]
            fib.append(nex)
        print(fib)

    pass