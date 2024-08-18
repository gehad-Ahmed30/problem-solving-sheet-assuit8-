def check(x,y):
    flag_year=0
    while x<=y:
        x*=3
        y*=2
        flag_year+=1
    return flag_year

x,y=map(int,input().split())
print(check(x,y))