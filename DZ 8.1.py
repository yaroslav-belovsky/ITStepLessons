a = input("приклад: ")
if "+" in a:
    action = "+"
    b, c = a.split("+")
    result = int(b) + int(c)
elif "-" in a:
    action = "-"
    b, c = a.split("-")
    result = int(b) - int(c)
elif "*" in a:
    action = "*"
    b, c = a.split("*")
    result = int(b) * int(c)
elif "/" in a:
    action = "/"
    b, c = a.split("/")
    result = int(b) / int(c)
print(int(b), action, int(c), "=", result)