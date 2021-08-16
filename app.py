import json
from tkinter import *

root = Tk()
root.iconbitmap('./logo.ico')
root.title("swiftzy")
selectedBot = None
notProvided = None
with open("userdata.json", "r") as f:
    userdata = json.load(f)

def addBot() : 
    pass

def selectBot(userDataFrame, botListFrame):
    userDataFrame.destroy()
    botListFrame.destroy()
    Button(root, text = "revert", command = firstDisplay).grid(row = 0, column = 0)

def signup():
    pass

def login(username, password, loginFrame):

    if (username == ""):
        notProvided = Label(loginFrame, text = "* Must fill all the required fields.")
        notProvided.grid(row = 3, column = 1)
    
    elif (password == ""):
        notProvided = Label(loginFrame, text = "* Must fill all the required fields.")
        notProvided.grid(row = 3, column = 1)

    else:

        if("@" in username and "." in username):
            userdata["email"] = username
        else:
            userdata["username"] = username
    
        userdata["password"] = password
        userdata["login"] = True

        with open("userdata.json", "w") as f:
            json.dump(userdata, f)
    
        loginFrame.destroy()

        firstDisplay()

def loginDisplay():
    loginFrame = LabelFrame(root, text = "Log In/Sign Up", padx = 80, pady = 80)
    loginFrame.grid(padx = 3, pady = 3)
    usernameEntry = Entry(loginFrame)
    usernameEntry.grid(row = 0, column = 1, padx = 3, pady = 2)
    passwordEntry = Entry(loginFrame)
    passwordEntry.grid(row = 1, column = 1, padx = 3, pady = 2)
    Label(loginFrame, text = "Username/Email : ").grid(row = 0, column = 0, padx = 3, pady = 2)
    Label(loginFrame, text = "Password : ").grid(row = 1, column = 0, padx = 3, pady = 2)
    Button(loginFrame, text = "Log In", command = lambda: login(usernameEntry.get(), passwordEntry.get(), loginFrame)).grid(row = 2, column = 0, padx = 3, pady = 2)
    Button(loginFrame, text = "Sign Up instead", command = lambda: signup()).grid(row = 2, column = 1, padx = 3, pady = 2)

def firstDisplay():
    userDataFrame = LabelFrame(root, text = "User Data", padx = 20, pady = 20)
    userDataFrame.grid(column=0,row=0,padx=5,pady=5)

    botListFrame = LabelFrame(root, text = "Bots", padx = 20, pady = 20)
    botListFrame.grid(column=0,row=1,padx=5,pady=5)

    Label(userDataFrame, text = f"Name: "+userdata["username"]+"                     ").grid(row = 0, column = 0)
    Label(userDataFrame, text = f"Email: "+userdata["email"]+"").grid(row = 0, column = 1)

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