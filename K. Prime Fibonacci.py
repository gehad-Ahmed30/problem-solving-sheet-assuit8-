def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def cal_fibonacci(n):
    fibonacci = [0] * (n + 1)
    fibonacci[1] = 1

    for i in range(2, n + 1):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]
    return fibonacci

number_of_tests = int(input())
test_cases = [int(input()) for _ in range(number_of_tests)]

fib_50 = cal_fibonacci(50)
results = []

for test in test_cases:
    x = fib_50[test]
    if is_prime(x):
        results.append("prime")
    else:
        results.append("not prime")
        
print("\n".join(results))

