def magnets(number):
    flag_sum=1
    for i in range(1,len(number)):
        if number[i] != number[i-1]:
            flag_sum+=1
        
    return flag_sum


n=int(input())
number=[]
for i in range(n):
    N=int(input())
    number.append(N)
print(magnets(number))