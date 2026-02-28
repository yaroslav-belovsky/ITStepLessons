import random as r
while True:
    number = r.randint(1, 1000000)
    print("------------------вгадай число!------------------")
    distance = r.randint(1, 10)
    print("вгадай число від одного до мільйона за як умога меншу кількість спроб!\n"
          f"ось підказка: {r.choice([f"я між {number - r.randint(1,10)} і {number + r.randint(1,10)} хто я?",
                                     f"я в районі 10 від числа {r.choice([number - r.randint(1,10), number + r.randint(1,10)])}, вгадай, яке я число?"])}")
    user_number = 0
    sprob = 0
    while user_number != number:
        user_number = float(input("товє число: "))
        sprob += 1
        if user_number > number:
            print("ні твоє число більше за моє!")
        elif user_number < number:
            print("ні твоє число менше за моє!")
    print(f"вітаю! Ти відгадав число! Ти впорався за {sprob} спроб!")
    a = input("хочеш зіграти знову? ")
    if a == "так":
        pass
    elif a == "ні":
        break