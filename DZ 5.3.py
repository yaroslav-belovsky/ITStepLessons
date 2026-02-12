import random as r
a = input("введіть текст: ")
pos = r.randint(0, len(a) - 1)
sym = a[pos]
b = a[0:pos]
c = a[1+pos:]
d = b + c
print(f"символ {sym}, рядок без нього {d}")