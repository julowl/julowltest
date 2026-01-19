hp_file = open("hp01.txt", "r", encoding="utf-8")
letter_count = {}
for line in hp_file:
    for letter in line.lower():
        letter_count[letter] = letter_count.get(letter, 0) + 1

spisok_let = []
for letter in letter_count:
    spisok_let.append((letter_count[letter], letter))
spisok_let.sort(reverse=True)
print(spisok_let[0:49])