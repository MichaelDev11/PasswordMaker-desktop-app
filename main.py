from tkinter import *
import tkinter as tk
import os
import random
import datetime

def main():
    root = Tk()
    root.title("PassGenerator")
    root.geometry("300x200")

    #This function here creates a file if it is not already existing and also creates the passwords to be stored in the file
    def Generate():
            date = datetime.datetime.now()
            password = ""
            includeSpecs = includee.get()
            desktopPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive') + str("\\Desktop")
            fileAdd = desktopPath + "\\passwords.txt"
            if not os.path.exists(fileAdd):
                with open (os.path.join(desktopPath, "passwords.txt"), "w") as fp:
                    pass
            
            length = int(passLength.get())
            

            chars = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHKLZXCVBNM"
            specChars = "!@#$%^&*()?"

            def split(chars):
                return [char for char in chars]

            characters = split(chars)

            def split(specChars):
                return [char for char in specChars]

            specialCharacters = split(specChars)

            if (includeSpecs == 1):
                if (length % 2 != 0):
                    length -= 0.5
                    lengthn = int(length)
                    for i in range (lengthn):
                        c = random.choice(characters)
                        z = random.choice(specialCharacters)
                        password += str(c) + str(z)
                    cheatHA = random.choice(specialCharacters)
                    password += str(cheatHA)
                if (length % 2 == 0):
                    for i in range (length):
                        c = random.choice(characters)
                        z = random.choice(specialCharacters)
                        password += str(c) + str(z)
                with open (fileAdd, "a") as f:
                    f.write("Passwords created by PassGenerator on " + str(date) + "\n")
                    f.write("Generated Password for " + str(passPurpose.get()) + ": " + str(password) + "\n\n")
            if (includeSpecs == 0):
                for i in range(length):
                    c = random.choice(characters)
                    password += str(c)
                with open (fileAdd, "a") as f:
                    f.write("Passwords created by PassGenerator on " + str(date) + "\n")
                    f.write("Generated Password for " + str(passPurpose.get()) + ": " + str(password) + "\n\n")

    includee = IntVar()
    
    # These are important to allow the specific labels and entries to be included on the GUI for the user to interact with.
    includeSpecsBox = tk.Checkbutton(root, variable=includee, text="Include Special Characters", onvalue=1, offvalue=0)
    includeSpecsBox.pack()

    passLabel = Label(root, width=80, justify=CENTER, text="What is your desired password length?")
    passLabel.pack()
    passLength = Entry(root, width=40, justify=CENTER)
    passLength.pack()

    purpLabel = Label(root, width=80, justify=CENTER, text="What application is this password for?")
    purpLabel.pack()
    passPurpose = Entry(root, width=40, justify=CENTER)
    passPurpose.pack()

    createButton = Button(root, text="Create Password", command=Generate, width=20)
    createButton.pack()

    root.mainloop()

main()
