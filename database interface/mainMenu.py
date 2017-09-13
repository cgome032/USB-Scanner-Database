from Tkinter import *




class Main_Menu:

    def __init__(self,master):
        self.master = master
        master.title("Login")

        loginFrame = Frame(master, width=300, height=200)
        loginFrame.pack(fill=BOTH)







if __name__ == '__main__':
    root=Tk()
    root.resizable()
    Main_Menu(root)
    root.mainloop()

