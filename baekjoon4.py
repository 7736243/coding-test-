word = input()
alpha = list(range(97, 123))

for n in alpha:
    print(word.find(chr(n)))