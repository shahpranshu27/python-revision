def fibonacci(num):
    fib_seq = [0,1]
    for i in range(2, num):
        next_term = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_term)
    
    return fib_seq

print(fibonacci(10))