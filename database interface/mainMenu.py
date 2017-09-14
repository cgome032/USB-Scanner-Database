from tkinter import *
from PIL import Image, ImageTk

from connection.empInitConnection import EmpDatabaseConnect


class MainMenu:

    def __init__(self,master):
        self.master = master

        # User entry variables
        self.userId = StringVar()
        self.userPw = StringVar()


        # Main menu-menu bar
        self.mainMenuBar = Menu(self.master)
        self.fileMenu = Menu(self.mainMenuBar,tearoff=0)
        self.fileMenu.add_command(label='Help')
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='Quit',command=self.master.quit)
        self.mainMenuBar.add_cascade(label='File',menu=self.fileMenu)

        self.master.config(menu=self.mainMenuBar)

        self.master.title("WWW Inventory Management System")
        #master.configure(background='#3399FF')

        # Login Frame for buttons/labels
        self.loginFrame = LabelFrame(self.master, width=300, height=200, text="Employee Login",bd='.0625i',relief=RIDGE)
        self.loginFrame.pack(side='bottom',fill=NONE)

        # Logo Frame for company logos
        self.logoFrame = Frame(self.master, width=100, height=200,borderwidth='0i')
        self.logoFrame.pack(side='top',fill=NONE,pady=20,anchor='c')

        self.__imgSrc = {
            'WMS': '../img/WMS Logo.JPG',
            'Westco': '../img/WestcoLogo.JPG',
            'Wadco': '../img/Wadco 3D 03.png',
            'Central': '../img/Central Metal Logo 600png.png'
        }

        self.__newWidth = 300   # New Width of company logos
        self.__newLength = 150  # New Length of company logos
        self.__xCounter = 0
        self.__yCounter = 0
        for img in self.__imgSrc.values():
            self.newImg = ImageTk.PhotoImage(Image.open(img).resize((self.__newWidth,self.__newLength)))
            self.newImageLabel = Label(self.logoFrame, image=self.newImg)
            self.newImageLabel.image = self.newImg # necessary to finish Image implementation
            self.newImageLabel.grid(row=self.__yCounter,column=self.__xCounter)
            self.__xCounter += 1
            if self.__xCounter == 2:
                self.__yCounter += 1
                self.__xCounter = 0

        self.userWidth = 20
        self.userHeight = 10

        self.userIdLabel = Label(self.loginFrame,width=self.userWidth,text='Employee Identification')
        self.userIdEntry = Entry(self.loginFrame,width=self.userWidth,textvariable=self.userId)

        self.userPwLabel = Label(self.loginFrame,width=self.userWidth,text='Employee Password')
        self.userPwEntry = Entry(self.loginFrame,width=self.userWidth,textvariable=self.userPw,show='*')

        self.userAttempt = Button(self.loginFrame,width=self.userWidth,text="Login",relief=GROOVE,command=lambda: self.employeeLogin(self.userId.get(),self.userPw.get()))
        self.master.bind('<Return>',lambda x: self.employeeLogin(self.userId.get(),self.userPw.get()))

        self.userIdLabel.grid(row=0,column=0)
        self.userIdEntry.grid(row=0,column=1)
        self.userPwLabel.grid(row=1,column=0)
        self.userPwEntry.grid(row=1,column=1)
        self.userAttempt.grid(row=2,column=1)


    def employeeLogin(self,userId,userPw):
        self.newDatabase = EmpDatabaseConnect()
        self.newDatabase.connectDatabase()
        #print('User Credentials: ' + userId)
        #print('User Password: ' + userPw)
        if (self.newDatabase.verifyCredentials(userId,userPw)):
            print("successful login")
        else:
            print("User information not recognized")

class AddItemMenu:
    def __init__(self,master):
        self.master = master


if __name__ == '__main__':
    root=Tk()
    root.resizable(False,False)
    MainMenu(root)
    root.mainloop()

