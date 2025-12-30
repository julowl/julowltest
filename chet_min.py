ls= [1,3,5,7,9,11,15]
a=[]
for i in ls:
    if i % 2 ==0:
        a.append(i)
if a:
    result = min(a)
    print(result)
else:
    print("Don't find")