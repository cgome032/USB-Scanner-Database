from tkinter import *
from PIL import Image, ImageTk


class AddItemMenu:
    def __init__(self, master):
        self.master = master

        # image sources 
        self.__imgSrc = {
            'WMS': '../img/WMS Logo.JPG',
            'Westco': '../img/WestcoLogo.JPG',
            'Wadco': '../img/Wadco 3D 03.png',
            'Central': '../img/Central Metal Logo 600png.png'
        }

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



if __name__ == '__main__':
    root = Tk()
    root.resizable()
    AddItemMenu(root)
    root.mainloop()