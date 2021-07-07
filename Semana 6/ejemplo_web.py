import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_582=tk.Button(root)
        GButton_582["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_582["font"] = ft
        GButton_582["fg"] = "#000000"
        GButton_582["justify"] = "center"
        GButton_582["text"] = "Button"
        GButton_582.place(x=200,y=130,width=147,height=30)
        GButton_582["command"] = self.GButton_582_command

        GLabel_11=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_11["font"] = ft
        GLabel_11["fg"] = "#333333"
        GLabel_11["justify"] = "center"
        GLabel_11["text"] = "Bienvenidos a nuestro programa"
        GLabel_11.place(x=150,y=10,width=230,height=68)

        GLineEdit_423=tk.Entry(root)
        GLineEdit_423["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_423["font"] = ft
        GLineEdit_423["fg"] = "#333333"
        GLineEdit_423["justify"] = "center"
        GLineEdit_423["text"] = "Ingrese su nombre"
        GLineEdit_423.place(x=150,y=190,width=280,height=35)

        GMessage_863=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_863["font"] = ft
        GMessage_863["fg"] = "#333333"
        GMessage_863["justify"] = "center"
        GMessage_863["text"] = "Message"
        GMessage_863.place(x=40,y=290,width=236,height=32)

        GListBox_830=tk.Listbox(root)
        GListBox_830["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_830["font"] = ft
        GListBox_830["fg"] = "#333333"
        GListBox_830["justify"] = "center"
        GListBox_830.place(x=250,y=350,width=80,height=25)
        GListBox_830["listvariable"] = "escoger"
        GListBox_830["selectmode"] = "single"

        GButton_965=tk.Button(root)
        GButton_965["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_965["font"] = ft
        GButton_965["fg"] = "#000000"
        GButton_965["justify"] = "center"
        GButton_965["text"] = "Button"
        GButton_965.place(x=230,y=80,width=70,height=25)
        GButton_965["command"] = self.GButton_965_command

        GCheckBox_458=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_458["font"] = ft
        GCheckBox_458["fg"] = "#333333"
        GCheckBox_458["justify"] = "center"
        GCheckBox_458["text"] = "CheckBox"
        GCheckBox_458.place(x=130,y=420,width=70,height=25)
        GCheckBox_458["offvalue"] = "0"
        GCheckBox_458["onvalue"] = "1"
        GCheckBox_458["command"] = self.GCheckBox_458_command

    def GButton_582_command(self):
        print("command")


    def GButton_965_command(self):
        print("command")


    def GCheckBox_458_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

