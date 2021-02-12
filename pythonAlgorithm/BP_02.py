import itertools

numbers = "011"

def is_prime_number(x):
    if x ==1 or x ==0:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    count = 0
    temp = []
    for i in range(0, len(numbers)):

        a = list(itertools.permutations(numbers, i+1))
        a= list(set(a))

        for j in a:
            temp.append(int("".join(j)))
            temp = list(set(temp))


    for k in range (0,len(temp)):
        if(is_prime_number(temp[k])):
            count+=1
    return count

print(solution(numbers))