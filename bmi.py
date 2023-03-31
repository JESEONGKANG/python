import tkinter
import tkinter.messagebox

window = tkinter.Tk()
window.title("강제성")
window.geometry("600x400+100+100")
window.resizable(False, False)

he= tkinter.StringVar()
we= tkinter.StringVar()

def btn_click() :
    h_value= float(he.get())
    w_value= float(we.get())
    h_value= h_value * 0.01
    result= w_value / (h_value * h_value)
    tkinter.messagebox.showinfo("결과", result)

titLabel= tkinter.Label(window, text= "체질량질수 계산기")
titLabel.config(font=("Arial", 25))
titLabel.config(fg="red")
titLabel.pack()

heightLabel= tkinter.Label(window, text= "신장")
heightLabel.config(font= ("Arial", 24))
heightLabel.place(x=30, y=70)

heightEntry= tkinter.Entry(window, textvariable= he)
heightEntry.place(x=120, y=82)

weightLabel= tkinter.Label(window, text= "체중")
weightLabel.config(font= ("Arial", 24))
weightLabel.place(x=30, y=120)

weightEntry= tkinter.Entry(window, textvariable= we)
weightEntry.place(x=120, y=130)


btn= tkinter.Button(window, text="확인", command= btn_click)
btn.place(x=30, y=250)

window. mainloop()
