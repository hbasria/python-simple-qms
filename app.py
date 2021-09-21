from tkinter import *


class Application:
    def __init__(self, master):
        self.master = master
        self.sequence_number = ""
        self.new_sequence_number = ""
        self.is_fullscreen = False
        self.master.attributes("-fullscreen", True)
        
        self.heading = Label(master, text="Numarator", font=('arial 60 bold'), fg='green')
        self.heading.place(x=350, y=0)

        self.n = Label(master, text="", font=('arial 300 bold'))
        self.n.place(x=600, y=100)

        self.pname = Label(master, text="", font=('arial 160 bold'))
        self.pname.place(x=300, y=600)

        master.bind("<Key>", self.key_pressed)


    def key_pressed(self, event):
        #print(event.keycode)
        
        if event.keycode > 0 and event.keycode < 20:
            self.new_sequence_number = f"{self.new_sequence_number}{event.char}" 

        if event.keycode == 36:
            self.pname.config(text=self.sequence_number)
            self.sequence_number = self.new_sequence_number 
            self.n.config(text=self.sequence_number)
            self.new_sequence_number = ""
        
        if event.keycode == 24:
            self.master.quit()
            
            
        
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
app = Application(root)

root.attributes('-zoomed', True)
root.attributes("-fullscreen", True)
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.resizable(False, False)
root.mainloop()


