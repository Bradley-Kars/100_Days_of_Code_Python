import my_library as mylib

sentence = "Sphinx of black quartz, judge my vow."
mylib.rainbowPrint(sentence)

print()

mylib.colorPrint("red", "This", hide_space=False)
mylib.colorPrint("green", "is", hide_space=False)
mylib.colorPrint("cyan", "a", hide_space=False)
mylib.colorPrint("magenta", "test", hide_space=True)
mylib.colorPrint("white", ".", hide_space=True)

print()
print()

mylib.rollDice(20)