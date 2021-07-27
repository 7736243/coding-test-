def solution(s):
    s = s.lower()
    pcnt = 0
    ycnt = 0
    
    for i in range(len(s)):
        if s[i] == 'p':
            pcnt += 1
        elif s[i] == 'y':
            ycnt += 1
            
    if pcnt == ycnt:
        return True
    else:
        return False