def solution(x):
    num = 0
    ax = x
    
    while (ax>0):
        num += ax%10
        ax = ax // 10
    

    if x%num == 0:
        return True
    else:
        return  False