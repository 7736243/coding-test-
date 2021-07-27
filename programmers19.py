def solution(s, n):
    answer = ''
    
    for i in range(len(s)):
        if s[i]==' ':
            answer += ' '
        elif s[i].islower():
            e = ord(s[i]) + n
            if e>122:   
                e-=26
            answer += chr(e)
        elif s[i].isupper():
            e = ord(s[i]) + n
            if e>90:   
                e-=26
            answer += chr(e)
            
    return answer