from Tkinter import *

def cipher():
    data = text_area.get("1.0",END)
    print data

window = Tk()

frame=Frame(window)
frame.pack()

text_area = Text(frame)
text_area.pack()

result = StringVar()
result.set('Num As: 0 Num of Ts: 0 Num Cs: 0 Num Gs: 0')
label=Label(window,textvariable=result)
label.pack()

button=Button(window,text="Count", command=cipher)
button.pack()

window.mainloop()