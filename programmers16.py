def solution(n):
    answer = 0
    an = n
    
    while(an>0):
        answer += an%10
        an //= 10
        
    return answer