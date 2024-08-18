def check(number,arr1,arr2):
    sum_arr1=sum(arr1)
    sum_arr2=sum(arr2)

    if sum_arr1==sum_arr2:
        return "Yes"
    else:
        return "No"


number=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(check(number,arr1,arr2))