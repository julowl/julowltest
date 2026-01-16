hp_file = open("hp01.txt", "r", encoding="utf-8")
character = "potter"
i=1
for line in hp_file:
    if line == "\n":
        i += 1
        continue
    if character.lower() in line.lower():
        print(i, line, end = "")
        break
    i += 1



hp_file = open("hp01.txt", "r", encoding="utf-8")
character = input()
i=1
for line in hp_file:
    if line == "\n":
        i += 1
        continue
    words = line.lower().split()
    if character.lower() in words:
        print(i, line, end = "")
        break
    i += 1

file = "C:/Users/Julia/Desktop/hm/hp01.txt"
hp_file = open("hp01.txt", "r", encoding="utf-8")
character = "Halloween"
i=1
for line in hp_file:
    if line == "\n":
        i += 1
        continue
    if character.lower() in line.lower():
        print(i, line, end = "")
        break
    i += 1