from itertools import combinations 
def solution(nums): 
    answer = 0
    
    for i in combinations(nums, 3):
        num = sum(i)
        cnt=0
        
        for p in range(1, num+1):
            if num%p==0:
                cnt+=1
                
        if cnt==2:
            answer+=1

    return answer