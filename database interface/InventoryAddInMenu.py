from tkinter import *
from PIL import Image, ImageTk
from MaterialBarcode.barcodeSetup import MatBarcode
from connection import matInitConnection
from tkinter import ttk
from tkinter.messagebox import showinfo

from Material import material

class AddItemMenu:
    def __init__(self, master):
        self.master = master

        # User entry variables
        self.upcId = StringVar()

        # image sources 
        self.__imgSrc = {
            'WMS': '../img/WMS Logo.JPG',
            'Westco': '../img/WestcoLogo.JPG',
            'Wadco': '../img/Wadco 3D 03.png',
            'Central': '../img/Central Metal Logo 600png.png'
        }
        # Main Frame for Inventory Menu
        self.AddMenu = Frame(self.master)
        self.AddMenu.pack(side='top')

        self.__newWidth = 300  # New Width of company logos
        self.__newLength = 150  # New Length of company logos
        self.__xCounter = 0
        self.__yCounter = 0
        for img in self.__imgSrc.values():
            self.newImg = ImageTk.PhotoImage(Image.open(img).resize((self.__newWidth, self.__newLength)))
            self.newImageLabel = Label(self.AddMenu, image=self.newImg)
            self.newImageLabel.image = self.newImg  # necessary to finish Image implementation
            self.newImageLabel.grid(row=self.__yCounter, column=self.__xCounter)
            self.__xCounter += 1

        self.userWidth = 20
        self.userHeight = 10

        self.tagEntry = Entry(self.AddMenu, width=self.userWidth,textvariable=self.upcId)
        self.attemptButton = Button(self.AddMenu, width=self.userWidth,text="Search",relief=GROOVE,command=lambda: self.getupcid(self.upcId.get()))
        self.master.bind('<Return>', lambda x: self.getupcid(self.upcId.get()))

        # Layout for Menu
        self.tagEntry.grid(row=1,column=0)
        self.attemptButton.grid(row=1,column=1)

    def getupcid(self,upcId):
        print('ID returned: ' + upcId)
        try:
            search_mat = matInitConnection.MatDatabaseConnect()
            search_mat.connectDatabase()
            ret_material = search_mat.getMaterialItem(upcId)
            mat_barcode = MatBarcode(ret_material.PlateID)
        except:
            self.popup_showerror()
            print("UPC not found")

    def popup_showerror(self):
        showinfo("Error", "Material ID not found")


if __name__ == '__main__':
    root = Tk()
    root.resizable()
    AddItemMenu(root)
    root.mainloop()