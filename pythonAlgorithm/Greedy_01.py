## 다시 풀기
N,K = map(int, input().split())
count = 0

while True:
    a =  N % K
    if a != 0:
        count = count +1
        N = N - 1
    else:
        N = N // K
        count += 1
    if N <= 1:
        break

print("result:", count)
