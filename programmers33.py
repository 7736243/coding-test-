def solution(numbers):
    answer = []
    lennum = len(numbers)
    
    for i in range(0, lennum):
        for j in range(i+1, lennum):
            num = numbers[i]+numbers[j]
            if num not in answer:
                answer.append(num)
            
    answer.sort()
    
    return answer