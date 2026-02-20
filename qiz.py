from turtle import *

q1 = 'I have 4 legs and a tail. I am very smart.I like to play with you. When I see a cat, I say "Woof, woof" I am… '
q2 = 'I am a pet. I am soft and furry. I like to sleep and drink milk. I do not like mice and dogs. I say "Meow, meow". I am… '
q3 = 'I am a big farm animal. I can be black, white or brown. I like to eat green grass. I give milk. I can say "Moo, moo". I am… '
q4 = 'I have four legs and a tail. I have no teeth. I can swim and dive underwater. I carry my house around with me. I am a… '
q5 = 'I live in the woods. I am very big and furry. I have a big nose,a little tail and four legs. I like to eat fish and berries. I am a… '
qbonus = "I am very large and grey.I have two big ears and two white tusks.I don't have a small nose; I have a long trunk.I can use it to spray water or pick up food.Who am I?"
answer_1 = "dog"
answer_2 = "cat"
answer_3 = "cow"
answer_4 = "turtle"
answer_5 = "bear"
answer_bonus = "elephant"
result = 0
answer = input(q1 + "\n").lower()
if answer == answer_1:
    print("Corect!")
    result += 1
elif answer != answer_1:
    print("No! It is a ", answer_1)
    result -= 1
answer = input(q2 + "\n").lower()
if answer == answer_2:
    print("Corect!")
    result += 1
elif answer != answer_2:
    print("No! It is a ", answer_2)
    result -= 1
answer = input(q3 + "\n").lower()
if answer == answer_3:
    print("Corect!")
    result += 1
elif answer != answer_3:
    print("No! It is a ", answer_3)
    result -= 1
answer = input(q4 + "\n").lower()
if answer == answer_4:
    print("Corect!")
    result += 1
    shape("turtle")
    shapesize(50)
    pensize(25)
    color("red", "orange")
    speed(500)
    right(500)
    answer = input("turtle bonus!!!\n" + qbonus + "\n").lower()
    if answer == answer_bonus:
        print("Corect!")
        result += 1
    elif answer != answer_bonus:
        print("No! It is a ", answer_bonus)
        result -= 1

elif answer != answer_4:
    print("No! It is a ", answer_4)
    result -= 1
answer = input(q5 + "\n").lower()
if answer == answer_5:
    print("Corect!")
    result += 1
elif answer != answer_5:
    print("No! It is a ", answer_5)
    result -= 1
print("yor scor", result)