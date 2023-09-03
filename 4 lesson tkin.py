import tkinter as tk

win = tk.Tk()  # создание окна
win.geometry('500x610+700+100')
win.title('название окна')
win.config(background='#A0522D')

btn1 = tk.Button(win, text='4 lesson', padx=10, pady=10)
btn2 = tk.Button(win, text='4 lesson bt2', padx=10, pady=10)
btn3 = tk.Button(win, text='bt3')
btn4 = tk.Button(win, text='4 lesson bt4', padx=10)
btn5 = tk.Button(win, text='4 lesson bt5')
btn6 = tk.Button(win, text='4 lesson bt6')
btn7 = tk.Button(win, text='4 lesson bt777')
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=1, column=0, sticky='w')
btn4.grid(row=1, column=1, rowspan=2, stick='ns')
btn5.grid(row=2, column=0) # СКОЛЬКО КОЛОНОК ЗАНИМАЕТ И в какую сторону растягивать
btn6.grid(row=3, column=0, columnspan=2, stick='we')
btn7.grid(row=0, column=2, rowspan=4, stick='ns')


win.mainloop()