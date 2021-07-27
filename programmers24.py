def solution(s):
    answer = list(s)
    
    if not (len(s)==4 or len(s)==6):
        return False
    
    for i in range(len(s)):
        if not (answer[i]>='0' and answer[i]<='9'):
            return False
        
    return True