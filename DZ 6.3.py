message = [("We ",),"rec",{"r":"o"},{"o":"r"},{"m1":"ded "},{"m3":["a "], "m4":{"m5": "UFO"}}]

answer = message[0][0] + message[1] + message[2]["r"] + message[3]["o"] + message[4]["m1"] + message[5]["m3"][0] + message[5]["m4"]["m5"]
print(answer)