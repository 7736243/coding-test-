def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    plen = len(participant)
    
    for i in range(plen):
        if i == plen-1:
            answer = participant[i]
            break
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    
    return answer