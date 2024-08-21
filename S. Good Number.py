def check(x,y,n):
    
    output=set(str(i) for i in range(y+1))
    result=set(n)
    return output.issubset(result)

x,y=map(int,input().split())
count=0
for i in range(x):
    n=input()
    if check(x,y,n):
        count+=1


print(count)
    
