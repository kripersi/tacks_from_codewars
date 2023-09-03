# Entry это ввод
import tkinter as tk

def getname():
    value = vvod.get()
    if value:
        print(f'hello {value}')
    else:
        print('wtf')

def delname():
    vvod.delete(0, 'end') # c какого по какой элемент удалить, чтобы всю стр delete(0, 'end')

win = tk.Tk()  # создание окна
win.geometry('500x610+700+100')
win.title('название окна')
win.config(background='#A0522D')
tk.Label(win, text='Name').grid(row=0, column=0, stick='w')

vvod = tk.Entry(win) # если добавить show='*' то будет как пароль
vvod.grid(row=0, column=1, stick='e')

btn1 = tk.Button(win, text='get name', command=getname)
btndel = tk.Button(win, text='delete name', command=delname)
btnins = tk.Button(win,text='append "ITS"', command=lambda: vvod.insert(0, 'ITS '))
btn1.grid(row=0, column=2)
btndel.grid(row=2, column=2)
btnins.grid(row=3, column=2)






win.mainloop()