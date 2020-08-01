#!/usr/bin/env python3

n = int(input("How many fibonacchi numbers do you want to display?\n"))

fib_x = 0
fib_next = 1

if n == 1:
    print(fib_x)

else:
    print(fib_x)

    for i in range(1,n):
        fib_x, fib_next = fib_next, fib_x + fib_next
        print(fib_x)
