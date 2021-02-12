def solution(answers):
    answer = []
    count =[0,0,0]
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(0, len(answers)):
        k1 = i % len(A)
        k2 = i % len(B)
        k3 = i % len(C)
        if A[k1] == answers[i]:
            count[0] += 1
        if B[k2] == answers[i]:
            count[1] += 1
        if C[k3] == answers[i]:
            count[2] += 1

    for i in range(0,len(count)):
        if count[i] == max(count):
            answer.append(i+1)


    return answer


print(solution([1, 3, 2, 4, 2]))