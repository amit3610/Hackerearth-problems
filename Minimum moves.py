for i in range(int(input())):
    x,y=input().split()
    x=int(x)
    y=int(y)
    if(y>x or x<0 or y<0):
        print(-1)
    else:
        print(max(x,y))








