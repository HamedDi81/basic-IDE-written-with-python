from tkinter import *
import tkinter.messagebox
from io import StringIO

class Ide:
#====================================Attribute===========================================================================    
    def __init__(self):
        self.root = Tk()
        self.root.title("Run Python Code")  # set up the title
        self.root.geometry('600x600')  # set up the size
        color = 'dark green'
        self.root.configure(bg=color)
        self.root.resizable(width=True, height=True)
#===========================================================================================================================
        self.top = Frame(self.root, width=600, height=50, bg=color)#A frame in Tk lets you organize and group widgets. It works like a container. Its a rectangular area in which widges can be placed.
        self.top.pack(side=TOP)
#===================================================================================================================================
        self.btn_clear = Button(self.top, text="clear", font=('arial', 25, 'italic'), highlightbackground=color,
                                command=lambda: self.clear_text())
        self.btn_clear.pack(side=TOP)
        
        self.btn_run = Button(self.top, text="Run", font=('arial', 25, 'italic'), highlightbackground=color, command=lambda: self.run())
        self.btn_run.pack(side=TOP)
        self.message = Text(font=('arial', 20, 'italic'), bd=10, width=88, bg='white')
        self.message.pack(side=TOP)
        self.root.mainloop()
    
# ==================================================Functions=============================================================
    
    
    def clear_text(self):
        self.message.delete("1.0", END)
    
    
    def run(self):
        try:
            old_stdout = sys.stdout
            redirected_output = sys.stdout = StringIO()
            exec(self.message.get("1.0", END))
            sys.stdout = old_stdout
            tkinter.messagebox.showinfo("Result", redirected_output.getvalue())
        except SyntaxError:
            tkinter.messagebox.showinfo("Result", "SyntaxError: unexpected EOF while parsing")
    
    


app=Ide() #this command run the program and open the IDE