def emoji_conveter(message):
    emojis = {":)": "😊", ":(": "😌"}
    worlds = message.split(" ")
    output = ""
    for world in worlds:
        output += emojis.get(world, world) + " "
    return output

message = input("> ")
print(emoji_conveter(message))


#The main difference between functions and methods is that functions are independent and can be called on their own, while methods are associated with a class and can be called only with its instance. This means that you can't call a method without having the instance of a class where that method is defined.¸