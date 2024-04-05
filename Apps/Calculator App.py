from tkinter import *
from math import *

WIN = Tk()
WIN.title("Calculator")
WIN.geometry("545x470")
WIN.resizable = False, False

operation = 0
current_op = 0
current_op_font =('ubuntu', 40)
op_font = ('ubuntu', 10)

op_txt_x = 500
op_txt_y = 50
cur_op_txt_x = 490
cur_op_txt_y = 80

button_1_clicked = False
button_2_clicked = False
button_3_clicked = False
button_4_clicked = False
button_5_clicked = False
button_6_clicked = False
button_7_clicked = False
button_8_clicked = False
button_9_clicked = False
button_10_clicked = False
button_11_clicked = False
button_12_clicked = False
button_13_clicked = False
button_14_clicked = False
button_15_clicked = False
button_16_clicked = False
button_17_clicked = False
button_18_clicked = False
button_19_clicked = False
button_20_clicked = False
button_21_clicked = False
button_22_clicked = False
button_23_clicked = False
button_24_clicked = False
button_25_clicked = False
button_26_clicked = False

error = False

def set_clicked_false(n):
    global button_1_clicked, button_2_clicked, button_3_clicked, button_4_clicked, button_5_clicked, button_6_clicked, button_7_clicked, button_8_clicked, button_9_clicked, button_10_clicked, button_11_clicked, button_12_clicked, button_13_clicked, button_14_clicked, button_15_clicked, button_16_clicked, button_17_clicked, button_18_clicked, button_19_clicked, button_20_clicked, button_21_clicked, button_22_clicked, button_23_clicked, button_24_clicked, button_25_clicked, button_26_clicked
    for i in range(1, 27):
        if i != n:
            globals()[f'button_{i}_clicked'] = False

