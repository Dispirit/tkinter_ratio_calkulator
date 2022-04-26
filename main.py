# from tkinter import Tk, Button, Entry, Label
#
#
# def clicked():
#     res = "Привет {}".format(txt.get())
#     lbl.configure(text=res)
#
#
# window = Tk()
# window.title("Добро пожаловать в приложение PythonRu")
# window.geometry('400x250')
# lbl = Label(window, text="Введите Request", font=("Arial Bold", 12))
# lbl.grid(column=0, row=0)
# lbl2 = Label(window, text="Введите Limits", font=("Arial Bold", 12))
# lbl2.grid(column=1, row=0)
#
#
# txt = Entry(window, width=10)
# txt.grid(column=2, row=0)
# btn = Button(window, text="Клик!", command=clicked)
# btn.grid(column=3, row=0)
# window.mainloop()


import tkinter as tk
import tkinter.font as tkFont
from tkinter import END


class App:
    def __init__(self, root):
        # setting title
        root.title("Ratio Calculator")
        # setting window size
        width = 250
        height = 220
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        align_main_form = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(align_main_form)
        root.resizable(width=False, height=False)
        root.configure(background='#cecece')

        self.rat_limit = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        self.rat_limit["font"] = ft
        self.rat_limit["bg"] = "#cecece"
        self.rat_limit["fg"] = "#000000"
        self.rat_limit["anchor"] = "w"
        self.rat_limit["justify"] = "left"
        self.rat_limit["text"] = "Enter ratio limit: "
        self.rat_limit.place(x=10, y=20, width=120, height=30)

        req_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        req_label["font"] = ft
        req_label["bg"] = "#cecece"
        req_label["fg"] = "#000000"
        req_label["anchor"] = "w"
        req_label["justify"] = "left"
        req_label["text"] = "Enter Requests: "
        req_label.place(x=10, y=60, width=120, height=30)

        lim_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        lim_label["font"] = ft
        lim_label["bg"] = "#cecece"
        lim_label["fg"] = "#000000"
        lim_label["anchor"] = "w"
        lim_label["justify"] = "left"
        lim_label["text"] = "Enter Limits: "
        lim_label.place(x=10, y=100, width=117, height=30)

        rat_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        rat_label["font"] = ft
        rat_label["bg"] = "#cecece"
        rat_label["fg"] = "#000000"
        rat_label["anchor"] = "w"
        rat_label["justify"] = "left"
        rat_label["text"] = "Ratio is: "
        rat_label.place(x=10, y=140, width=70, height=30)

        self.rat_result = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14, weight=tkFont.BOLD)
        self.rat_result["font"] = ft
        self.rat_result["bg"] = "#cecece"
        self.rat_result["fg"] = "#000000"
        # self.rat_result["anchor"] = "w"
        self.rat_result["justify"] = "center"
        self.rat_result["text"] = ""
        self.rat_result.place(x=150, y=140, width=50, height=30)

        self.rat_edit = tk.Entry(root)
        self.rat_edit["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.rat_edit["font"] = ft
        self.rat_edit["bg"] = "#cecece"
        self.rat_edit["fg"] = "#000000"
        self.rat_edit["justify"] = "center"
        self.rat_edit["text"] = ""
        self.rat_edit.place(x=150, y=20, width=50, height=30)

        self.req_edit = tk.Entry(root)
        self.req_edit["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.req_edit["font"] = ft
        self.req_edit["bg"] = "#cecece"
        self.req_edit["fg"] = "#000000"
        self.req_edit["justify"] = "center"
        self.req_edit["text"] = ""
        self.req_edit.place(x=150, y=60, width=50, height=30)

        self.lim_edit = tk.Entry(root)
        self.lim_edit["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.lim_edit["font"] = ft
        self.lim_edit["bg"] = "#cecece"
        self.lim_edit["fg"] = "#000000"
        self.lim_edit["justify"] = "center"
        self.lim_edit["text"] = ""
        self.lim_edit.place(x=150, y=100, width=50, height=30)

        clear_btn = tk.Button(root)
        clear_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=14)
        clear_btn["font"] = ft
        clear_btn["fg"] = "#000000"
        clear_btn["justify"] = "center"
        clear_btn["text"] = "Clear"
        clear_btn.place(x=140, y=185, width=82, height=30)
        clear_btn["command"] = self.clear_btn_command

        calculate_btn = tk.Button(root)
        calculate_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=14)
        calculate_btn["font"] = ft
        calculate_btn["fg"] = "#000000"
        calculate_btn["justify"] = "center"
        calculate_btn["text"] = "Calculate"
        calculate_btn.place(x=20, y=185, width=98, height=30)
        calculate_btn["command"] = self.calculate_btn_command

    def clear_btn_command(self):
        print("Clear all fields")
        self.lim_edit.delete(0, END)
        self.req_edit.delete(0, END)
        self.rat_result['text'] = ""
        self.rat_edit.delete(0, END)

    def calculate_btn_command(self):
        print("Calculate")
        req_inside = self.req_edit.get()
        lim_inside = self.lim_edit.get()
        rat_inside = self.rat_edit.get()
        try:
            ratio = (int(lim_inside) / int(req_inside))
            print(req_inside, lim_inside, ratio)
            self.rat_result['text'] = "%.2f" % ratio
            if float(rat_inside) < float(ratio):
                self.rat_result["fg"] = "#F08080"
            else:
                self.rat_result["fg"] = "#2E8B57"
        except ValueError:
            print("Only digits possible")
        except ZeroDivisionError:
            print("You can't divide by 0!")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

