def check(s1,s2):
    flag_s1=0
    for i in range(len(s2)):
        if s1[flag_s1]==s2[i]:
            flag_s1+=1
    return flag_s1+1

s1=input()
s2=input()
print(check(s1,s2))