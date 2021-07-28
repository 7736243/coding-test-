def solution(new_id):
    result = ''
    
    new_id = new_id.lower()
    
    for i in range(len(new_id)):
        now  = new_id[i]
        if now.islower() or now.isdigit() or now=='-' or now=='_' or now=='.':
            result += now
    
    while True:
        if '..' in result:
            result = result.replace('..', '.', len(result))
        else:
            break
            
    result = result.strip('.')
    
    if result == '':
        result = 'a'
        
    if len(result)>=16:
        result = result[0:15]
    result = result.strip('.')
    
    while True:
        if len(result)<=2:
            result += result[-1]
        else:
            break
            
    return result