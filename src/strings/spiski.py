hp_file = open("hp01.txt", "r", encoding="utf-8")
word_cnt = {}
for line in hp_file:
    words = line.split()
    for word in words:
        if word not in word_cnt:
            word_cnt[word] = 1
        elif word in word_cnt:
            word_cnt[word] = word_cnt[word] + 1

spisok1 = []
for word in word_cnt:
    spisok1.append((word_cnt[word], word))
spisok1.sort(reverse=True)
print(spisok1[0:4])

