def check(s):
    start=ord('a')
    temp=0
    for i in range(len(s)):
        current=ord(s[i])            #convert str to int
        result=abs(current-start)
        if result<=13:
            temp+=result

        else:
            temp+=(26-result)
        start=current

    return temp


s=list(input())
print(check(s))
