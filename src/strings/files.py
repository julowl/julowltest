from os import write

find_world = open("find_word.py", errors = "ignore")  #открыть файл
count = 0
for line in find_world:
    count = count + 1
print(count)

find_world_cups = open("find_word_cups.py", "w", errors = "ignore") #"w"  открыть файл для записи
find_world = open("find_word.py", errors = "ignore") #открыть файл для чтения (если ничего не указать то поумол для чтен)
for line in find_world:
    find_world_cups.write(line.upper()) # записывает по строчно из find_world

clean = open("find_word.py", errors = "ignore")
count = 0
for line in clean:
    count = len(line.split()) + count
print(count)


