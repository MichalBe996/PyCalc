


import tkinter as tk

class Calculator():
    def __init__(self):
        root = tk.Tk()
        large_font = ("Verdana", 20)
        small_font = ("Verdana", 15)
        root.geometry("370x420")
        root.title("PyCalc")




        E = tk.Label(root, font = large_font, bg = "white")
        E.place(x = 10, y = 20)

        def but_1():
            E["text"] += "1"
        def but_2():
            E["text"] += "2"
        def but_3():
            E["text"] += "3"
        def but_4():
            E["text"] += "4"
        def but_5():
            E["text"] += "5"
        def but_6():
            E["text"] += "6"
        def but_7():
            E["text"] += "7"
        def but_8():
            E["text"] += "8"
        def but_9():
            E["text"] += "9"
        def but_0():
            E["text"] += "0"

        def but_ce():
            E["text"] = ""

        def but_c():
            E["text"] = str(E["text"][:-1])


        def addition():
            global symbol
            symbol = "+"
            global saved_num
            saved_num = int(E["text"])
            but_ce()
        def subtract():
            global symbol
            symbol = "-"
            global saved_num
            saved_num = int(E["text"])
            but_ce()
        def multiply():
            global symbol
            symbol = "*"
            global saved_num
            saved_num = int(E["text"])
            but_ce()
        def division():
            global symbol
            symbol = "/"
            global saved_num
            saved_num = int(E["text"])
            but_ce()

        def equal():
            if symbol == "+":
                print(saved_num + int(E["text"]))
                E["text"] = saved_num + int(E["text"])
            elif symbol == "-":
                print(saved_num - int(E["text"]))
                E["text"] = saved_num - int(E["text"])
            elif symbol == "*":
                print(saved_num * int(E["text"]))
                E["text"] = saved_num * int(E["text"])
            elif symbol == "/":
                print(saved_num / int(E["text"]))
                E["text"] = saved_num / int(E["text"])


        button_ce = tk.Button(root, text = "CE", font = small_font, command = but_ce)
        button_ce.place(x = 30, y = 80)
        button_c = tk.Button(root, text = "C", font = small_font, command = but_c)
        button_c.place(x = 80, y = 80)
        button_add = tk.Button(root, text = "+", font = small_font, command = addition)
        button_add.place(x = 120, y = 80)
        button_equals = tk.Button(root, text = "=", font = small_font, command = equal)
        button_equals.place(x = 310, y = 80)
        button_minus = tk.Button(root, text = "-", font = small_font, command = subtract)
        button_minus.place(x = 160, y = 80)
        button_mult = tk.Button(root, text = "*", font = small_font, command = multiply)
        button_mult.place(x = 195, y = 80)
        button_division = tk.Button(root, text = "/", font = small_font, command = division)
        button_division.place(x = 235, y = 80)

        button_1 = tk.Button(root, text = "1", font = large_font, width = 3, command = but_1)
        button_1.place(x = 30, y = 300)
        button_2 = tk.Button(root, text = "2", font = large_font, width = 3, command = but_2)
        button_2.place(x = 120, y = 300)
        button_3 = tk.Button(root, text = "3", font = large_font, width = 3, command = but_3)
        button_3.place(x = 210, y = 300)
        button_4 = tk.Button(root, text = "4", font = large_font, width = 3, command = but_4)
        button_4.place(x = 30, y = 220)
        button_5 = tk.Button(root, text = "5", font = large_font, width = 3, command = but_5)
        button_5.place(x = 120, y = 220)
        button_6 = tk.Button(root, text = "6", font = large_font, width = 3, command = but_6)
        button_6.place(x = 210, y = 220)
        button_7 = tk.Button(root, text = "7", font = large_font, width = 3, command = but_7)
        button_7.place(x = 30, y = 140)
        button_8 = tk.Button(root, text = "8", font = large_font, width = 3, command = but_8)
        button_8.place(x = 120, y = 140)
        button_9 = tk.Button(root, text = "9", font = large_font, width = 3, command = but_9)
        button_9.place(x = 210, y = 140)
        button_0 = tk.Button(root, text = "0", font = large_font, width = 3, command = but_0)
        button_0.place(x = 120, y = 360)

        root.mainloop()

MyCalc = Calculator()