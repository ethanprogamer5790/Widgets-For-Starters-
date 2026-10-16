#Import necessary libraries
from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

# Add widgets
# Add label
lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=300)

# Add Label for getting name as input from user
# Use Entry Widget to create a text box for user to enter details
name_lbl = Label(text="Full Name", bg="#3995D3")
name_entry = Entry()

# Function to display a Message
def display():
    # Read input given by user
    name = name_entry.get()
    # Declaring a global variable
    # to make it accesiable anywhere in the program
    global Message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello "+name+"/n"
    # Display details in a text box
    # Specify where to add the detailes inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

# Add a text widget to display infromation/message
text_box = Text(height=3)

# Add buutton and give value of command as name of the functiom
# Press button, display function will be called automatically
btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')

# Organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

# Start the GUI event loop
root.mainloop()