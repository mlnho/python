import sys

# baekjoon
word = sys.stdin.readline().strip()

# all -1
alphabet = [-1] * 26

# word_list = []
#
# for i in range(len(word)):
#     word_list.append(ord(word[i]) - 97)

for i in range(len(word)):
    word_index = ord(word[i]) - 97
    if alphabet[word_index] == -1:
        alphabet[word_index] = i

print(*alphabet)
