import json
from tkinter import *

root = Tk()
root.iconbitmap('./logo.ico')
root.title("swiftzy")
selectedBot = None
with open("userdata.json", "r") as f:
    userdata = json.load(f)

def addBot() : 
    pass

def selectBot(userDataFrame, botListFrame):
    userDataFrame.destroy()
    botListFrame.destroy()
    Button(root, text = "revert", command = firstDisplay).grid(row = 0, column = 0)

def loginDisplay():
    loginFrame = LabelFrame(root, text = "Log in/Sign up", padx = 80, pady = 80)
    loginFrame.grid(row = 0, column = 0, padx = 2, pady = 2)
    Label(loginFrame, text = "Username/Email : ").grid(row = 0, column = 0, padx = 3, pady = 2)
    Label(loginFrame, text = "Password : ").grid(row = 1, column = 0, padx = 3, pady = 2)
    usernameEntry = Entry(loginFrame).grid(row = 0, column = 1, padx = 3, pady = 2)
    passwordEntry = Entry(loginFrame).grid(row = 1, column = 1, padx = 3, pady = 2)
    Button(loginFrame, text = "Log In").grid(row = 2, column = 0, padx = 3, pady = 2)
    Button(loginFrame, text = "Sign Up instead").grid(row = 2, column = 1, padx = 3, pady = 2)

def firstDisplay():
    userDataFrame = LabelFrame(root, text = "User Data", padx = 20, pady = 20)
    userDataFrame.grid(column=0,row=0,padx=5,pady=5)

    botListFrame = LabelFrame(root, text = "Bots", padx = 20, pady = 20)
    botListFrame.grid(column=0,row=1,padx=5,pady=5)

    Label(userDataFrame, text = "Name: Hilogen                     ").grid(row = 0, column = 0)
    Label(userDataFrame, text = "Email: example@example.com").grid(row = 0, column = 1)

    Button(botListFrame, text = "Add Bot",command=lambda: addBot()).grid(row = 0, column = 0, pady = 10)

    with open("config.json", "r") as f:
        config = json.load(f)

    botCount = len(config)
    botAddedCount = 1

    while botAddedCount < botCount :
        Button(botListFrame, text = config[botAddedCount]["name"], padx = 140, command = lambda: selectBot(userDataFrame, botListFrame)).grid(row = botAddedCount, column = 0, pady = 3)
        botAddedCount += 1

if (userdata["login"] == True):
    firstDisplay()
elif(userdata["login"] == False):
    loginDisplay()
else:
    print("error")

root.mainloop()