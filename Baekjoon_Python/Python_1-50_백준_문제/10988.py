word = input()
result = 0
word_list = [0]*len(word)
word_list_r = [0]*len(word)
for i in range(len(word)):
    word_list[i] = word[i]
    word_list_r[i] = word[i]
word_list_r.reverse()
for i in range(len(word)):
    if word_list[i] != word_list_r[i]:
        result += 1
if result == 0:
    print("1")
else:
    print("0")