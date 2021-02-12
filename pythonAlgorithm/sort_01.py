N, K = list(map(int, input().split()))

A = list(map(int, input().split(',')))
B = list(map(int, input().split(',')))

visited = [0] * N

minA = 0
minB = 0
for i in range(0,N):
    for j in range(0,i):
        if A[i]<A[j]:
            minA = A[i]
            A[i] = A[j]
            A[j] = minA

for i in range(0,N):
    for j in range(0,i):
        if B[i]>B[j]:
            minB = B[i]
            B[i] = B[j]
            B[j] = minB
count = 0
for i in range(0,K):
    count+=B[i]

for i in range(K,N):
    count+=A[i]

print(count)