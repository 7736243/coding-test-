def solution(lottos, win_nums):
    answer = []
    
    maxcnt = 0
    for i in lottos:
        if i in win_nums:
            maxcnt+=1
        if i ==0:
            maxcnt+=1
    
    mincnt = 0
    for i in lottos:
        if win_nums.count(i) >= 1:
            mincnt+=1
            
    if maxcnt==6:   answer.append(1)
    elif maxcnt==5: answer.append(2)
    elif maxcnt==4: answer.append(3)
    elif maxcnt==3: answer.append(4)
    elif maxcnt==2: answer.append(5)
    else:  answer.append(6)
        
    if mincnt==6: answer.append(1)
    elif mincnt==5: answer.append(2)
    elif mincnt==4: answer.append(3)
    elif mincnt==3: answer.append(4)
    elif mincnt==2: answer.append(5)
    else: answer.append(6)
    
    return answer