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

def signout(userDataFrame, botListFrame):
    userDataFrame.destroy()
    botListFrame.destroy()
    userdata["login"] = False
    userdata["email"] = ""
    userdata["username"] = ""
    userdata["password"] = ""
    with open("userdata.json", "w") as f:
        json.dump(userdata, f)
    loginDisplay()

def updateInfo(addInfoFrame, infoType, info):
    if(infoType == "email"):
        if(not "@" in info or not "." in info):
            Label(addInfoFrame, text = "* Please enter a valid email.").grid(row = 0, column = 2)
        else:
            userdata[infoType] = info
            with open("userdata.json", "w") as f:
                json.dump(userdata, f)
            addInfoFrame.destroy()
            firstDisplay()
    else:
        userdata[infoType] = info
        with open("userdata.json", "w") as f:
            json.dump(userdata, f)
        addInfoFrame.destroy()
        firstDisplay()

def addInfo(userDataFrame, botListFrame, infoType):
    userDataFrame.destroy()
    botListFrame.destroy()
    addInfoFrame = LabelFrame(root, text = f"Add {infoType}", padx = 80, pady = 80)
    addInfoFrame.grid(row = 0, column = 0, padx = 3, pady = 3)
    Label(addInfoFrame, text = f"Enter {infoType} : ").grid(row = 0, column = 0)
    infoEntry = Entry(addInfoFrame)
    infoEntry.grid(row = 0, column = 1)
    Button(addInfoFrame, text = f"Update current {infoType}", command = lambda: updateInfo(addInfoFrame, infoType, infoEntry.get())).grid(row = 1, column = 1)

def firstDisplay():
    userDataFrame = LabelFrame(root, text = "User Data", padx = 80, pady = 20)
    userDataFrame.grid(column=0,row=0,padx=5,pady=5)

    botListFrame = LabelFrame(root, text = "Bots", padx = 90, pady = 20)
    botListFrame.grid(column=0,row=1,padx=5,pady=5)

    Label(userDataFrame, text = f"Name: "+userdata["username"]+"                     ").grid(row = 0, column = 0)
    Label(userDataFrame, text = f"Email: "+userdata["email"]+"").grid(row = 0, column = 1)

    if(userdata["username"] == ""):
        Button(userDataFrame, text = "Add Username", command = lambda: addInfo(userDataFrame, botListFrame, "username")).grid(row = 1, column = 1)
    elif(userdata["email"] == ""):
        Button(userDataFrame, text = "Add Email", command = lambda: addInfo(userDataFrame, botListFrame, "email")).grid(row = 1, column = 1)

    Button(userDataFrame, text = "Sign Out", command = lambda: signout(userDataFrame, botListFrame)).grid(row = 1, column = 0, pady = 15)

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