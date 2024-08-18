def check(a):
    flag_sum=0
    for x,y in a:
        if y-x>=2:
          flag_sum+=1
        
    return flag_sum
    
            
n=int(input())
a=[]
for i in range(n):
    N=tuple(map(int,input().split()))
    a.append(N)

print(check(a))
