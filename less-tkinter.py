#
# import tkinter as tk
#
# window = tk.Tk()
#
# label = tk.Label(
#     text="Привет, Tkinter!",
#     fg="white",
#     bg="black",
#     width=20,
#     height=20
# )
#
# label.pack()
# window.mainloop()


# from tkinter import *
# import time
#
#
# def tick():
#     label.after(200, tick)
#     label['text'] = time.strftime('%H:%M:%S')
# root = Tk()
# label = Label(font='sans 40')
# label.pack()
# label.after_idle(tick)
# root.mainloop()


# from tkinter import *
# root = Tk()
# frame1 = Frame(root, bg='green', bd=5)
# frame2 = Frame(root, bg='red', bd=5)
# button1 = Button(frame1, text='Первая кнопка')
# button2 = Button(frame2, text='Вторая кнопка')
# frame1.pack()
# frame2.pack()
# button1.pack()
# button2.pack()
# root.mainloop()


# from tkinter import *
# root=Tk()
# var1=IntVar()
# var2=IntVar()
# check1=Checkbutton(root,text='1 пункт',variable=var1,onvalue=1,offvalue=0)
# check2=Checkbutton(root,text='2 пункт',variable=var2,onvalue=1,offvalue=0)
# check1.pack()
# check2.pack()
# root.mainloop()


# from tkinter import *
# root=Tk()
# var=IntVar()
# rbutton1=Radiobutton(root,text='1',variable=var,value=1)
# rbutton2=Radiobutton(root,text='2',variable=var,value=2)
# rbutton3=Radiobutton(root,text='3',variable=var,value=3)
# rbutton1.pack()
# rbutton2.pack()
# rbutton3.pack()
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# def getV(root):
#     a = scale1.get()
#     print("Значение", a)
#
# scale1 = Scale(root,orient=HORIZONTAL,length=300,from_=50,to=80,
#                tickinterval=5, resolution=1)
# button1 = Button(root, text="Получить значение")
# scale1.pack()
# button1.pack()
# button1.bind("<Button-1>", getV)
# root.mainloop()



# from tkinter import *
# root = Tk()
# text = Text(root, height=3, width=60)
# text.pack(side='left')
# scrollbar = Scrollbar(root)
# scrollbar.pack(side='left')
# # первая привязка
# scrollbar['command'] = text.yview
# # вторая привязка
# text['yscrollcommand'] = scrollbar.set
# root.mainloop()


# from tkinter import *
# root=Tk()
# button1 = Button(text="1")
# button2 = Button(text="2")
# button3 = Button(text="3")
# button4 = Button(text="4")
# button5 = Button(text="5")
# button1.pack(side='left')
# button2.pack(side='top')
# button3.pack(side='left')
# button4.pack(side='bottom')
# button5.pack(side='right')

# root.mainloop()


# from tkinter import *
# root=Tk()
# text = Text(wrap=NONE)
# vscrollbar = Scrollbar(orient='vert', command=text.yview)
# text['yscrollcommand'] = vscrollbar.set
# hscrollbar = Scrollbar(orient='hor', command=text.xview)
# text['xscrollcommand'] = hscrollbar.set
# # размещаем виджеты
# text.grid(row=0, column=0, sticky='nsew')
# vscrollbar.grid(row=0, column=1, sticky='ns')
# hscrollbar.grid(row=1, column=0, sticky='ew')
# # конфигурируем упаковщик, чтобы текстовый виджет расширялся
# root.rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)
# root.mainloop()


from tkinter import *
root=Tk()
def leftclick(event):
    print('Вы нажали левую кнопку мыши')
def rightclick(event):
    print('Вы нажали правую кнопку мыши')
button1=Button(root, text='Нажми')
button1.pack()
button1.bind('<Button-1>', leftclick)
button1.bind('<Button-3>', rightclick)
root.mainloop()