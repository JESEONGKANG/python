from tkinter import *
from tkinter import messagebox

def clickButton() :
    messagebox.showinfo("버튼클릭", "버튼을 눌렀습니다")

root = Tk()
root.title("GUI 프로그래밍 연습")
root.geometry("400x200")

label1 = Label(root, text="2023 수시 대박")
label1.pack()
label2 = Label(root, text="기원합니다.", \
               font=("궁서체", 30), bg="blue", fg="yellow")
label2.pack()

button1 = Button(root, text="여기를 클릭하세요", \
                 fg="red", bg="yellow", \
                 command=clickButton)
button1.pack(expand=1)

root.mainloop()
