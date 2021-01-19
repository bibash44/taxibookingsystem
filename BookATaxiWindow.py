from tkinter import *
from tkcalendar import *
import datetime
from tkinter import messagebox
import re
from BookingBLL import *
from UserDashboard import *


# class declaration for booking taxi for user
class UserBookingWindow:
    def __init__(self, userData):

        # Assigning title, width height and setting window to middle of the screen
        self.userData = userData
        self.bookingWindow = Tk()
        self.bookingWindow.title("Book a taxi")
        windowWidth = 500
        windowHeight = 550
        screenWidth = self.bookingWindow.winfo_screenwidth()
        screenHeight = self.bookingWindow.winfo_screenheight()
        x = (screenWidth / 2) - (windowWidth / 2)
        y = (screenHeight / 2) - (windowHeight / 2)
        self.bookingWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, x, y))

        # Widgets placement in the designed window
        lblHeading = Label(self.bookingWindow,
                           text="Hello " + self.userData[0][1] + " please enter booking details", font=("", 10))
        lblHeading.place(x=155, y=0)

        # pick a date label
        self.lblPickDate = Label(self.bookingWindow, text="Pick a date ", font=("", 10))
        self.lblPickDate.place(x=155, y=30)

        # Calander
        self.cal = Calendar(self.bookingWindow, selectmode="day", year=datetime.datetime.now().year,
                            month=datetime.datetime.now().month, day=datetime.datetime.now().day)
        self.cal.place(x=155, y=55)

        # Time label and textfield
        self.lblTime = Label(self.bookingWindow, text="Enter pickup time (HH:MM AM/PM)")
        self.lblTime.place(x=155, y=250)

        self.txtTime = Entry(self.bookingWindow, width=40, border=3)
        self.txtTime.place(x=155, y=270)

        # pickup label
        self.lblPickUpLocation = Label(self.bookingWindow, text="Enter pickup location")
        self.lblPickUpLocation.place(x=155, y=310)

        self.txtPickUpLocation = Entry(self.bookingWindow, width=40, border=3)
        self.txtPickUpLocation.place(x=155, y=330)

        # dropoff label field
        self.lblDropOffLocation = Label(self.bookingWindow, text="Enter drop off location")
        self.lblDropOffLocation.place(x=155, y=370)

        self.txtDropOffLocation = Entry(self.bookingWindow, width=40, border=3)
        self.txtDropOffLocation.place(x=155, y=400)

        self.btnBookTaxi = Button(self.bookingWindow, text="Make booking", fg="white", bg="#1DA0E4", width=35, height=3,
                                  command=self.makeBooking)
        self.btnBookTaxi.place(x=155, y=450)

        self.bookingWindow.mainloop()

    # function to make the booking
    def makeBooking(self):
        # variable declaration to store user provided inputs
        date = self.cal.get_date()
        time = self.txtTime.get()
        pickup_location = self.txtPickUpLocation.get()
        dropoff_location = self.txtDropOffLocation.get()

        # Validation for checking user inputs and showing errors if the validation fails

        if date == "":
            self.validationError("Please select pickup date")
        elif not re.findall(
                "(0[1-9]:[0-5][0-9]((\ ){0,1})((AM)|(PM)|(am)|(pm)))|([1-9]:[0-5][0-9]((\ ){0,1})((AM)|(PM)|(am)|(pm)))|(1[0-2]:[0-5][0-9]((\ ){0,1})((AM)|(PM)|(am)|(pm)))",
                time):
            self.txtTime.focus()
            self.validationError("Please enter correct time format")
        elif pickup_location == "":
            self.validationError("Please enter pick up location")
            self.txtPickUpLocation.focus()

        elif dropoff_location == "":
            self.validationError("Please enter pick off location")
            self.txtDropOffLocation.focus()
        else:

            makeBooking = BookingBLL().makeBooking(self.userData[0][0], date, time, pickup_location, dropoff_location)
            if makeBooking == 1:
                messagebox.showinfo("Success", "Your booking is confirmed for " + date + " at " + time)
                self.txtTime.delete(0, END)
                self.txtPickUpLocation.delete(0, END)

    # Static Function that returns error message box
    @staticmethod
    def validationError(ValidationMessage):
        return messagebox.showerror("Validation error", ValidationMessage)
