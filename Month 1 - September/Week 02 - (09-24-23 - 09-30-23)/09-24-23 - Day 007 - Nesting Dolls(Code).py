anime = input("What's your favorite anime? ")

if anime.lower() in ["dragon ball", "dragonball", "dragon ball z", "dragonballz", "dbz", "dragonball super", "dragon ball super"]:
    print("Now that's the right choice!")

    character = input("Who's your favorite character? ").lower()

    if character == "goku":
        print("Basic but understandable, have a good day.")
    elif character == "vegeta":
        print("After that punch to Beerus I can feel that!")
    elif character == "goten":
        print("That's no one's favorite!")
    elif character == "piccolo":
        print("Gohans dad, a wise choice.")
    elif character == "bulma":
        print("I see vegeta isn't the only one in love.")
    elif character == "krillin":
        print("Whats the dude from xaiolin showdown doing here?")
    elif character == "gohan":
        print("SSJ2 would be enough but now beast mode...")
    elif character == "trunks":
        print("the real question is which version.")
    elif character == "frieza":
        print("Frieza is one of the most iconic villains in anime history.")
    elif character == "cell":
        print("No one should be picking our Hisoka.")
    elif character == "majin buu":
        print("Why though?")
    elif character == "beerus":
        print("A god does seemlike an easy choice.")
    elif character == "whis":
        print("Someone stronger than a god, seems like the easy way out.")
    elif character == "android 17":
        print("Android 17 has proven to be a formidable ally.")
    elif character == "android 18":
        print("Yes.")
    elif character == "yamcha":
        print("#DeathPose")
    elif character == "tien":
        print("him just going off on cell was perfection.")
    elif character == "master roshi":
        print("Maybe don't.")
    elif character == "gotenks":
        print("This may be worse than picking Goten.")
    elif character == "videl":
        print("Videl goes haard!")
    elif character == "mr. popo":
        print("You better be an abridged fan!")
    elif character == "dende":
        print("You better not be an abridged fan!")
    else:
        print("Who's that again?.")
else:
    print("Cool story bro.")