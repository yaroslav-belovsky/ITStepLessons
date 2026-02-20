my_bsket = {}


def add():
    strig_produkt = input("напиши так: назва/ціна - ")
    global x
    global y
    x = ""
    y = ""
    global ended
    ended = False
    integer = False
    for i in list(strig_produkt):
        if i == "/":
            integer = True
            ended = True
            continue
        if integer:
            x += i
        elif integer == False:
            y += i
    if ended == False:
        print("не має /")
        add()
while True:
    answer = input("продовжити?\n1-так, 2-ні\n")
    if answer == "1":
        add()
        weare = y
        my_bsket[weare] = int(x)
    elif answer == "2":
        total = sum(my_bsket.values())
        print("чек")
        for i in my_bsket:
            print(f"       {i}      {my_bsket[i]}")
        print(f"\nвсього: {total} грн")
        break