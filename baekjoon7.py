a = int(input())
b = int(input())
c = int(input())

sum1 = list(str(a*b*c))

for i in range(10):
    print(sum1.count(str(i)))