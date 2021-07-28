def solution(numbers, hand):
    answer = []
    ans = [[1, 2, 3],
            [4, 5, 6],
           [7, 8, 9],
           ['*', 0, '#']]
    lh = 30
    rh = 32
    
    def abs(n1):
        if n1<0:
            n1*=-1
        return n1
    
    for i in range(len(numbers)):
        now = numbers[i]
        
        ny, nx = 0, 0
        for i in range(4):
            for j in range(3):
                if ans[i][j]==now:
                    ny = i
                    nx = j         
        
        if now==1 or now==4 or now==7:
            answer.append('L')
        elif now==3 or now==6 or now==9:
            answer.append('R')
        else:
            dis_left = abs(lh//10-ny) + abs(lh%10-nx)
            dis_right = abs(rh//10-ny) + abs(rh%10-nx)
            
            if dis_left == dis_right:
                if hand == 'right':
                    answer.append('R')
                else:
                    answer.append('L')
            elif dis_left < dis_right:
                answer.append('L')
            else:
                answer.append('R')
                
        if answer[-1]=='R':
            rh = ny*10 + nx
        else:
            lh = ny*10 + nx
                
    return ''.join(answer)