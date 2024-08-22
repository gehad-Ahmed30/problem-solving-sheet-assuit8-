import math

fib = [0] * 51
fib[1] = 0  
fib[2] = 1  

for i in range(3, 51):
    fib[i] = fib[i - 1] + fib[i - 2]

prime_status = ["not prime"] * 51

for i in range(1, 51):
    num = fib[i]
    if num > 1: 
        is_prime = True
        if num == 2 or num == 3:
            is_prime = True
        elif num % 2 == 0 or num % 3 == 0:
            is_prime = False
        else:
            for j in range(5, int(math.sqrt(num)) + 1, 6):
                if num % j == 0 or num % (j + 2) == 0:
                    is_prime = False
                    break
        if is_prime:
            prime_status[i] = "prime"

T = int(input())  
results = []

for _ in range(T):
    N = int(input())
    results.append(prime_status[N])

print("\n".join(results))


