import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
from tkinter.ttk import *

root = tk.Tk()

import os
pic = open(os.path.expanduser("~/Desktop/UNIVERSITY/NUST/NUST Notes:PDFs/Semester 2/CP Lab/PROJECT/images.png"))
root.iconphoto(False,pic)
root.title("Enigma By Muneeb & Co")

root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

canvas = tk.Canvas(root,height = 500, width=400, bg="White")
canvas.pack()

bold_font = tkfont.Font(family="Helvetica",size=12,weight="bold")

operation1 = tk.Label(root,text= "Enter the Text",width=20,bg="White")
operation1.config(font=bold_font)
canvas.create_window(200,100,window=operation1)
user_text = tk.Entry(root)
canvas.create_window(200,150,window=user_text)

operation2=tk.Label(root,text="Choose an Operation",width=25,bg="White")
operation2.config(font=bold_font)
canvas.create_window(200,200,window=operation2)

v = tk.IntVar()

def choice():
    x = v.get()
    if(x==1):
        encryption()
    elif(x==2):
        decryption()

operation3=tk.Radiobutton(root, text="Encrypt it",padx = 20, variable=v, value=1,command=choice,bg="White")
operation3.config(font=bold_font)
canvas.create_window(100,250,window=operation3)
operation4=tk.Radiobutton(root, text="Decrypt it",padx = 20, variable=v, value=2,command=choice,bg="White")
operation4.config(font=bold_font)
canvas.create_window(300,250,window=operation4)

def encryption():
    plain_text = user_text.get()
    cipher_text = ""
    key = 3
    for i in range(len(plain_text)):
        letter = plain_text[i]
        if(letter.isupper()):
            cipher_text+=chr((ord(letter)+key-65)%26+65)
        else:
            cipher_text+=chr((ord(letter)+key-97)%26+97)
    operation5 =tk.Label(root,text=cipher_text,width=20,bg="White")
    operation5.config(font=bold_font)
    canvas.create_window(200,350,window=operation5)

def decryption():
    cipher_text = user_text.get()
    plain_text = ""
    key = 3
    for i in range(len(cipher_text)):
        letter = cipher_text[i]
        if(letter.isupper()):
            plain_text+=chr((ord(letter)-key-65)%26+65)
        else:
            plain_text+=chr((ord(letter)-key-97)%26+97)
    operation6 =tk.Label(root,text=plain_text,width=20,bg="Black")
    operation6.config(font=bold_font)
    canvas.create_window(200,350,window=operation6)

operation7 =tk.Label(root,text=" Your Converted Text is ",width=20,bg="White")
operation7.config(font=bold_font)
canvas.create_window(200,300,window=operation7)

root.mainloop()