def button_clicked(button_id):
    global operation, error, current_op, op_txt_x, op_txt_y, cur_op_txt_x, cur_op_txt_y, button_1_clicked, button_2_clicked, button_3_clicked, button_4_clicked, button_5_clicked, button_6_clicked, button_7_clicked, button_8_clicked, button_9_clicked, button_10_clicked, button_11_clicked, button_12_clicked, button_13_clicked, button_14_clicked, button_15_clicked, button_16_clicked, button_17_clicked, button_18_clicked, button_19_clicked, button_20_clicked, button_21_clicked, button_22_clicked, button_23_clicked, button_24_clicked, button_25_clicked, button_26_clicked
    if button_id == 1: #percentage
        if error == False:
            num = str(int(current_op)/100)
            a = len(operation)
            b = len(current_op)
            c = a - b
            operation = operation[:c]
            operation += num
            cur_op_txt_x = 490
            current_op = 0
            pass

    elif button_id == 2: #delete current
        a = len(operation)
        b = len(current_op)
        c = a - b
        operation = operation[:c]
        cur_op_txt_x = 490
        current_op = "0"
        pass

    elif button_id == 3: #delete all
        current_op = 0
        operation = 0
        cur_op_txt_x = 490
        op_txt_x = 500
        button_3_clicked = True
        set_clicked_false(3)

    elif button_id == 4: #delete
        if current_op == 0:
            pass
        elif current_op != 0 and button_1_clicked == False and button_5_clicked == False and button_6_clicked == False and button_7_clicked == False and button_8_clicked == False and button_12_clicked == False and button_16_clicked == False and button_20_clicked == False and button_23_clicked == False and button_24_clicked == False:
            current_op = current_op[:-1]
            operation = operation[:-1]
            op_txt_x += 7
            cur_op_txt_x += 29
            if len(operation) == 0:
                operation = 0
                op_txt_x = 500
            if len(current_op) == 0:
                current_op = 0
                cur_op_txt_x = 490
        button_4_clicked = True
        set_clicked_false(4)
        

    elif button_id == 5: #inverse
        if current_op == 0 and operation == 0:
            current_op = "Cannot divide by zero"
            cur_op_txt_x = 10
        else:
            operation = "1/" + operation
            current_op = eval(operation)
            current_op = str(current_op)
            for i in range(len(current_op)):
                if "." in current_op[i]:
                    d = i
                    d += 5
            current_op = current_op[:d]
            operation = current_op
            for i in range(len(str(current_op[:d]))):
                cur_op_txt_x -= 29


    elif button_id == 6: #squared
        if current_op == 0:
            pass
        elif current_op != 0 and button_1_clicked == False and button_5_clicked == False and button_6_clicked == False and button_7_clicked == False and button_8_clicked == False and button_12_clicked == False and button_16_clicked == False and button_20_clicked == False and button_23_clicked == False and button_24_clicked == False:
            operation += "**2"
            op_txt_x -= 21
            current_op = str(eval(current_op + "**2"))
            for i in range(len(current_op)):
                cur_op_txt_x -= 29
            if len(operation) == 0:
                operation = 0
                op_txt_x = 500
            if len(current_op) == 0:
                current_op = 0
                cur_op_txt_x = 490
        button_6_clicked = True
        set_clicked_false(6)

    elif button_id == 7: #square root
        try:
            operation = "sqrt(" + operation + ")"
            current_op = str(eval(operation))
        except TypeError:
            operation = str(operation)
            operation = "sqrt(" + operation + ")"
            current_op = str(eval(operation))
        except SyntaxError:
            error = True
        except ValueError:
            error = True
            operation = "Math Domain Error"
        if error == False:
            for i in range(len(current_op)):
                    if "." in current_op[i]:
                        d = i
                        d += 5
                        cur_op_txt_x = 490
            current_op = current_op[:d]
            for i in range(len(str(current_op[:d]))):
                cur_op_txt_x -= 29
        error = False
        button_7_clicked = True
        set_clicked_false(7)

    elif button_id == 8: #divide
        print("/")
        if operation == 0:
            pass
        elif operation != 0 and not button_12_clicked:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x = 490
            operation += str("/")
            op_txt_x -= 7
            current_op = str(current_op)
            current_op = "0"
            cur_op_txt_x = 490

        button_8_clicked = True
        set_clicked_false(8)

    elif button_id == 9: #num 1
        print("1")
        if operation == 0:
            operation = str(operation)
            operation = str("1")
            current_op = "1"
        elif operation != 0:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x += 29
            operation += str("1")
            op_txt_x -= 7
            current_op = str(current_op)
            current_op += "1"
            cur_op_txt_x -= 29

        button_9_clicked = True
        set_clicked_false (9)

    elif button_id == 10: #num 2
        print("2")
        if operation == 0:
            operation = str(operation)
            operation = str("2")
            current_op = "2"
        elif operation != 0:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x += 29
            operation += str("2")
            op_txt_x -= 7
            current_op = str(current_op)
            current_op += "2"
            cur_op_txt_x -= 29

        button_10_clicked = True
        set_clicked_false (10)


    elif button_id == 11: #num 3
        print("3")
        if operation == 0:
            operation = str(operation)
            operation = str("3")
            current_op = "3"
        elif operation != 0:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x += 29
            operation += str("3")
            op_txt_x -= 7
            current_op = str(current_op)
            current_op += "3"
            cur_op_txt_x -= 29

        button_11_clicked = True
        set_clicked_false (11)

    elif button_id == 12: #multiply
        print("*")
        if operation == 0:
            pass
        elif operation != 0 and not button_12_clicked:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x = 490
            operation += str("*")
            op_txt_x -= 7
            current_op = str(current_op)
            current_op = "0"
            cur_op_txt_x = 490

        button_12_clicked = True
        set_clicked_false(12)

    elif button_id == 13: #num 4
        print("4")
        if operation == 0:
            operation = str(operation)
            operation = str("4")
            current_op = "4"
        elif operation != 0:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x += 29
            operation += str("4")
            op_txt_x -= 7
            current_op = str(current_op)
            current_op += "4"
            cur_op_txt_x -= 29

        button_13_clicked = True
        set_clicked_false (13)

    elif button_id == 14: #num 5
        print("5")
        if operation == 0:
            operation = str(operation)
            operation = str("5")
            current_op = "5"
        elif operation != 0:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x += 29
            operation += str("5")
            op_txt_x -= 7
            current_op = str(current_op)
            current_op += "5"
            cur_op_txt_x -= 29

        button_14_clicked = True
        set_clicked_false (14)

    elif button_id == 15: #num 6
        print("6")
        if operation == 0:
            operation = str(operation)
            operation = str("6")
            current_op = "6"
        elif operation != 0:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x += 29
            operation += str("6")
            op_txt_x -= 7
            current_op = str(current_op)
            current_op += "6"
            cur_op_txt_x -= 29

        button_15_clicked = True
        set_clicked_false (15)

    elif button_id == 16: #substract
        print("-")
        if operation == 0:
            pass
        elif operation != 0 and not button_16_clicked:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x = 490
            operation += str("-")
            op_txt_x -= 7
            current_op = str(current_op)
            current_op = "0"
            cur_op_txt_x = 490

        button_16_clicked = True
        set_clicked_false(16)

    elif button_id == 17: #num 7
        print("7")
        if operation == 0:
            operation = str(operation)
            operation = str("7")
            current_op = "7"
        elif operation != 0:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x += 29
            operation += str("7")
            op_txt_x -= 7
            current_op = str(current_op)
            current_op += "7"
            cur_op_txt_x -= 29

        button_17_clicked = True
        set_clicked_false (17)

    elif button_id == 18: #num 8
        print("8")
        if operation == 0:
            operation = str(operation)
            operation = str("8")
            current_op = "8"
        elif operation != 0:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x += 29
            operation += str("8")
            op_txt_x -= 7
            current_op = str(current_op)
            current_op += "8"
            cur_op_txt_x -= 29

        button_18_clicked = True
        set_clicked_false (18)

    elif button_id == 19: #num 9
        print("9")
        if operation == 0:
            operation = str(operation)
            operation = str("9")
            current_op = "9"
        elif operation != 0:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x += 29
            operation += str("9")
            op_txt_x -= 7
            current_op = str(current_op)
            current_op += "9"
            cur_op_txt_x -= 29

        button_19_clicked = True
        set_clicked_false (19)

    elif button_id == 20: #addition
        print("+")
        if operation == 0:
            pass
        elif operation != 0 and not button_20_clicked:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x = 490
            operation += str("+")
            op_txt_x -= 7
            current_op = str(current_op)
            current_op = "0"
            cur_op_txt_x = 490

        button_20_clicked = True
        set_clicked_false(20)

    elif button_id == 21: #substraction
        if operation == 0 or operation == "0":
            pass
        elif operation[0] != "-":
            operation = "-" + operation
        elif operation[0] == "-":
            operation = operation[1:]
        set_clicked_false(21)
 
    elif button_id == 22: #num 0
        print("0")
        if operation == 0:
            operation = str(operation)
            operation = str("0")
            current_op = "0"
        elif operation != 0:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x += 29
            operation += str("0")
            op_txt_x -= 7
            current_op = str(current_op)
            current_op += "0"
            cur_op_txt_x -= 29

        button_22_clicked = True
        set_clicked_false(22)

    elif button_id == 23: #decimal
        try:
            operation += "."
            current_op += "."
        except TypeError:
            operation = str(operation)
            current_op = str(current_op)
            operation += "."
            current_op += "."

        button_23_clicked = True
        set_clicked_false(23)

    elif button_id == 24: #calculate
        print("=")
        if operation == 0:
            pass
        elif operation != 0 or button_24_clicked == False:
            if current_op == "0":
                current_op = current_op[:-1]
                cur_op_txt_x = 490
            current_op = str(current_op)
            try:
                current_op = eval(operation) 
            except SyntaxError:
                current_op = "Invalid Syntax"
                error = True
            except ZeroDivisionError:
                current_op = "Cannot divide by zero"
                error = True
            operation = str(current_op)
            current_op = str(current_op)
            if "." in operation: 
                for i in range(len(current_op)):
                    if "." in current_op[i]:
                        d = i
                        d += 5
                current_op = current_op[:d]
                operation = current_op
            if button_24_clicked == False:
                cur_op_txt_x = 490
                op_txt_x = 500
                for i in range(len(operation)):
                    op_txt_x -=7
                    cur_op_txt_x -= 29
                cur_op_txt_x += 29
                           
        button_24_clicked = True
        set_clicked_false(24)

    elif button_id == 25:   #left parentheses
        if operation == "0" or operation == 0:
            operation = "("
        else:
            operation += "("
        button_25_clicked = True
        set_clicked_false(25)

    elif button_id == 26:   #right parentheses 
        if operation == "0" or operation == 0:
            operation = ")"
        else:
            operation += ")"
        button_26_clicked = True
        set_clicked_false(26)

    current_op_txt.config(text = current_op)
    op_txt.config(text = operation)
    op_txt.place(x=op_txt_x, y=op_txt_y)
    current_op_txt.place(x=cur_op_txt_x, y=cur_op_txt_y)


