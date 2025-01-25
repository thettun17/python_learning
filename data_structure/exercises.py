message = input("> ")
emojis = {
    ":)": "😊",
    ":(": "😌"
}
worlds = message.split(" ")
output = ""
for world in worlds:
    output += emojis.get(world, world) + " "
print(output)