mi = [-1, 3, 0, 5, 8, 9]
current_min = None
for i in mi:
    if current_min is None:
        current_min = i
    if i < current_min:
        current_min=i
print(current_min)

