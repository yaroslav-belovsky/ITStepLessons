import random as r


print("гра привидів👻\n"
     "вгадай за якими дверима людина😫\nти привид👻\nє 50 дверей🚪\nє 15 спроб")
raund = 1
human_door = r.randint(1,50)
attempts = 15
while True:
   door = input(f"обирай: ")
   if attempts != 0:
        if door.isdigit():
           door = int(door)
           if human_door == door:
               print(f"в тебе вийшло! ти знайшов людину за {16 - attempts} спроб😰👻")
               break
           elif human_door != door:
               attempts -= 1
               print(f"тут його не має... не здавайся ще {attempts} спроб👻")
           if human_door > door:
               print("твоє привидське чуття підказує що він десь за дверима номер яких більший...")
           elif human_door < door:
               print("твоє привидське чуття підказує що він десь за дверима номер яких менший...")
        else:
            print("та напиши число від одного до п'ятдесяти!!!😡")
   elif attempts == 0:
       print("ой... шкода... ти не знайшов його😢")
       break