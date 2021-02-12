"""
a = list(input())

result = []
count = 0
for i in range(0,len(a)):
    if(ord(a[i])<65 or ord(a[i])>90):
        a[i] = (int)(a[i])
        count+=a[i]
    else:
        result.append(a[i])
result.sort()
result.append(count)
"""
print("AA".isalpha())
#print(result)