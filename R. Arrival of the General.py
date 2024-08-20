def check(n,N):
    x=len(N)
    max_num=max(N)
    result_max=N.index(max_num)

    min_num=min(N)
    result_min=x-1-N[::-1].index(min_num)

    sum_swap=result_max+(n-1-result_min)

    if result_max>result_min:
        sum_swap-=1
    return sum_swap


n=int(input())
N=list(map(int,input().split()))
print(check(n,N))
