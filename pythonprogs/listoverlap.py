a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = list(set(a + b))
print(c)

d = []
#elements common in both lists

for num in c : 
    if num in a and num in b :
        d.append(num)

print(f"common numbers : {d}")

