from tkinter import *
from tkinter import messagebox
import re
from BookingBLL import *
from tkinter import ttk
from UserBLL import *
from AssignedBookingBLL import *


# Class declaration for assigned bookings window for admin
class ViewAdminAssignedBookings:
    def __init__(self, userData):
        self.userData = userData
        self.ViewAssignedBookings = Tk()
        self.ViewAssignedBookings.title("View Assigned bookings")
        windowWidth = 1200
        windowHeight = 500
        screenWidth = self.ViewAssignedBookings.winfo_screenwidth()
        screenHeight = self.ViewAssignedBookings.winfo_screenheight()
        x = (screenWidth / 2) - (windowWidth / 2)
        y = (screenHeight / 2) - (windowHeight / 2)
        self.ViewAssignedBookings.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, x, y))

        # Widgets placement in the designed window
        self.lblHeading = Label(self.ViewAssignedBookings,
                                text="Total assigned bookings", font=("", 10))
        self.lblHeading.place(x=650, y=10)

        self.assignedBookingTable = ttk.Treeview(self.ViewAssignedBookings, show="headings", height=5)
        self.assignedBookingTable.place(x=55, y=50)

        self.assignedBookingTable['columns'] = (0, 1, 3, 3, 4, 5, 6, 7, 8)

        self.assignedBookingTable.column(0, width=120, anchor=CENTER)
        self.assignedBookingTable.column(1, width=120, anchor=CENTER)
        self.assignedBookingTable.column(2, width=120, anchor=CENTER)
        self.assignedBookingTable.column(3, width=120, anchor=CENTER)
        self.assignedBookingTable.column(4, width=120, anchor=CENTER)
        self.assignedBookingTable.column(5, width=120, anchor=CENTER)
        self.assignedBookingTable.column(6, width=120, anchor=CENTER)
        self.assignedBookingTable.column(7, width=120, anchor=CENTER)
        self.assignedBookingTable.column(8, width=120, anchor=CENTER)

        self.assignedBookingTable.heading(0, text="Assigned id")
        self.assignedBookingTable.heading(1, text="Driver name")
        self.assignedBookingTable.heading(2, text="License Plate")
        self.assignedBookingTable.heading(3, text="Date")
        self.assignedBookingTable.heading(4, text="Time")
        self.assignedBookingTable.heading(5, text="Pickup location")
        self.assignedBookingTable.heading(6, text="Drop off location")
        self.assignedBookingTable.heading(7, text="User name")
        self.assignedBookingTable.heading(8, text="Payment method")

        self.fetchBookingData()
        self.ViewAssignedBookings.mainloop()

    # FUnction to Fetch assigned bookings data
    def fetchBookingData(self):
        assignedBookingsData = AssignedBookingBLL().getAssignDrivers()
        print(assignedBookingsData)
        if assignedBookingsData == 0:
            messagebox.showerror("Error", "Failed to fetch bookings data")
        else:
            for data in assignedBookingsData:
                self.assignedBookingTable.insert('', "end", values=(
                    data[0], data[4], data[11], data[15], data[16], data[17], data[18], data[21], data[26]))
