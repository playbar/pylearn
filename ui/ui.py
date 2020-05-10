from tkinter import *

root = Tk();

textLabel = Label(root,text="内容", justify=LEFT, padx=10);
textLabel.pack(side=LEFT);
photo = PhotoImage(file='18.png');
imgLabel = Label(root, image=photo);
imgLabel.pack(side=RIGHT)

mainloop();
