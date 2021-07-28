def solution(array, commands):
    answer = []
    
    def change(arr, i, j, k):
        arr = arr[i-1:j]
        arr.sort()
        return arr[k-1]
        
    for i, j, k in commands:
        answer.append(change(array, i, j, k))
    
    return answer