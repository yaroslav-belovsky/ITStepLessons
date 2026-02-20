string_list = list(input("введи текст "))
sim = ""
number = 0
while len(sim) != 1:
    sim = input("введи ОДИН символ ")
for i in string_list:
    if i == sim:
        number += 1
print(number)