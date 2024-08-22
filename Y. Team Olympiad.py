def check(n,N):
    programming=[]
    math_=[]
    sport=[]

    for i in range(len(N)):
        if N[i]==1:
            math_.append(i+1)
        elif N[i]==2:
            programming.append(i+1)
        elif N[i]==3:
            sport.append(i+1)
    x=min(len(math_),len(programming),len(sport))
    print(x)
    for i in range(x):
       print(math_[i],programming[i],sport[i])
    

n=int(input())
N=list(map(int,input().split()))
check(n,N)
