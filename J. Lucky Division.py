def lucky(n):
    number_lucky=[4,7,44,47,444,447,74,474,477,777,774,744]
    flag=False
    for i in number_lucky:
        if n % i==0:
            flag=True
            continue
    if flag:
        print("YES")   
    else:
        print("NO")

        
n=int(input())
lucky(n)