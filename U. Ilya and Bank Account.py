def check(n):
    if n>=0:
        return n
    else:
        str_n=str(n)
        result1=int(str_n[:-1])
        result2=int(str_n[:-2]+str_n[-1])

    return max(result1,result2)

n=int(input())
print(check(n))
