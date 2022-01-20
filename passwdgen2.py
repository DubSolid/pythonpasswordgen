import random
import string
from tkinter import *

#GUI setup
window = Tk(className=' PassGen')
window.geometry("400x300")

#ascii chars definition
length = 20
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#password generation 
def generate():
    all = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(all,length))
    return password
password = generate()

#printing out password to both a txt file and GUI
def printpasswd():
    generated_password = generate()
    outF = open("generated-passwords.txt", "a")
    outF.write(generated_password + "\n")
    outF.close()
    label_var = StringVar()
    label_var.set(generated_password)
    my_label = Label(master=window, width=100, height=1, textvar=label_var)
    my_label.pack()

#button to generate password in GUI
button = Button(
    master=window,
    text = "Generate password",
    width=15,
    command=printpasswd,
)
button.pack()

window.mainloop()
