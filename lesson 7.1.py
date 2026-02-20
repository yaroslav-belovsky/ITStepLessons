my_bsket = {}


def add():
    strig_produkt = input("напиши так: назва/ціна - ")
    name = ""
    price = ""
    slash = False
    for i in strig_produkt:
        if i == "/":
            slash = True
            continue
        if slash:
            price += i
        else:
            name += i
    if slash == False:
        print("не має /")
        add()
    my_bsket[name] = int(price)

while True:
    answer = input("продовжити?\n1-так, 2-ні\n")
    if answer == "1":
        add()
    elif answer == "2":
        total = sum(my_bsket.values())
        print("чек")
        for name in my_bsket:
            print(f"       {name}      {my_bsket[name]}")
        print(f"\nвсього: {total} грн")
        break