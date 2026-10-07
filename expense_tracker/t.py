text = [1, 2, 3, 4, 0]

# res = []
# for i in text:
#     res.append(i + 1)

# res = [i + 1 for i in text]

import string
def ispunctuation(word):
    punctuations = string.punctuation
    return all(char in punctuations for char in word)

word = "item72"
res = []
for i in word:
    res.append((i.isdigit()))
    res.append((ispunctuation(i)))

print(res)
print(all(res))

