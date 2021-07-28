def solution(answers):
    answer = []
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer2 = [0, 0, 0]
    
    for i in range(len(answers)):
        if(answers[i]==n1[i%len(n1)]):
            answer2[0]+=1
        if(answers[i]==n2[i%len(n2)]):
            answer2[1]+=1
        if(answers[i]==n3[i%len(n3)]):
            answer2[2]+=1
    
    max1 = max(answer2)
    
    for i in range(len(answer2)):
        if max1 == answer2[i]:
            answer.append(i+1)
            
    return answer