def draw_buttons():
    button_percentage = Button(WIN, text="%")
    button_percentage.place(x=5, y=200)
    button_percentage.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(1))
    button_CE = Button(WIN, text="CE")
    button_CE.place(x=140, y=200)
    button_CE.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(2))
    button_C = Button(WIN, text="C")
    button_C.place(x=275, y=200)
    button_C.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(3))
    button_del = Button(WIN, text="⌫")
    button_del.place(x=410, y=200)
    button_del.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(4))

    button_inverse = Button(WIN, text="1/x")
    button_inverse.place(x=5, y=245)
    button_inverse.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(5))
    button_square = Button(WIN, text="x²")
    button_square.place(x=140, y=245)
    button_square.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(6))
    button_root = Button(WIN, text="√x")
    button_root.place(x=275, y=245)
    button_root.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(7))
    button_div = Button(WIN, text="÷")
    button_div.place(x=410, y=245)
    button_div.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(8))

    button_1 = Button(WIN, text="1")
    button_1.place(x=5, y=290)
    button_1.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(9))
    button_2 = Button(WIN, text="2")
    button_2.place(x=140, y=290)
    button_2.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(10))
    button_3 = Button(WIN, text="3")
    button_3.place(x=275, y=290)
    button_3.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(11))
    button_mult = Button(WIN, text="x")
    button_mult.place(x=410, y=290)
    button_mult.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(12))

    button_4 = Button(WIN, text="4")
    button_4.place(x=5, y=335)
    button_4.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(13))
    button_5 = Button(WIN, text="5")
    button_5.place(x=140, y=335)
    button_5.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(14))
    button_6 = Button(WIN, text="6")
    button_6.place(x=275, y=335)
    button_6.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(15))
    button_subst = Button(WIN, text="-")
    button_subst.place(x=410, y=335)
    button_subst.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(16))

    button_7 = Button(WIN, text="7")
    button_7.place(x=5, y=380)
    button_7.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(17))
    button_8 = Button(WIN, text="8")
    button_8.place(x=140, y=380)
    button_8.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(18))
    button_9 = Button(WIN, text="9")
    button_9.place(x=275, y=380)
    button_9.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(19))
    button_add = Button(WIN, text="+")
    button_add.place(x=410, y=380)
    button_add.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(20))

    button_negate = Button(WIN, text="±")
    button_negate.place(x=5, y=425)
    button_negate.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(21))
    button_0 = Button(WIN, text="0")
    button_0.place(x=140, y=425)
    button_0.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(22))
    button_dot = Button(WIN, text=".")
    button_dot.place(x=275, y=425)
    button_dot.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(23))
    button_eq = Button(WIN, text="=")
    button_eq.place(x=410, y=425)
    button_eq.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(24), bg= 'blue', fg= 'white')

    button_left_par = Button(WIN, text="(")
    button_left_par.place(x=275, y=155)
    button_left_par.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(25))
    button_right_par = Button(WIN, text=")")
    button_right_par.place(x=410, y=155)
    button_right_par.config(width=17, height=2, cursor="hand2", command= lambda: button_clicked(26))

op_txt = Label(WIN, text = operation, font = op_font)
op_txt.place(x=500, y =50)
current_op_txt = Label(WIN, text = current_op, font=current_op_font)
current_op_txt.place(x=490, y = 80)

draw_buttons()

WIN.mainloop()
