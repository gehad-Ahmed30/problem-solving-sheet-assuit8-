def isprime(num):
    if num <2:
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
    return True

def nextprime(n):
    num=n+1
    while not isprime(num):
        num+=1
    return num


x,y=map(int,input().split())

if nextprime(x)==y:
    print("YES")
else:
    print('NO')