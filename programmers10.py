def solution(n, m):
    answer = []
    
    def getgcd(a, b):
        c = 0
        while(1):
            c = a%b
            if c==0:
                return b
            a = b
            b = c
            
    gcd = getgcd(n, m)
    answer.append(gcd)
    answer.append(n*m/gcd)
    
    return answer