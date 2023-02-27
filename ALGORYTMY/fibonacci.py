# Fibonacci rekurencyjnie
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
        print(fib(n-1) + fib(n-2))


print(fib(10))


# Fibonacci iteracyjnie
def fib(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a + b
        return b


print(fib(10))


def fib_seq(n):
    fibs = [0, 1]
    while fibs[-1] <= n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:-1]


print(fib_seq(10))
