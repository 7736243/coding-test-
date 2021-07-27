def solution(arr):
    answer = []
    answer = arr
    
    if len(arr) == 1:
        return [-1]
    else:
        answer.remove(min(answer))

    return answer