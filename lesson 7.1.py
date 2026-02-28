my_bsket = {}
my_budget = int(input("який ваш бюджет? "))

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
    else:
        my_bsket[name] = int(price)

while True:
    answer = input("продовжити?\n1-так, 2-ні\n")
    if answer == "1":
        add()
    elif answer == "2":
        total = sum(my_bsket.values())
        print("чек")
        print("бюджет:", my_budget)
        print()
        for name in my_bsket:
            print(f"       {name}      {my_bsket[name]}")
        print(f"\nвсього: {total} грн", end="")
        if total > my_budget:
            print("   ви вийшли з бюджету")
        elif total < my_budget:
            print(f"   ви вписуєтесь в бюджет і маєте ще {my_budget - total} грн в зпасі")
        elif total == my_budget:
            print("   ви на межі по бюджету!")
        break