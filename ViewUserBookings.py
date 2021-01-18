from tkinter import *
from tkinter import messagebox
import re
from BookingBLL import *
from tkinter import ttk


class ViewBookings:
    def __init__(self, userData):
        self.userData = userData

        self.ViewBookingWindow = Tk()
        self.ViewBookingWindow.title("View bookings")

        windowWidth = 830
        windowHeight = 500
        screenWidth = self.ViewBookingWindow.winfo_screenwidth()
        screenHeight = self.ViewBookingWindow.winfo_screenheight()
        x = (screenWidth / 2) - (windowWidth / 2)
        y = (screenHeight / 2) - (windowHeight / 2)

        self.ViewBookingWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, x, y))

        self.lblHeading = Label(self.ViewBookingWindow,
                                text="Hello " + self.userData[0][1] + ", your booking details", font=("", 10))
        self.lblHeading.place(x=255, y=10)

        self.bookingTable = ttk.Treeview(self.ViewBookingWindow, show="headings", height=10)
        self.bookingTable.place(x=55, y=50)

        self.bookingTable['columns'] = (0, 1, 3, 3, 4, 5)

        self.bookingTable.column(0, width=120, anchor=CENTER)
        self.bookingTable.column(1, width=120, anchor=CENTER)
        self.bookingTable.column(2, width=120, anchor=CENTER)
        self.bookingTable.column(3, width=120, anchor=CENTER)
        self.bookingTable.column(4, width=120, anchor=CENTER)
        self.bookingTable.column(5, width=120, anchor=CENTER)

        self.bookingTable.heading(0, text="id")
        self.bookingTable.heading(1, text="Pickup date")
        self.bookingTable.heading(2, text="Pickup time")
        self.bookingTable.heading(3, text="Pickup address")
        self.bookingTable.heading(4, text="Drop off address")
        self.bookingTable.heading(5, text="Booking status")
        self.bookingTable.bind('<Button-1>', self.selectItem)

        self.lblNote = Label(self.ViewBookingWindow, text="Double click to select the item")
        self.lblNote.place(x=55, y=300)

        self.lblDiaplaySelectedItem = Label(self.ViewBookingWindow, text="Selected Booking : None")
        self.lblDiaplaySelectedItem.place(x=55, y=330)

        self.btnCancelBooking = Button(self.ViewBookingWindow, text="Cancel booking", width=25, height=3, fg="white",
                                       bg="#DD5145", command=self.cancelBooking)
        self.btnCancelBooking.place(x=310, y=350)

        self.fetchBookingData()

        self.ViewBookingWindow.mainloop()

    def fetchBookingData(self):
        bookingDatas = BookingBLL().fetchBookingsdata(self.userData)
        if bookingDatas == 0:
            messagebox.showerror("Error", "Unable to fetch data")
        else:
            for data in bookingDatas:
                self.bookingTable.insert('', "end", values=(data[0], data[2], data[3], data[4], data[5], data[6]))

    def selectItem(self, event):

        getValueFromTable = self.getValueFromTable()
        if getValueFromTable == "" or getValueFromTable is None:
            return
        else:
            self.lblDiaplaySelectedItem.config(
                text="Selected Booking: "
                     "   Id = " + str(getValueFromTable[0]) +
                     ",  Date =" + str(getValueFromTable[1]) +
                     ",  Time = " + str(getValueFromTable[2]) +
                     ",  Pick Up address = " + str(getValueFromTable[3]) +
                     ",  Drop off address = " + str(getValueFromTable[4]))

    def cancelBooking(self):
        valueToCancel = self.getValueFromTable()
        if valueToCancel == "" or valueToCancel is None:
            messagebox.showwarning("Failed", "Please select booking you want to cancel")
        else:
            doCancelBooking = messagebox.askquestion("Are you sure", "Are you sure to cancel booking?")
            if doCancelBooking == 'yes':
                cancelBooking = BookingBLL().cancelBooking(valueToCancel[0])
                if cancelBooking == 1:
                    messagebox.showinfo("Success ",
                                        "Your booking number " + str(valueToCancel[0]) + " has been cancelled")
                    self.ViewBookingWindow.destroy()
                    vub = ViewBookings(self.userData)
                else:
                    messagebox.showerror("Error ", "Failed to cancel booking ")

    def getValueFromTable(self):
        focusedItemInTable = self.bookingTable.focus()
        currentItemInTable = self.bookingTable.item(focusedItemInTable)
        getCurrentTableValue = currentItemInTable.values()
        getCurrentTableValue = list(getCurrentTableValue)
        return getCurrentTableValue[2]
