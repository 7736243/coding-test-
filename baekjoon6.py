str1 = input().lower()
strlist = list(set(str1))
cnt = []

for i in strlist:
    count = str1.count(i)
    cnt.append(count)
    
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(strlist[(cnt.index(max(cnt)))].upper())