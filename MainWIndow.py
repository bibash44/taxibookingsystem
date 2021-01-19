from RegisterWindow import *
import tkinter as tk


# Class declaration for main window
class MainWindow:
    def __init__(self):
        # Assigning title, width height and setting window to middle of the screen
        self.mainWindow = tk.Tk()
        self.mainWindow.title("Main window")
        windowWidth = 300
        windowHeight = 300
        screenWidth = self.mainWindow.winfo_screenwidth()
        screenHeight = self.mainWindow.winfo_screenheight()
        x = (screenWidth / 2) - (windowWidth / 2)
        y = (screenHeight / 2) - (windowHeight / 2)
        self.mainWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, x, y))

        # Widgets placement in the designed window
        self.lbl1 = Label(self.mainWindow, text="")
        self.lbl1.pack()
        self.lbl1 = Label(self.mainWindow, text="")
        self.lbl1.pack()

        #  placement for login button
        self.btnLogin = Button(self.mainWindow, text="Login", pady=10, width=20, padx=10, command=self.loginUser)
        self.btnLogin.config(bg="#1BA160", fg="white")
        self.btnLogin.pack()

        self.lbl1 = Label(self.mainWindow, text="OR")
        self.lbl1.pack()

        #  placement for register button
        self.btnRegisterr = Button(self.mainWindow, text="Register", pady=10, width=20, padx=10,
                                   command=self.registerUser)
        self.btnRegisterr.config(bg="#136AA9", fg="white")
        self.btnRegisterr.pack()
        self.mainWindow.mainloop()

    # Function to open login window
    def loginUser(self):
        self.mainWindow.destroy()
        llg = Login()

    # FUnction to open register window
    def registerUser(self):
        self.mainWindow.destroy()
        rrg = Register()


MainWindow()
