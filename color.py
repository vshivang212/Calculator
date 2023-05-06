import os 

os.system("cls")



def colorText(text):
    for colors in COLORS:
        text = text.replace("[[" + colors +"]]", Colors[colors])
    return text

hello = "[[RED]hello [BLUE]]world[[WHITE]]"

f = open("calculatorimage.txt", "+r")
ascii = "".join(f.readlines())
print(colorText(ascii))