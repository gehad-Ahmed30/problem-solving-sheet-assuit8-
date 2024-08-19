def check(n):
    max_num=max(n)
    min_num=min(n)
    result=max_num-min_num
    return result

n=list(map(int,input().split()))
print(check(n))