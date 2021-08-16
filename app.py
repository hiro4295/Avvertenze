import json
from tkinter import *

root = Tk()
root.iconbitmap('./logo.ico')
root.title("swiftzy")
selectedBot = None
notProvided = None
with open("userdata.json", "r") as f:
    userdata = json.load(f)
with open("config.json", "r") as f:
    config = json.load(f)

def goBackFromAddBot(addBotFrame):
    addBotFrame.destroy()
    firstDisplay()

def createBot(addBotFrame, name, token):
    if(name == "" or token == ""):
        Label(addBotFrame, text = "* Must enter all the required info.").grid(row = 4, column = 2)
    else:
        botExistsAlready = False
        sl = 1
        while sl < len(config):
            if(config[sl]["name"] == name):
                botExistsAlready = True
            sl += 1

        if(botExistsAlready == True):
            Label(addBotFrame, text = "* Cannot use an existing name for a new bot.").grid(row = 4, column = 2)
        else:
            config.append({"name":name, "token":token})

            with open("config.json", "w") as f:
                json.dump(config, f)
            addBotFrame.destroy()
            firstDisplay()

def addBot(userDataFrame, botListFrame): 
    userDataFrame.destroy()
    botListFrame.destroy()
    addBotFrame = LabelFrame(root, text = "Create a new bot", padx = 10, pady = 10)
    addBotFrame.grid(row = 0, column = 0)
    Button(addBotFrame, text = "Go Back", command = lambda: goBackFromAddBot(addBotFrame)).grid(row = 0, column = 0)
    Label(addBotFrame, text = "Enter Bot Name : ").grid(row = 1, column = 1, pady = 5)
    Label(addBotFrame, text = "Add Bot Token : ").grid(row = 2, column = 1, pady = 5)
    botNameEntry = Entry(addBotFrame)
    botNameEntry.grid(row = 1, column = 2)
    botTokenEntry = Entry(addBotFrame)
    botTokenEntry.grid(row = 2, column = 2)
    Button(addBotFrame, text = "Create Bot", command = lambda: createBot(addBotFrame, botNameEntry.get(), botTokenEntry.get())).grid(row = 3, column = 2)

def selectBot(name):
    userDataFrame.destroy()
    botListFrame.destroy()
    Button(root, text = name, command = firstDisplay).grid(row = 0, column = 0)

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
    global userDataFrame
    global botListFrame

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

    Button(botListFrame, text = "Add Bot",command=lambda: addBot(userDataFrame, botListFrame)).grid(row = 0, column = 0, pady = 10)

    botCount = len(config)
    botAddedCount = 1

    while botAddedCount < botCount :
        exec(f'global {config[botAddedCount]["name"]}Button\n{config[botAddedCount]["name"]}Button = Button(botListFrame, text = config[botAddedCount]["name"], padx = 140, command = lambda: selectBot({config[botAddedCount]["name"]}Button.cget("text")))\n{config[botAddedCount]["name"]}Button.grid(row = botAddedCount, column = 0, pady = 3)')
        botAddedCount += 1

if (userdata["login"] == True):
    firstDisplay()
elif(userdata["login"] == False):
    loginDisplay()
else:
    print("error")

root.mainloop()