a, b = input().split()

an1 = list(a)
an2 = list(b)

an1.reverse()
an2.reverse()

a = "".join(an1)
b = "".join(an2)

if a > b:
    print(a)
else:
    print(b)