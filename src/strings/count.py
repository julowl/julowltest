
word_cnt = dict()# хранит ключ значение , где ключ неизменяемый обьект
hp_file = open("hp01.txt", "r", encoding="utf-8")
for line in hp_file:
    words = line.split()
    for word in words:
        if word not in word_cnt:
            word_cnt[word] = 1
        elif word in word_cnt:
            word_cnt[word] = word_cnt[word] + 1
print(word_cnt.get("potter"))

popular_word = None
for word in word_cnt:
    if popular_word is None:
        popular_word = word
    if word_cnt[word] > word_cnt[popular_word]:
        popular_word = word
print(popular_word, word_cnt[popular_word])
