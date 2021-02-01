## 다시 풀기
N = input("N:")
K = input("K:")
result = 0

a = N/(K*K)
b = N%(K*K)

result=a+1
for i in range (0,b):
    result+=1

print("result:",result)
