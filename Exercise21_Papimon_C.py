from tkinter import *
import math
def calculateBMI(event):
    bmi = (float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2))
    if bmi > 30.0:
        labelResult.configure(text="อ้วนมากนะคะ")
    elif bmi > 25.0 and bmi < 29.9:
        labelResult.configure(text="อ้วนอยู่ค่ะ")
    elif bmi > 23.0 and bmi < 24.9:
        labelResult.configure(text="น้ำหนักเกิน")
    elif bmi > 18.6 and bmi < 22.9:
        labelResult.configure(text="น้ำหนักปกติ เหมาะสมค่ะ")
    elif bmi < 18.5:
        labelResult.configure(text="ผอมเกิ๊น")

MainWindow = Tk()
labelHight = Label(MainWindow, text="ส่วนสูง (cm)")
labelHight.grid(row=0,column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)
labelWeight = Label(MainWindow, text="น้ำหนัก (Kg)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = (Button(MainWindow, text="คำนวณ"))
calculateButton.bind('<Button-1>',calculateBMI)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow, text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
MainWindow.mainloop()