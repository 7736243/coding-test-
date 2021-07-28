def solution(a, b):
    import calendar
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    
    now = calendar.weekday(2016, a, b)
    
    return days[now]