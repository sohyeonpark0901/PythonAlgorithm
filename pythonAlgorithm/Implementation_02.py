N = int(input())

count =0
for i in range (0,N+1):

    for j in range(0,60):

        for k in range(0,60):
            if (str(i)+str(j)+str(k)).count("3"):
                count+=1

print(count)