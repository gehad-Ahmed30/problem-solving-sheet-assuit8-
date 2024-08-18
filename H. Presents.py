def presents(n,N):
    output=[0] * n      # n=4  [0,0,0,0]
    for i in range(n):
        result=N[i]-1   #convert to 0-based index
        output[result]=i+1    
    print(' '.join(map(str, output)))


n=int(input())
N=list(map(int,input().split()))
presents(n,N)