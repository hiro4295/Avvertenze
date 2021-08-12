from tkinter import *

root = Tk()
root.iconbitmap('./logo.ico')
root.title("swiftzy")

def enter():
    label_message = Label(frame, text = message_input.get())
    label_message.grid(column=0,row=1)

frame = LabelFrame(root, text="Avvertenze", padx=480, pady=480)
frame.grid(column=0,row=0,padx=5,pady=5)

message_input = Entry(frame, width=100,borderwidth=5)
message_input.grid(column=9,row=0, columnspan=6, padx=10, pady=10)

button_1 = Button(frame, text = "text",command= enter)
button_1.grid(column=1, row=1)

root.mainloop()