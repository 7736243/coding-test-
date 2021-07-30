def solution(nums):
    answer = 0
    max_cnt = len(nums)//2
    num = len(set(nums))
    
    if max_cnt<num:
        answer = max_cnt
    else:
        answer = num
    
    return answer