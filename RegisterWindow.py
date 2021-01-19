from LoginWindow import *
from tkinter import *
from tkinter import messagebox
import re
from UserBLL import *


# Class declaration for register window
class Register:
    def __init__(self):
        # Assigning title, width height and setting window to middle of the screen
        self.registerWindow = Tk()
        self.registerWindow.title("Register user")
        windowWidth = 750
        windowHeight = 750
        screenWidth = self.registerWindow.winfo_screenwidth()
        screenHeight = self.registerWindow.winfo_screenheight()
        x = (screenWidth / 2) - (windowWidth / 2)
        y = (screenHeight / 2) - (windowHeight / 2)
        self.registerWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, x, y))

        # Widgets placement in the designed window
        # Label and text field placement for name
        self.lblName = Label(self.registerWindow, text="Please enter your name *")
        self.lblName.pack()
        self.txtName = Entry(self.registerWindow, width=25, border=3, font=("", 12))
        self.txtName.pack()

        self.lbl1 = Label(self.registerWindow, text="")
        self.lbl1.pack()

        # Label and textfield placement for email
        self.lblEmail = Label(self.registerWindow, text="Please enter your email *")
        self.lblEmail.pack()
        self.txtEmail = Entry(self.registerWindow, width=25, border=3, font=("", 12))
        self.txtEmail.pack()

        self.lbl1 = Label(self.registerWindow, text="")
        self.lbl1.pack()

        # Label and textfield placement for phone
        self.lblPhone = Label(self.registerWindow, text="Please enter your phone number *")
        self.lblPhone.pack()
        self.txtPhone = Entry(self.registerWindow, width=25, border=3, font=("", 12))
        self.txtPhone.pack()

        self.lbl1 = Label(self.registerWindow, text="")
        self.lbl1.pack()

        # Label and textfield placement for address
        self.lblAddress = Label(self.registerWindow, text="Please enter your address *")
        self.lblAddress.pack()
        self.txtAddress = Entry(self.registerWindow, width=25, border=3, font=("", 12))
        self.txtAddress.pack()

        self.lbl1 = Label(self.registerWindow, text="")
        self.lbl1.pack()

        # Label and option menu placement for gender
        self.genderVar = StringVar(self.registerWindow)
        self.chooseGender = ['Male', 'Female']
        self.genderVar.set(self.chooseGender[0])
        self.lblGender = Label(self.registerWindow, text="Please select your gender *")
        self.lblGender.pack()
        self.genderDropDown = OptionMenu(self.registerWindow, self.genderVar, *self.chooseGender)
        self.genderDropDown.config(width=30)
        self.genderDropDown.pack()

        self.lbl1 = Label(self.registerWindow, text="")
        self.lbl1.pack()

        # Label and textfield placement for payment
        self.paymentVar = StringVar(self.registerWindow)
        self.choosePayment = ['Cash', 'Online']
        self.paymentVar.set(self.choosePayment[0])
        self.lblPayment = Label(self.registerWindow, text="Please select your payment method *")
        self.lblPayment.pack()
        self.paymentDropDown = OptionMenu(self.registerWindow, self.paymentVar, *self.choosePayment)
        self.paymentDropDown.config(width=30)
        self.paymentDropDown.pack()

        self.lbl1 = Label(self.registerWindow, text="")
        self.lbl1.pack()

        # Label and option menu placement for usertype
        self.usertypeVar = StringVar(self.registerWindow)
        self.chooseUserType = ['user', 'driver']
        self.usertypeVar.set(self.chooseUserType[0])
        self.lblUserType = Label(self.registerWindow, text="Please select your user type *")
        self.lblUserType.pack()
        self.usertypeDropDown = OptionMenu(self.registerWindow, self.usertypeVar, *self.chooseUserType,
                                           command=self.userTypeOptionChange)
        self.usertypeDropDown.config(width=30)
        self.usertypeDropDown.pack()

        self.lbl1 = Label(self.registerWindow, text="")
        self.lbl1.pack()

        # Label and textfield placement for license plate number
        self.lbllicensePlate = Label(self.registerWindow, text="Please enter your license plate *")
        self.lbllicensePlate.pack()
        self.txtlicensePlate = Entry(self.registerWindow, width=25, border=3, state="disabled", font=("", 12))
        self.txtlicensePlate.pack()

        self.lbl1 = Label(self.registerWindow, text="")
        self.lbl1.pack()

        # Label and textfield placement for password
        self.lblPassword = Label(self.registerWindow, text="Please enter your password *")
        self.lblPassword.pack()
        self.txtPassword = Entry(self.registerWindow, width=25, border=3, show="*", font=("", 12))
        self.txtPassword.pack()

        self.lbl1 = Label(self.registerWindow, text="")
        self.lbl1.pack()

        # Label and textfield placement for password
        self.lblCPassword = Label(self.registerWindow, text="Please re-enter same password *")
        self.lblCPassword.pack()
        self.txtCPassword = Entry(self.registerWindow, width=25, border=3, show="*", font=("", 12))
        self.txtCPassword.pack()

        self.lbl1 = Label(self.registerWindow, text="")
        self.lbl1.pack()

        #  placement for register button
        self.btnRegister = Button(self.registerWindow, text="Register", pady=10, command=self.ValidateInputs, width=20,
                                  padx=10)
        self.btnRegister.config(bg="#136AA9", fg="white")
        self.btnRegister.pack()

        self.lbl1 = Label(self.registerWindow, text="")
        self.lbl1.pack()

        self.registerWindow.mainloop()

    def userTypeOptionChange(self, event):
        userType = self.usertypeVar.get()
        if userType == 'user':
            self.txtlicensePlate.delete(0, END)
            self.txtlicensePlate.config(state="disabled")

        elif userType == 'driver':
            self.txtlicensePlate.config(state="normal")

    def ValidateInputs(self):
        Name = self.txtName.get()
        Email = self.txtEmail.get().lower()
        Phone = self.txtPhone.get()
        Address = self.txtAddress.get()
        Gender = self.genderVar.get()
        Payment = self.paymentVar.get()
        Password = self.txtPassword.get()
        Usertype = self.usertypeVar.get()
        Licenseplate = self.txtlicensePlate.get()
        Cpassword = self.txtCPassword.get()

        if not re.match("[A-Za-z]{2,25}\s[A-Za-z]{2,25}", Name):
            self.validationError("Invalid Name")
            self.txtName.focus()

        elif not re.match("^[0-9a-zA-Z!#$%&;'*+\-/\=\?\^_`\.{|}~]{1,64}@[0-9a-zA-Z]{1,255}\.[a-zA-Z]{1,10}",
                          Email):
            self.validationError("Invalid email")
            self.txtEmail.focus()

        elif Phone == "":
            self.validationError("Please your phone number")
            self.txtPhone.focus()

        elif not re.match("[0-9]{1,9}", Phone):
            self.validationError("Please enter valid phone number")
            self.txtPhone.focus()

        elif Address == "":
            self.validationError("Please enter your address")
            self.txtAddress.focus()

        elif (Usertype == "driver" and Licenseplate == ""):
            self.validationError("Please enter your license plate")
            self.txtlicensePlate.focus()

        elif len(Password) <= 5:
            self.validationError("Please enter more than 5 characters")
            self.txtPassword.focus()

        elif Cpassword != Password:
            self.validationError("Please re enter same password")
            self.txtCPassword.focus()

        else:
            addUser = UserBLL().registerUser(Name, Email, Phone, Address, Gender, Payment, Password, Licenseplate,
                                             Usertype)
            if addUser == 0:
                messagebox.showwarning("User exist ",
                                       "User with " + Email + " already exist, please choose a different email")
                self.txtEmail.focus()
            elif addUser == 1:
                doLogin = messagebox.askquestion("Success", "New user registered successfully, do you want to login")
                if doLogin == 'yes':
                    self.registerWindow.destroy()
                    llg = Login()

                else:
                    self.txtName.delete(0, END)
                    self.txtPassword.delete(0, END)
                    self.txtCPassword.delete(0, END)
                    self.txtAddress.delete(0, END)
                    self.txtEmail.delete(0, END)
                    self.txtPhone.delete(0, END)

    @staticmethod
    def validationError(ValidationMessage):
        return messagebox.showerror("Validation error", ValidationMessage)
