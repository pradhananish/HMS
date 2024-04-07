from tkinter import *
class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("costumer")
        self.root.geometry("1295x550+230+220")

if __name__ == '__main__':
    root=Tk()
    object=Cust_Win(root)
    root.mainloop()

