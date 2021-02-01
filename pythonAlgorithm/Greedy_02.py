N = str(input())

result = 1

for i in range(0, len(N)):

    arr = [0]*(len(N))
    arr[i] = int(N[i])
    if i==0 and N[i]=='0':
        arr[i]=0
    if arr[i] == 0 :
        if ([i] == 0 or [i]==1):
            result = arr[0] + arr[1]
        else:
            result += arr[i]
    else:
        result *= arr[i]
        print("result3:", result)


