from tkinter import *

root = Tk()
root.iconbitmap('./logo.ico')
root.title("swiftzy")

userDataFrame = LabelFrame(root, text = "User Data", padx = 20, pady = 20)
userDataFrame.grid(column=0,row=0,padx=5,pady=5)

botListFrame = LabelFrame(root, text = "Bots", padx = 20, pady = 20)
botListFrame.grid(column=0,row=1,padx=5,pady=5)

Label(userDataFrame, text = "Name: Hilogen                     ").grid(row = 0, column = 0)
Label(userDataFrame, text = "Email: example@example.com").grid(row = 0, column = 1)

Button(botListFrame, text = "Add Bot").grid(row = 0, column = 0, padx = 140)

root.mainloop()