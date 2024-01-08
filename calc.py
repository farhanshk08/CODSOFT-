from tkinter import *

first_num = second_num = operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text="")
    
def get_operator(op):
    global first_num,operator
    first_num = int(result_label['text'])
    operator = op
    result_label.config(text="")
    
def get_result(): 
    global first_num,second_num,operator
    second_num = int(result_label['text'])
    if operator == "+":
        result = first_num + second_num
    elif operator == "-":
        result = first_num - second_num
    elif operator == "*":
        result = first_num * second_num
    else:
        if second_num == 0:
            result = "Error"
        else:
            result = round(first_num / second_num,2)
    result_label.config(text=str(result))
 
root = Tk()
root.title("Calculator")
root.geometry("300x380")
root.resizable(False, False) #fixed size
root.configure(bg = "black")


result_label=Label(root, text="",bg="black",fg="green")
result_label.grid(row=0,column=0 ,columnspan=50,pady=(50,25),sticky='w')
result_label.config(font=("Verdana", 30, 'bold'))

#first row
btn7 = Button(root, text="7",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command=lambda:get_digit(7))
btn7.grid(row=1,column=0)

btn7 = Button(root, text="8",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command=lambda:get_digit(8))
btn7.grid(row=1,column=1)

btn7 = Button(root, text="9",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command=lambda:get_digit(9))
btn7.grid(row=1,column=2)

btn_add = Button(root, text="+",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command=lambda:get_operator("+"))
btn_add.grid(row=1,column=3)

#second row 
btn4 = Button(root, text="4",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command=lambda:get_digit(4))
btn4.grid(row=2,column=0)

btn4 = Button(root, text="5",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command=lambda:get_digit(5))
btn4.grid(row=2,column=1)

btn4 = Button(root, text="6",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command=lambda:get_digit(6))
btn4.grid(row=2,column=2)

btn_sub = Button(root, text="-",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command=lambda:get_operator("-"))
btn_sub.grid(row=2,column=3)

#third row
btn1 = Button(root, text="1",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command=lambda:get_digit(1))
btn1.grid(row=3,column=0)

btn1 = Button(root, text="2",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command=lambda:get_digit(2))
btn1.grid(row=3,column=1)

btn1 = Button(root, text="3",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command=lambda:get_digit(3))
btn1.grid(row=3,column=2)

btn_mul = Button(root, text="x",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command= lambda:get_operator("*"))
btn_mul.grid(row=3,column=3)

#fourth row
btn_clr = Button(root, text="C",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command=lambda:clear())
btn_clr.grid(row=4,column=0)

btn0 = Button(root, text="0",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command=lambda:get_digit(0))
btn0.grid(row=4,column=1)

btn_eq = Button(root, text="=",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command=get_result)
btn_eq.grid(row=4,column=2)

btn_div = Button(root, text="/",bg="green",fg="yellow",width=5,height=2 ,font=("Verdana", 14, 'bold'),command = lambda:get_operator("/"))
btn_div.grid(row=4,column=3)

root.mainloop()