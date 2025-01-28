def emoji_conveter(message):
    emojis = {":)": "😊", ":(": "😌"}
    worlds = message.split(" ")
    output = ""
    for world in worlds:
        output += emojis.get(world, world) + " "
    return output

message = input("> ")
print(emoji_conveter(message))
