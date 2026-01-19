
word_cnt = dict()# хранит ключ значение , где ключ неизменяемый обьект
hp_file = open("hp01.txt", "r", encoding="utf-8")
for line in hp_file:
    words = line.split()
    for word in words:
        if len(word) > 1:
            second_letter = word[1]
            word_cnt[second_letter] = word_cnt.get(second_letter, 0) + 1
second_letter_list = []
for second_letter in word_cnt:
    second_letter_list.append((word_cnt[second_letter], second_letter))
second_letter_list.sort(reverse=True)
print(second_letter_list[:10])
