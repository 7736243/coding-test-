def solution(n, lost, reserve):
    b = []
    
    for i in reserve:
        for j in lost:
            if i==j:
                b.append(i);
                
    for i in b:
        reserve.remove(i)
        lost.remove(i)
    
    for i in reverse:
        for j in lost:
            if i-1==j or i+1==j:
                lost.remove(j)
                break
                
    answer = n - len(lost)
    return answer