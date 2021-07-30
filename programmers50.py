def solution(board, moves):
    answer = 0
    stack = []
    
    for i in moves:
        for j in board:
            if j[i-1]!=0:
                stack.append(j[i-1])
                j[i-1]=0
                break
                
        if len(stack)>=2 and stack[-1] == stack[-2]:
            stack = stack[:-2]  
            answer+=2
        
    return  answer