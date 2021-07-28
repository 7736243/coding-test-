def solution(N, stages):
    answer = {}
    people = len(stages)
    
    for i in range(1, N+1):
        if people != 0:
            cnt = stages.count(i)
            answer[i] = cnt / people
            people -= cnt
        else:
            answer[i] = 0
        
    return sorted(answer, key=lambda a: answer[a], reverse=True)