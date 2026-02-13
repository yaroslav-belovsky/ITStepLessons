i = {"name": input("твоє імя "), "things": {input("річ 1 "), input("річ 2 "), input("річ 3 ")}}
character1 = {"name": input("ім'я персонажа1 "), "things": {input("річ 1 "), input("річ 2 "), input("річ 3 ")}}
character2 = {"name": input("ім'я персонажа2 "), "things": {input("річ 1 "), input("річ 2 "), input("річ 3 ")}}
character3 = {"name": input("ім'я персонажа3 "), "things": {input("річ 1 "), input("річ 2 "), input("річ 3 ")}}

print(f"{i["name"]} бере {i["things"]} і команду з героїв {character1["name"], character2["name"], character3["name"]}\n"
      f"{character1["name"]} бере {character1["things"]}\n"
      f"{character2["name"]} бере {character2["things"]}\n"
      f"{character3["name"]} бере {character3["things"]}\n")