from tkinter import *

class Calculator:
    def __init__(self):

        self.load_gui()
        self.root.mainloop()


    def load_gui(self):

        self.root=Tk()
        self.root.title("CALCULATOR")
        self.root.geometry("272x380")
        self.root.resizable(0,0)
        self.root.configure(background="white")

        self.result_label= Label(self.root,text="",background="white", font=("verdana",28,"bold"),fg="black")
        self.result_label.grid(row=0,column=0,pady=10,columnspan=10,sticky="w")

        btn_7= Button(self.root, text="7",background="blue", font=("verdana",28,"bold"),fg="white",command=lambda:self.display_digit(7))
        btn_7.grid(row=1,column=0,sticky="nsew")
        btn_8= Button(self.root, text="8",background="blue", font=("verdana",28,"bold"),fg="white",command=lambda:self.display_digit(8))
        btn_8.grid(row=1,column=1,sticky="nsew")
        btn_9= Button(self.root, text="9",background="blue", font=("verdana",28,"bold"),fg="white",command=lambda:self.display_digit(9))
        btn_9.grid(row=1,column=2,sticky="nsew")
        sum_btn= Button(self.root, text="+",background="blue", font=("verdana",28,"bold"),fg="white",command=lambda:self.get_op("+"))
        sum_btn.grid(row=1,column=3,sticky="nsew")

        btn_4= Button(self.root, text="4",background="blue", font=("verdana",28,"bold"),fg="white",command=lambda:self.display_digit(4))
        btn_4.grid(row=2,column=0,sticky="nsew")
        btn_5= Button(self.root, text="5",background="blue", font=("verdana",28,"bold"),fg="white",command=lambda:self.display_digit(5))
        btn_5.grid(row=2,column=1,sticky="nsew")
        btn_6= Button(self.root, text="6",background="blue", font=("verdana",28,"bold"),fg="white",command=lambda:self.display_digit(6))
        btn_6.grid(row=2,column=2,sticky="nsew")
        sub_btn= Button(self.root, text="-",background="blue", font=("verdana",28,"bold"),fg="white",command=lambda:self.get_op("-"))
        sub_btn.grid(row=2,column=3,sticky="nsew")

        btn_3= Button(self.root, text="3",background="blue", font=("verdana",28,"bold"),fg="white",command=lambda:self.display_digit(3))
        btn_3.grid(row=3,column=0,sticky="nsew")
        btn_2= Button(self.root, text="2",background="blue", font=("verdana",28,"bold"),fg="white",command=lambda:self.display_digit(2))
        btn_2.grid(row=3,column=1,sticky="nsew")
        btn_1= Button(self.root, text="1",background="blue", font=("verdana",28,"bold"),fg="white",command=lambda:self.display_digit(1))
        btn_1.grid(row=3,column=2,sticky="nsew")
        mul_btn= Button(self.root, text="*",background="blue", font=("verdana",28,"bold"),fg="white",command=lambda:self.get_op("*"))
        mul_btn.grid(row=3,column=3,sticky="nsew")

        btn_0= Button(self.root, text="0",background="blue", font=("verdana",28,"bold"),fg="white",command=lambda:self.display_digit(0))
        btn_0.grid(row=4,column=0,sticky="nsew")
        btn_clear= Button(self.root, text="C",background="blue", font=("verdana",28,"bold"),fg="white",command=self.clear)
        btn_clear.grid(row=4,column=1,sticky="nsew")
        btn_equals= Button(self.root, text="=",background="blue", font=("verdana",28,"bold"),fg="white",command=self.equals_result)
        btn_equals.grid(row=4,column=2,sticky="nsew")
        div_btn= Button(self.root, text="/",background="blue", font=("verdana",28,"bold"),fg="white",command=lambda:self.get_op("/"))
        div_btn.grid(row=4,column=3,sticky="nsew")

    def display_digit(self,digit):
        current_digit = self.result_label["text"]
        new_digit = current_digit + str(digit)
        self.result_label.config(text=new_digit)
    
    def get_op(self,op):
        
        self.num1= int(self.result_label["text"])
        self.operation=op
        self.result_label.config(text="")

    def equals_result(self):
        self.num2= int(self.result_label["text"])

        if self.operation == "+":
            self.sum = self.num1 + self.num2
            self.result_label.config(text=self.sum)
        elif self.operation == "-":
            self.sub = self.num1 - self.num2
            self.result_label.config(text=self.sub)
        elif self.operation == "*":
            self.mul = self.num1 * self.num2
            self.result_label.config(text=self.mul)
        else:
            if self.num2 == 0:
                self.result_label.config(text="Error")
            else:
                self.div= self.num1 / self.num2
                self.result_label.config(text=self.div)

    def clear(self):
        return self.result_label.config(text="")


ob=Calculator()