def check(n,N):
    count=0
    flag=0
    for i in N:
        if i==-1:
            if count>=1:
                count-=1
            else:
                flag+=1
        else:
            count+=i
                   
    return flag
        
n=int(input())
N=list(map(int,input().split()))
print(check(n,N))