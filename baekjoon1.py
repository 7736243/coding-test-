n = int(input())

for i in range(n):
    repeatnum, inputstr = input().split()
    answer = ""
        
    for char in inputstr:
        answer += int(repeatnum) * char
        
    print(answer)