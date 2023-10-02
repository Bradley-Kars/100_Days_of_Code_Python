exit = ""
while exit != "yes":
    animal = input("What animal would you like to hear? ")
    if animal.lower() == "cow":
        print("The cow goes moo")
    elif animal.lower() == "pig":
        print("The pig goes oink")
    elif animal.lower() == "dog":
        print("The dog goes woof")
    elif animal.lower() == "cat":
        print("The cat goes meow")
    elif animal.lower() == "horse":
        print("The horse goes neigh")
    elif animal.lower() == "chicken":
        print("The chicken goes cluck")
    elif animal.lower() == "rooster":
        print("The rooster goes crow")
    elif animal.lower() == "fish":
        print("The fish goes glub")
    elif animal.lower() == "bear":
        print("The bear goes roar")
    elif animal.lower() == "bird":
        print("The bird goes chirp")
    elif animal.lower() == "snake":
        print("The snake goes hiss")
    elif animal.lower() == "lion":
        print("The lion goes roar")
    elif animal.lower() == "turkey":
        print("The turkey goes gobble")
    elif animal.lower() == "wolf":
        print("The wolf goes howl")
    elif animal.lower() == "duck":
        print("The duck goes quack")
    elif animal.lower() == "monkey":
        print("The monkey goes chatter")
    elif animal.lower() == "lobster":
        print("The lobster goes click")
    elif animal.lower() == "dolphin":
        print("The dolphin goes squeak")
    elif animal.lower() == "bison":
        print("The bison goes bellow")
    elif animal.lower() == "fox":
        print("The fox goes yip")
    else:
        print("You're just being difficult, aren't you?")
    exit = input("Would you like to exit?: ")