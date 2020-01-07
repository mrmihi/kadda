import re
from tkinter import *

root = Tk()

root.title("කඩ්ඩ ජයගමු !")
root.iconbitmap("bomb.ico")
def sub ():

    string =string_b.get()
    print(string)
    pattern = r'. '
    new = re.sub(pattern, '.', string)
    pattern = "\."
    up = re.sub(pattern, ". ", new)
    print(up)
    string_2 = Label(root, text="Saved to kadda.txt in directory.").grid(row=1, column=1)


    file = open ("kadda.txt", "w")
    file.write(up)
    file.close()

string_2 = Label(root, text="Visit bocca.xyz for more").grid(row=0, column=1)
#string_l = Label(root, text="sting").grid(row = 1, column =1)
string_b = Entry(root)
string_b.insert(END, 'කඩ්ඩ ඇතුලත් කරන්න ')
string_b.grid(row = 1 , column= 0)

#BUTTON
submit = Button(root, text ="කඩ්ඩ හදන්න " ,command = sub)
submit.grid(row =3 , column = 0)

root.mainloop()
