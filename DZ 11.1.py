from turtle import *

speed(0)

colors = ["red", "purple", "blue", "green", "orange", "yellow", "skyblue", "limegreen"]

for i in range(500):
    pencolor(colors[i % len(colors)])

    width(i / 100 + 1)
    forward(i)

    left(59)

input()