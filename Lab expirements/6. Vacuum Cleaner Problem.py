

room = {"A": "Dirty", "B": "Dirty"}
location = "A"

while "Dirty" in room.values():
    print("Location:", location)

    if room[location] == "Dirty":
        room[location] = "Clean"
        print("Action: Suck")
    elif location == "A":
        location = "B"
        print("Action: Right")
    else:
        location = "A"
        print("Action: Left")

print(room)
print("Both rooms are Clean")

