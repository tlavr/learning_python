import tkinter as tk, os
import tkinter.ttk as ttk

ins = tk.INSERT

class Wind(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.grid()
        self.get_form_interface()
        self.get_action()

    def get_form_interface(self):
        print("jhgjhgj")
        self.txt = tk.Entry(self,width=30)
        self.txt.grid(row = 0, column =0)
        self.txt.insert(ins, "some_text")
        self.lbl = ttk.Label(self, text = "It's me!")
        self.lbl.grid(row=1, column=0)

        self.btn = ttk.Button(self, text = "Mybut")
        self.btn.grid(row=2, column=0)

    def get_action(self):
        self.btn.bind("<Button-1>", self.my_button_action)

    def my_button_action(self, evt):
        print("Button press!")

if __name__ == "__main__":

    win = Wind()
    win.master.style = ttk.Style()
    win.master.style.theme_use("default")
    win.master.title("Base_Sketch")
    win.master.mainloop()
