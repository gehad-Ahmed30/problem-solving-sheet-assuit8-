def check(x,y,output):
    sum_num=y
    count=0
    for i in output:
        action,num=i
        num=int(num)
        if action== '+':
            sum_num+=num
        elif num < sum_num and action =='-':
            sum_num-=num
        else:
            count+=1
    return sum_num,count


x,y=map(int,input().split())
output=[]
for i in range(x):
    output.append(input().split())
result=check(x,y,output)
print(result[0],result[1])