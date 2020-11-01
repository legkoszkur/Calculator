import tkinter as tk
from PIL import ImageTk as itk
from math import *
import math

root = tk.Tk()
root.geometry("400x450")
root.title("Calculator")
root.resizable(False, False)

path1 = 'C:/Users/Janusz/Desktop/icona.png'
icon_image = itk.PhotoImage(file = path1)
root.iconphoto(False, icon_image)

path2 = 'C:/Users/Janusz/Desktop/background.jpg'
background_image = itk.PhotoImage(file = path2)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1, relx=0.,rely=0,)

main_screen = tk.StringVar()
auxiliary_screen = tk.StringVar()
operator = ""


frame_screen = tk.Frame(root, bg='brown', )
frame_screen.place(relwidth=0.80, relheight=0.14, relx=0.1, rely=0.1)


display = tk.Entry(frame_screen, bg='white', justify='right', textvariable=main_screen,
                   state='disabled', font=('Arial', 14, 'bold'))
display.place(relwidth=0.98, relheight=0.55, relx=0.01, rely=0.4)



display_2 = tk.Entry(frame_screen, state='disabled', textvariable=auxiliary_screen, justify='right')
display_2.place(relwidth=0.98, relheight=0.3, relx=0.01, rely=0.05)


frame_buttons = tk.Frame(root, bg='brown', )
frame_buttons.place(relwidth=0.80, relheight=0.72, relx=0.1, rely=0.25,)


basic_symbols = ["-", "+", "/", "*", "."]
other_symbols = ["(",")"]

def click_opertion(number):
    global operator
    operator = operator + str(number)
    main_screen.set(operator)
    auxiliary_screen.set(operator)

def equle_button():
    global operator
    if len(operator) == 0:
        pass
    else:
        try:
            main_screen.set(str(eval(operator)))
        except SyntaxError or TypeError:
            main_screen.set("Incorrect equasion.")
            auxiliary_screen.set("Press C to go back in to your equasion.")
        except TypeError:
            main_screen.set("Incorrect equasion.")
            auxiliary_screen.set("Press C to go back in to your equasion.")

def symbols_buttons(symbol):
    global operator
    if len(operator) == 0:
        if symbol == basic_symbols[0]:
            main_screen.set(operator)
            operator = operator + str(symbol)
            auxiliary_screen.set(operator)
            main_screen.set(operator)
    elif len(operator) != 0:
        if operator[-1] in basic_symbols:
            pass
        else:
            main_screen.set(operator)
            operator = operator + str(symbol)
            auxiliary_screen.set(operator)
            main_screen.set(operator)
    else:
        pass

def clean_buttons(ct):
    global main_screen
    global operator
    if ct == "full":
        main_screen.set('')
        auxiliary_screen.set('')
        operator = ""
    elif ct == "last":
        if len(operator) != 0:
            if len(operator) == 1:
                operator = operator[:-1]
                main_screen.set(operator)
                auxiliary_screen.set('')
            elif operator[-2] == ".":
                operator = operator[:-2]
                main_screen.set(operator)
                auxiliary_screen.set('')
            else:
                operator = operator[:-1]
                main_screen.set(operator)
                auxiliary_screen.set('')

def functions_buttons(ans):
    global operator
    if len(operator) != 0:
        if operator[-1] in basic_symbols:
            operator = operator[:-1]
        try:
            main_screen.set(str(eval(operator)))
        except SyntaxError:
            main_screen.set("Incorrect equasion.")
            auxiliary_screen.set("Press C to go back in to your equasion.")
            pass
        else:
            try:
                equle_button()
                if ans == "two":
                    operator = 2 ** float(eval(operator))
                elif ans == "ten":
                    operator = 10 ** float(eval(operator))
                elif ans == "one":
                    operator = 1 / float(eval(operator))
                elif ans == "log":
                    operator = log(float(eval(operator)))
                elif ans == "expo":
                    operator = float(eval(operator)) ** 2
                elif ans == "sqrt":
                    operator = sqrt(float(eval(operator)))
                elif ans == "exp":
                    operator = exp(float(eval(operator)))
                auxiliary_screen.set(operator)
                main_screen.set(operator)
                operator = str(operator)
            except OverflowError:
                main_screen.set("Your number is to large.")
                auxiliary_screen.set("Press C to go back in to your equasion.")
            except ValueError:
                main_screen.set("Incorect operation")
                auxiliary_screen.set("Press C to go back in to your equasion.")


    else:
        pass

def constants_buttons(special):
    global operator
    if operator[-4:] == round(getattr(math, special), 2):
        pass
    elif len(operator) == 0:
        operator = operator + str(round(getattr(math, special), 2))
        main_screen.set(operator)
        auxiliary_screen.set(operator)
    elif len(operator) >= 2 and operator[-1] in basic_symbols[0:4]:
        operator = operator + str(round(getattr(math, special), 2))
        main_screen.set(operator)
        auxiliary_screen.set(operator)
    else:
        pass

button_names = [
                    [
                    "/","C","CE",u'\u03C0',"e","2"+u'\u207F',
                    ],

                    [
                    "*",7,8,9,"x"+ u'\u00B2',"10"+u'\u207F',
                    ],

                    [
                    "-",4,5,6,u'\u221A'+"x","1/x",
                    ],

                    [
                    "+",1,2,3,"exp","ln",
                    ],

                    [
                    "=",".",0,'000',"(",")"
                    ],
                ]

button_colors = [
                    [
                    "lightcyan","chocolate","chocolate","cyan","cyan","cyan",
                    ],

                    [
                    "lightcyan","gold","gold","gold","cyan","cyan",
                    ],

                    [
                    "lightcyan","gold","gold","gold","cyan","cyan",
                    ],

                    [
                    "lightcyan","gold","gold","gold","cyan","cyan",
                    ],

                    [
                    "lightcyan","lightcyan","gold","gold","lightcyan","lightcyan",
                    ]
                ]

button_commands = [
                    [
                    lambda: symbols_buttons("/"), lambda: clean_buttons("last"), lambda: clean_buttons("full"),
                    lambda: constants_buttons('pi'), lambda: constants_buttons('e'), lambda: functions_buttons("two")
                    ],

                    [
                    lambda: symbols_buttons("*"), lambda: click_opertion(7), lambda: click_opertion(8),
                    lambda: click_opertion(9), lambda: functions_buttons("expo"), lambda: functions_buttons("ten")
                    ],

                    [
                    lambda: symbols_buttons("-"), lambda: click_opertion(4), lambda: click_opertion(5),
                    lambda: click_opertion(6), lambda: functions_buttons("sqrt"), lambda: functions_buttons("one")
                    ],

                    [
                    lambda: symbols_buttons("+"), lambda: click_opertion(1), lambda: click_opertion(2),
                    lambda: click_opertion(3),lambda: functions_buttons("exp"), lambda: functions_buttons("log")
                    ],

                    [
                    equle_button, lambda: symbols_buttons("."),lambda: click_opertion(0),
                    lambda: click_opertion('000'), lambda: click_opertion("("), lambda: click_opertion(")")
                    ]
                ]

for i in range(6):
    for j in range(5):
        button_set = tk.Button(frame_buttons, text=button_names[j][i], width=5, height=2, bg=button_colors[j][i],
                               font='arial', fg="black", relief='raised', command=button_commands[j][i],)
        button_set.pack()
        button_set.place(relwidth=0.16, relheight=0.192, relx=0.01+i*0.165, rely=0.01+j*0.198)

root.mainloop()







