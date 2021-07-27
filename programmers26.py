def solution(s):
    answer = sorted(list(s), reverse=True)

    answer = ''.join(answer)
    return answer