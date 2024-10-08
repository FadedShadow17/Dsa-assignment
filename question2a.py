from tkinter import *

win = Tk()
win.geometry("350x400")
win.resizable(0, 0)
win.title("Calculator")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""
input_text = StringVar()

input_frame = Frame(win, width=350, height=60, bd=0, highlightbackground="blue", highlightcolor="blue", highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('Helvetica', 20), textvariable=input_text, width=50, bg="#ccc", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=20)

btns_frame = Frame(win, width=350, height=340, bg="#444")
btns_frame.pack()

clear = Button(btns_frame, text="C", fg="white", width=32, height=3, bd=0, bg="#f44336", cursor="hand2", command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text="/", fg="white", width=10, height=3, bd=0, bg="#4CAF50", cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

seven = Button(btns_frame, text="7", fg="white", width=10, height=3, bd=0, bg="#9E9E9E", cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg="white", width=10, height=3, bd=0, bg="#9E9E9E", cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", fg="white", width=10, height=3, bd=0, bg="#9E9E9E", cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="*", fg="white", width=10, height=3, bd=0, bg="#4CAF50", cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

four = Button(btns_frame, text="4", fg="white", width=10, height=3, bd=0, bg="#9E9E9E", cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", fg="white", width=10, height=3, bd=0, bg="#9E9E9E", cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", fg="white", width=10, height=3, bd=0, bg="#9E9E9E", cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text="-", fg="white", width=10, height=3, bd=0, bg="#4CAF50", cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

one = Button(btns_frame, text="1", fg="white", width=10, height=3, bd=0, bg="#9E9E9E", cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", fg="white", width=10, height=3, bd=0, bg="#9E9E9E", cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", fg="white", width=10, height=3, bd=0, bg="#9E9E9E", cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text="+", fg="white", width=10, height=3, bd=0, bg="#4CAF50", cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

zero = Button(btns_frame, text="0", fg="white", width=21, height=3, bd=0, bg="#9E9E9E", cursor="hand2", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(btns_frame, text=".", fg="white", width=10, height=3, bd=0, bg="#4CAF50", cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
equals = Button(btns_frame, text="=", fg="white", width=10, height=3, bd=0, bg="#4CAF50", cursor="hand2", command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
