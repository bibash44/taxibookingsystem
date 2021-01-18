from tkinter import *
from BookATaxiWindow import *
from ViewUserBookings import *


class UserDashboard:
    def __init__(self, userData):
        self.userData = userData
        self.userDashboardWindow = Tk()
        self.userDashboardWindow.title("User Dashboard")
        windowWidth = 450
        windowHeight = 350

        screenWidth = self.userDashboardWindow.winfo_screenwidth()
        screenHeight = self.userDashboardWindow.winfo_screenheight()

        x = (screenWidth / 2) - (windowWidth / 2)
        y = (screenHeight / 2) - (windowHeight / 2)

        self.userDashboardWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, x, y))

        lblHeading = Label(self.userDashboardWindow, text="Hello " + self.userData[0][1], font=("", 12))
        lblHeading.place(x=55, y=0)

        btnBookTaxi = Button(self.userDashboardWindow, text="Book taxi", height=5, width=15, fg="#ffffff", bg="#7C59EB",
                             font=("", 10), command=self.openBookingWindow)
        btnBookTaxi.place(x=55, y=50)

        btnViewBooking = Button(self.userDashboardWindow, text="View Booking", height=5, width=15, fg="#ffffff",
                                bg="#FF483D",
                                font=("", 10), command=self.openViewBookingWindow)
        btnViewBooking.place(x=255, y=50)

        self.userDashboardWindow.mainloop()

    def openBookingWindow(self):
        self.userDashboardWindow.iconify()
        ubw = UserBookingWindow(self.userData)

    def openViewBookingWindow(self):
        self.userDashboardWindow.iconify()
        ubw = ViewBookings(self.userData)
