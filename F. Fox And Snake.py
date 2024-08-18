def fox_snake(x,y):
    for i in range(x):
        if i % 2==0:
            print (y * '#')
        elif (i // 2) %2==0:     #even
            print('.' * (y - 1) + '#')
        else:
            print('#' + '.' * (y - 1))
            
x,y=map(int,input().split())
fox_snake(x,y)
