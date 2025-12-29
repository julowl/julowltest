m=[12,6,15,5,2,7,28,3,10]
current_max = None
for i in m:
    if current_max is None:
        current_max = i
    elif i > current_max:
        current_max = i
print(current_max)

