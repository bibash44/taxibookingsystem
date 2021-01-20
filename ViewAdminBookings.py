from tkinter import *
from tkinter import messagebox
import re
from BookingBLL import *
from tkinter import ttk
from UserBLL import *
from AssignedBookingBLL import *


# Class declaration for viewing bookings window for admin
class ViewAdminBookings:
    def __init__(self, userData):
        self.userData = userData
        self.ViewBookingWindow = Tk()
        self.ViewBookingWindow.title("View bookings")
        windowWidth = 1300
        windowHeight = 700
        screenWidth = self.ViewBookingWindow.winfo_screenwidth()
        screenHeight = self.ViewBookingWindow.winfo_screenheight()
        x = (screenWidth / 2) - (windowWidth / 2)
        y = (screenHeight / 2) - (windowHeight / 2)

        # Widgets placement in the designed window
        self.ViewBookingWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, x, y))

        self.lblHeading = Label(self.ViewBookingWindow,
                                text="Total bookings of user", font=("", 10))
        self.lblHeading.place(x=650, y=10)

        self.bookingTable = ttk.Treeview(self.ViewBookingWindow, show="headings", height=5)
        self.bookingTable.place(x=55, y=50)

        self.lblHeading = Label(self.ViewBookingWindow,
                                text="Total drivers", font=("", 10))
        self.lblHeading.place(x=650, y=200)

        self.driversTable = ttk.Treeview(self.ViewBookingWindow, show="headings", height=5)
        self.driversTable.place(x=55, y=230)

        self.bookingTable['columns'] = (0, 1, 3, 3, 4, 5, 6, 7, 8, 9, 10)
        self.driversTable['columns'] = (0, 1, 3, 3, 4, 5)

        self.bookingTable.column(0, width=110, anchor=CENTER)
        self.bookingTable.column(1, width=110, anchor=CENTER)
        self.bookingTable.column(2, width=110, anchor=CENTER)
        self.bookingTable.column(3, width=110, anchor=CENTER)
        self.bookingTable.column(4, width=110, anchor=CENTER)
        self.bookingTable.column(5, width=110, anchor=CENTER)
        self.bookingTable.column(6, width=110, anchor=CENTER)
        self.bookingTable.column(7, width=110, anchor=CENTER)
        self.bookingTable.column(8, width=110, anchor=CENTER)
        self.bookingTable.column(9, width=110, anchor=CENTER)
        self.bookingTable.column(10, width=110, anchor=CENTER)

        self.driversTable.column(0, width=200, anchor=CENTER)
        self.driversTable.column(1, width=200, anchor=CENTER)
        self.driversTable.column(2, width=200, anchor=CENTER)
        self.driversTable.column(3, width=200, anchor=CENTER)
        self.driversTable.column(4, width=200, anchor=CENTER)
        self.driversTable.column(5, width=200, anchor=CENTER)

        self.bookingTable.heading(0, text="id")
        self.bookingTable.heading(1, text="Pickup date")
        self.bookingTable.heading(2, text="Pickup time")
        self.bookingTable.heading(3, text="Pickup location")
        self.bookingTable.heading(4, text="Drop off location")
        self.bookingTable.heading(5, text="Booking status")
        self.bookingTable.heading(6, text="Name")
        self.bookingTable.heading(7, text="Email")
        self.bookingTable.heading(8, text="Phone")
        self.bookingTable.heading(9, text="Gender")
        self.bookingTable.heading(10, text="Payment method")

        self.driversTable.heading(0, text="Id")
        self.driversTable.heading(1, text="Name")
        self.driversTable.heading(2, text="Email")
        self.driversTable.heading(3, text="Phone")
        self.driversTable.heading(4, text="Gender")
        self.driversTable.heading(5, text="License plate")

        self.bookingTable.bind('<Button-1>', self.selectDataFromBookingTable)
        self.driversTable.bind('<Button-1>', self.selectDatFromDriversTable)

        self.lblNote = Label(self.ViewBookingWindow, text="Double click to select the item")
        self.lblNote.place(x=55, y=400)

        self.lblDiaplaySelectedItem = Label(self.ViewBookingWindow, text="Selected Booking : None")
        self.lblDiaplaySelectedItem.place(x=55, y=420)

        self.lblDisplaySelectedDriver = Label(self.ViewBookingWindow, text="Selected Driver : None")
        self.lblDisplaySelectedDriver.place(x=55, y=440)

        self.btnAssignDriver = Button(self.ViewBookingWindow, text="Assign Driver", width=25, height=3, fg="white",
                                      bg="#4A8AF4", command=self.assignDriver)
        self.btnAssignDriver.place(x=55, y=480)

        self.btnConfirmBooking = Button(self.ViewBookingWindow, text="Confirm booking", width=25, height=3, fg="white",
                                        bg="#5DBA8D", command=self.confirmBooking)
        self.btnConfirmBooking.place(x=255, y=480)

        self.fetchBookingData()
        self.fetchDriverData()

        self.ViewBookingWindow.mainloop()

    def fetchBookingData(self):
        bookingDatas = BookingBLL().fetchBookingsdataForAdmin()
        if bookingDatas == 0:
            messagebox.showerror("Error", "Failed to fetch bookings data")
        else:
            for data in bookingDatas:
                self.bookingTable.insert('', "end", values=(
                    data[0], data[2], data[3], data[4], data[5], data[6], data[8], data[9], data[10], data[12],
                    data[13]))

    def fetchDriverData(self):
        driverData = UserBLL().getDriverDatas()
        if driverData == 0:
            messagebox.showerror("Error ", "Failed to fetch drivers data")
        else:
            for data in driverData:
                self.driversTable.insert('', "end", values=(
                    data[0], data[1], data[2], data[3], data[5], data[8]
                ))

    def selectDataFromBookingTable(self, event):
        getValueFromBookingTable = self.getValueFromBookingTable()
        if getValueFromBookingTable == "" or getValueFromBookingTable is None:
            return
        else:
            self.lblDiaplaySelectedItem.config(
                text="Selected Booking: "
                     "   Id = " + str(getValueFromBookingTable[0]) +
                     ",  Date =" + str(getValueFromBookingTable[1]) +
                     ",  Time = " + str(getValueFromBookingTable[2]) +
                     ",  Pick up location = " + str(getValueFromBookingTable[3]) +
                     ",  Drop off location = " + str(getValueFromBookingTable[4]))

    def selectDatFromDriversTable(self, event):
        getValueFromDriversTable = self.getValueFromDriversTable()
        if getValueFromDriversTable == "" or getValueFromDriversTable is None:
            return
        else:
            self.lblDisplaySelectedDriver.config(
                text="Selected Driver: "
                     "   Id = " + str(getValueFromDriversTable[0]) +
                     ",  Name =" + str(getValueFromDriversTable[1]) +
                     ",  License Plate = " + str(getValueFromDriversTable[5]))

    def confirmBooking(self):
        bookingToConfirm = self.getValueFromBookingTable()

        if bookingToConfirm == "" or bookingToConfirm is None:
            messagebox.showwarning("Failed", "Please select booking you want to confirm")
        else:
            doConfirm = messagebox.askquestion("Are you sure", "Are you sure to confirm booking?")
            if doConfirm == 'yes':
                status = str(bookingToConfirm[5])
                if status == 'confirmed':
                    messagebox.showwarning("Failed", "Booking is already confirmed")
                else:
                    confirmBooking = BookingBLL().confirmBooking(str(bookingToConfirm[0]))
                    if confirmBooking == 1:
                        messagebox.showinfo("Success ",
                                            "Your booking number " + str(bookingToConfirm[0]) + " has been confirmed")
                        self.ViewBookingWindow.destroy()
                        vub = ViewAdminBookings(self.userData)
                    else:
                        messagebox.showerror("Failed ", "Failed to confirm booking")

    def assignDriver(self):
        bookingToAssign = self.getValueFromBookingTable()
        driverToAssign = self.getValueFromDriversTable()

        if bookingToAssign == "" or bookingToAssign is None:
            messagebox.showwarning("Failed", "Please select a booking to assign")
            return
        elif driverToAssign == "" or bookingToAssign is None:
            messagebox.showwarning("Failed", "Please select a driver to assign")
            return
        else:
            bookingStatus = bookingToAssign[5]
            if not bookingStatus == "confirmed":
                messagebox.showwarning("Failed",
                                       "Booking not confirmed, please confirm booking before assigning to the driver")
            else:
                bookingid = str(bookingToAssign[0])
                driverid = str(driverToAssign[0])

                doAssign = messagebox.askquestion("Confirm ",
                                                  "Are you sure to assign driver " + driverToAssign[1] + " to user " +
                                                  bookingToAssign[5])
                if doAssign == 'yes':
                    assigndriverToBooking = AssignedBookingBLL().assignDriver(driverid, bookingid)
                    if assigndriverToBooking == 0:
                        messagebox.showwarning("Failed ", "Driver is already assigned to selected booking")
                    elif assigndriverToBooking == 1:
                        messagebox.showinfo("Success ", "Driver assigned")
                        self.ViewBookingWindow.destroy()
                        vub = ViewAdminBookings(self.userData)

    def getValueFromBookingTable(self):
        focusedItemInTable = self.bookingTable.focus()
        currentItemInTable = self.bookingTable.item(focusedItemInTable)
        getCurrentTableValue = currentItemInTable.values()
        getCurrentTableValue = list(getCurrentTableValue)
        return getCurrentTableValue[2]

    def getValueFromDriversTable(self):
        focusedItemInTable = self.driversTable.focus()
        currentItemInTable = self.driversTable.item(focusedItemInTable)
        getCurrentTableValue = currentItemInTable.values()
        getCurrentTableValue = list(getCurrentTableValue)
        return getCurrentTableValue[2]
