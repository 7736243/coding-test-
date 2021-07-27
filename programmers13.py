def solution(n):
    answer = 0
    num = n**(1/2)
    
    if num%1==0:
        answer = (num+1)**2
    else:
        answer = -1
    
    return answer