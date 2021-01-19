from tkinter import *
from tkinter import messagebox
from UserDashboard import *
from AdminDashBoard import *
from UserBLL import *
from ViewDriversAssignedBookings import *


# Class declaration for login window
class Login:

    def __init__(self):
        # Assigning title, width height and setting window to middle of the screen
        self.loginWindow = Tk()
        self.loginWindow.title("Login")
        windowWidth = 300
        windowHeight = 300
        screenWidth = self.loginWindow.winfo_screenwidth()
        screenHeight = self.loginWindow.winfo_screenheight()
        x = (screenWidth / 2) - (windowWidth / 2)
        y = (screenHeight / 2) - (windowHeight / 2)
        self.loginWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, x, y))

        # Widgets placement in the designed window
        # Label and textfield placement for email
        self.lblEmail = Label(self.loginWindow, text="Please enter your email *")
        self.lblEmail.pack()
        self.txtEmail = Entry(self.loginWindow, width=25, border=3, font=("", 12))
        self.txtEmail.pack()

        self.lbl1 = Label(self.loginWindow, text="")
        self.lbl1.pack()

        # Label and textfield placement for password
        self.lblPassword = Label(self.loginWindow, text="Please enter your password *")
        self.lblPassword.pack()
        self.txtPassword = Entry(self.loginWindow, width=25, border=3, show="*", font=("", 12))
        self.txtPassword.pack()

        self.lbl1 = Label(self.loginWindow, text="")
        self.lbl1.pack()

        #  placement for login button
        self.btnLogin = Button(self.loginWindow, text="Login", pady=10, width=20, padx=10, command=self.loginUser)
        self.btnLogin.config(bg="#1BA160", fg="white")
        self.btnLogin.pack()

        self.loginWindow.mainloop()

    # function to get user input and validate user input
    # Directs user to their specific window based on their usertype after successfull login
    def loginUser(self):
        email = self.txtEmail.get()
        password = self.txtPassword.get()
        userData = UserBLL().loginUser(email, password)
        if userData == 0:
            messagebox.showerror("Access denied", "Invalid username and password")
        else:
            userttype = userData[0][9]
            # normal user login
            if userttype == "user":
                print("User login")
                self.loginWindow.destroy()
                ud = UserDashboard(userData)
            # Driver login
            elif userttype == "driver":
                self.loginWindow.destroy()
                ud = ViewDriversAssignedBookings(userData)
            # Admin login
            elif userttype == "admin":
                self.loginWindow.destroy()
                ud = AdminDashboard(userData)
