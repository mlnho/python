word = input()

word_2 = ''.join(reversed(word))

if(word == word_2):
    print(1)
else :
    print(0)