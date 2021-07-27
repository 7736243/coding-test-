def solution(s):
    answer = list(s)
    idx = 0
    
    for i in range(len(s)):
        if answer[i]==' ':
            idx = 0
        else:
            if idx%2==0:
                answer[i]=answer[i].upper()
            idx+=1

    return ''.join(answer)