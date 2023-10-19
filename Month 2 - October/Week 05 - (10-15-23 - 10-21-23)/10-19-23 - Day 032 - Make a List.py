import random

def colorPrint(color, word, hide_space=False):
    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
    }
    end_color = "\033[0m"

    if color in colors:
        print(f"{colors[color]}{word}{end_color}", end=" " if not hide_space else "")
    else:
        print(f"{word}", end=" " if not hide_space else "")

greetings = ["Hello", "Hola", "Bonjour", "Hallo", "Ciao", "Olá", "Hallo", "Привет (Privet)", "你好 (Nǐ hǎo)", "こんにちは (Konnichiwa)", "مرحباً (Marhaban)", "नमस्ते (Namaste)", "Jambo", "안녕하세요 (Annyeong haseyo)", "Γειά σας (Yia sas)", "Merhaba", "שָׁלו֝ם (Shalom)", "สวัสดี (Sawasdee)", "Hej", "Hei", "Hei", "Hej", "Xin chào", "হ্যালো (Helo)", "Γειά σας (Yia sas)", "Cześć", "Salut", "Helló", "Habari", "Sawubona"]
languages = ["English", "Spanish", "French", "German", "Italian", "Portuguese", "Dutch", "Russian", "Chinese - Mandarin", "Japanese", "Arabic", "Hindi", "Swahili", "Korean", "Greek", "Turkish", "Hebrew", "Thai", "Swedish", "Finnish", "Norwegian", "Danish", "Vietnamese", "Bengali", "Greek", "Polish", "Romanian", "Hungarian", "Swahili", "Zulu"]

randomPick = random.randint(0, 29)
colorPrint("blue", f"{greetings[randomPick]}")
colorPrint("white", " : ")
colorPrint("cyan",f"{languages[randomPick]}")