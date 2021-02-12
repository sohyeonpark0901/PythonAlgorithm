N = int(input())
input = list(map(str,input().split()))

arr = ["L", "U", "D", "R"]
dx = [0,-1,1,0]
dy = [-1,0,0,1]
result = [1,1]
x=1
y=1
for i in range(0,len(input)):
    index = 0
    for j in range(0,4):

        if input[i] == arr[j] :

            index=j
            x = x + dx[j]
            y = y + dy[j]

            if(1<=x<=N and 1<=y<=N):
                result[0]= x
                result[1]= y
            else:
                x = x-dx[j]
                y = y-dy[j]

print(result)






