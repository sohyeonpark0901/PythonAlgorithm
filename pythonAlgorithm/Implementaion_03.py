x ,y= input()
xIndex = ['a','b','c','d','e','f','g','h']

dx = [2,1,2,1,-2,-1,-2,-1]
dy = [-1,-2,1,2,-1,-2,1,2]
count = 0
x=(xIndex.index(x))+1
y=int(y)

for i in range(0,len(dx)):
    x=dx[i]+x
    y=dy[i]+y
    if((1<=x<=8)and(1<=y<=8)):
        count+=1

print(count)
