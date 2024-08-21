def check(n,N):
    for x,y in N:
        if x !=y:
            return "rated"
    for i in range(n-1):
       if N[i][0] < N[i+1][0]:
           return "unrated"
       
       
    return "maybe"


n=int(input())
N=[]
for i in range(n):
    output=tuple(map(int,input().split()))
    N.append(output)

print(check(n,N))


#tuples are generally more memory-efficient than lists, especially when you know that the data does not need to be modified. This can be beneficial when dealing with a large number of participants