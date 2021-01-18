from tkinter import *
from ViewAdminBookings import *
from ViewAdminAssignedBookings import *


class AdminDashboard:
    def __init__(self, userData):
        self.userData = userData
        self.adminDashboardWindow = Tk()
        self.adminDashboardWindow.title("User Dashboard")
        windowWidth = 450
        windowHeight = 350

        screenWidth = self.adminDashboardWindow.winfo_screenwidth()
        screenHeight = self.adminDashboardWindow.winfo_screenheight()

        x = (screenWidth / 2) - (windowWidth / 2)
        y = (screenHeight / 2) - (windowHeight / 2)

        self.adminDashboardWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, x, y))

        lblHeading = Label(self.adminDashboardWindow, text="Hello " + self.userData[0][1], font=("", 12))
        lblHeading.place(x=55, y=0)

        btnAssignDriver = Button(self.adminDashboardWindow, text="Assigned Drivers ", height=5, width=15, fg="#ffffff",
                                 bg="#7C59EB",
                                 font=("", 10), command=self.openViewAssignedBookings)
        btnAssignDriver.place(x=55, y=50)

        btnViewBooking = Button(self.adminDashboardWindow, text="View Bookings", height=5, width=15, fg="#ffffff",
                                bg="#FF483D",
                                font=("", 10), command=self.openViewBookings)
        btnViewBooking.place(x=255, y=50)

        self.adminDashboardWindow.mainloop()

    def openViewBookings(self):
        self.adminDashboardWindow.iconify()
        vad = ViewAdminBookings(self.userData)

    def openViewAssignedBookings(self):
        self.adminDashboardWindow.iconify()
        vad = ViewAdminAssignedBookings(self.userData)
