from tkinter import *
import math
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.integrate import odeint
import numpy as np

def f(a,k,x,y):
    return (a*x**k)*(y**2+1)
def toch_resh(a,k,x):
    return math.tan((a/(k+1))*x**(k+1))

def Eil1():
    global Y_b1,k,a
    k = int(k_en.get())
    a = int(a_en.get())
    h=0.1
    y=0
    x=0
    Y_b1=[]
    if k==-1:
        messagebox.showerror('Ошибка программы', 'k не равно -1')
    
    columns = ("i","xi","yi",'y точное','abs',"pr","Δyi=h*yi’") #таблица
    tree = ttk.Treeview(win1,columns=columns, show="headings")
    tree.place(x=200, y=140,height=150)
    tree.heading("i", text="№", anchor=CENTER)
    tree.heading("xi", text="Значение x", anchor=CENTER)
    tree.heading("yi", text="Значение y", anchor=CENTER)
    tree.heading("y точное", text="y точное", anchor=CENTER)
    tree.heading("abs", text="Абсолютная погр.", anchor=CENTER)
    tree.heading("pr", text="yi’", anchor=CENTER)
    tree.heading("Δyi=h*yi’", text="Δyi=h*yi’", anchor=CENTER)
    
    tree.column("#1", stretch=NO, width=80)
    tree.column("#2", stretch=NO, width=130)
    tree.column("#3", stretch=NO, width=130)
    tree.column("#4", stretch=NO, width=130)
    tree.column("#5", stretch=NO, width=130)
    tree.column("#6", stretch=NO, width=130)
    tree.column("#7", stretch=NO, width=130)
    for i in range(11):
        yi=round(f(a,k,x,y),5)
        y_toch=round(toch_resh(a,k,x),5)
        pogr=round(abs(y_toch-y),5)
        next_y=round(h*yi,5)
        tree.insert('','end', values=(i,x,y,y_toch,pogr,yi,next_y))
        x=round(x+h,1)
        Y_b1.append(y)
        y=round(next_y+y,5)
def scipy():
    def f(y,x,a,k):
        return (a*x**k)*(y**2+1)
    y0=0
    t = np.linspace(0,1,11)
    bibl=odeint(f,y0,t,args=(a,k))
    bibl=np.array(bibl).flatten()
    plt.figure(figsize=[8.0, 8.0])
    plt.plot(t, Y_b1, label='Эйлер', color='red')
    plt.plot(t, Y_b2, label='Рунге-Кутт', color='blue',marker='*',lw=3)
    plt.plot(t, Y, label='Адамс', color='yellow')
    plt.plot(t, bibl, label='Scipy', color='green',marker='o')
    plt.title('Методы')
    plt.xlabel('Ось x')
    plt.ylabel('Ось y')
    plt.legend()
    plt.show()
def RK1():
    global Y_b2
    k = int(k_en.get())
    a = int(a_en.get())
    h=0.1
    y=0
    x=0
    Y_b2=[]
    if k==-1:
        messagebox.showerror('Ошибка программы', 'k не равно -1')
    
    columns = ("i","xi","yi",'y точное','abs',"pr","Δyi=h*yi’") #таблица
    tree = ttk.Treeview(win1,columns=columns, show="headings")
    tree.place(x=200, y=320,height=150)
    tree.heading("i", text="№", anchor=CENTER)
    tree.heading("xi", text="Значение x", anchor=CENTER)
    tree.heading("yi", text="Значение y", anchor=CENTER)
    tree.heading("y точное", text="y точное", anchor=CENTER)
    tree.heading("abs", text="Абсолютная погр.", anchor=CENTER)
    tree.heading("pr", text="yi’", anchor=CENTER)
    tree.heading("Δyi=h*yi’", text="Δyi=h*yi’", anchor=CENTER)
    
    tree.column("#1", stretch=NO, width=80)
    tree.column("#2", stretch=NO, width=130)
    tree.column("#3", stretch=NO, width=130)
    tree.column("#4", stretch=NO, width=130)
    tree.column("#5", stretch=NO, width=130)
    tree.column("#6", stretch=NO, width=130)
    tree.column("#7", stretch=NO, width=130)
    
    for i in range(11):
        yi=round(f(a,k,x,y),5)
        y_toch=round(toch_resh(a,k,x),5)
        pogr=round(abs(y_toch-y),5)
        k1=h*f(a,k,x,y)
        k2=h*f(a,k,x+h/2,y+k1/2)
        k3=h*f(a,k,x+h/2,y+k2/2)
        k4=h*f(a,k,x+h,y+k3)
        next_y=round((k1+2*k2+2*k3+k4)/6,5)
        tree.insert('','end', values=(i,x,y,y_toch,pogr,yi,next_y))
        x=round(x+h,1)
        Y_b2.append(y)
        y=round(y+next_y,5)
    
def AD():
    global Y
    k = int(k_en.get())
    a = int(a_en.get())
    h=0.1
    y=0
    x0=0
    X=[]
    for i in range(11):
        X.append(round(x0+h*i,1))
    Y = []
    if k==-1:
        messagebox.showerror('Ошибка программы', 'k не равно -1')
    
    columns = ("i","xi","yi",'y точное','abs',"pr","Δyi=h*yi’") #таблица
    tree = ttk.Treeview(win1,columns=columns, show="headings")
    tree.place(x=200, y=500,height=150)
    tree.heading("i", text="№", anchor=CENTER)
    tree.heading("xi", text="Значение x", anchor=CENTER)
    tree.heading("yi", text="Значение y", anchor=CENTER)
    tree.heading("y точное", text="y точное", anchor=CENTER)
    tree.heading("abs", text="Абсолютная погр.", anchor=CENTER)
    tree.heading("pr", text="yi’", anchor=CENTER)
    tree.heading("Δyi=h*yi’", text="Δyi=h*yi’", anchor=CENTER)
    
    tree.column("#1", stretch=NO, width=80)
    tree.column("#2", stretch=NO, width=130)
    tree.column("#3", stretch=NO, width=130)
    tree.column("#4", stretch=NO, width=130)
    tree.column("#5", stretch=NO, width=130)
    tree.column("#6", stretch=NO, width=130)
    tree.column("#7", stretch=NO, width=130)
    q=[]
    next_y = 0
    for i in range(0, 4):
        x = X[i]
        yi=round(f(a,k,x,y),5)
        y_toch=round(toch_resh(a,k,x),5)
        pogr=round(abs(y_toch-yi),5)
        y += next_y
        Y.append(round(y,5))
        tree.insert('','end', values=(i,X[i],Y[i],y_toch,pogr,yi,next_y))
        q.append(h*f(a,k,x, y))
        k1=h*f(a,k,x,y)
        k2=h*f(a,k,x+h/2,y+k1/2)
        k3=h*f(a,k,x+h/2,y+k2/2)
        k4=h*f(a,k,x+h,y+k3)
        next_y = round((k1+2*k2+2*k3+k4) / 6,5)
    for i in range(3, 10):
        x=X[i]
        yi=round(f(a,k,x,y),5)
        y_toch=round(toch_resh(a,k,X[i+1]),5)
        pogr=round(abs(y_toch-y),5)
        next_y = round(q[i] + 1/2 * (q[i]-q[i-1]) + 5/12 * (q[i-1] - q[i-2]) ** 2 + 3/8 * (q[i-2] - q[i-3]) ** 3,5)
        y=round(Y[i] + next_y,5)
        Y.append(y)
        tree.insert('','end', values=(i+1,X[i+1],Y[i+1],y_toch,pogr,yi,next_y))
        q.append(h * f(a,k,X[i+1], Y[i+1]))
def f1(y1,y2):
    return 2*y1-y2
def f2(x,y1,y2):
    return -2*y1+y2+18*x
def toch_resh1(x):
    return math.exp(3*x)+3*x**2+2*x+1
def toch_resh2(x):
    return -(math.exp(3*x))+6*x**2-2*x
def Eil2():
    h=0.1
    y1=2
    y2=-1
    x=0
    X=[]
    Y1=[]
    Y2=[]
    Y1_t=[]
    Y2_t=[]
    columns = ("i","xi","yi1",'y1 точное','abs1',"yi2",'y2 точное','abs2') #таблица
    tree = ttk.Treeview(win2,columns=columns, show="headings")
    tree.place(x=10, y=160,height=150)
    tree.heading("i", text="№", anchor=CENTER)
    tree.heading("xi", text="X", anchor=CENTER)
    tree.heading("yi1", text="Y1", anchor=CENTER)
    tree.heading("y1 точное", text="Y1 точное", anchor=CENTER)
    tree.heading("abs1", text="Абсолютная погр.", anchor=CENTER)
    tree.heading("yi2", text="Y2", anchor=CENTER)
    tree.heading("y2 точное", text="Y2 точное", anchor=CENTER)
    tree.heading("abs2", text="Абсолютная погр.", anchor=CENTER)
    
    tree.column("#1", stretch=NO, width=30)
    tree.column("#2", stretch=NO, width=50)
    tree.column("#3", stretch=NO, width=65)
    tree.column("#4", stretch=NO, width=90)
    tree.column("#5", stretch=NO, width=105)
    tree.column("#6", stretch=NO, width=65)
    tree.column("#7", stretch=NO, width=90)
    tree.column("#8", stretch=NO, width=105)
    
    for i in range(11):
        X.append(x)
        Y1.append(y1)
        Y2.append(y2)
        yi1=round(f1(y1,y2),5)
        yi2=round(f2(x,y1,y2),5)
        y1_toch=round(toch_resh1(x),5)
        Y1_t.append(y1_toch)
        y2_toch=round(toch_resh2(x),5)
        Y2_t.append(y2_toch)
        pogr1=round(abs(y1_toch-y1),5)
        pogr2=round(abs(y2_toch-y2),5)
        next_y1=round(yi1*h,5)
        next_y2=round(yi2*h,5)
        tree.insert('','end', values=(i,x,y1,y1_toch,pogr1,y2,y2_toch,pogr2))
        x=round(x+h,1)
        y1=round(next_y1+y1,5)
        y2=round(next_y2+y2,5)
    
    fig = plt.figure(figsize=(7, 3), dpi=110)
    ax = fig.add_subplot(1, 2, 1)
    ax.plot(X, Y1, X, Y1_t)
    ax.scatter(X, Y1, X, Y1_t)
    ax.grid(True)
    bx = fig.add_subplot(1, 2, 2)
    bx.plot(X, Y2, X, Y2_t)
    bx.scatter(X, Y2, X, Y2_t)
    bx.grid(True)
    canvas = FigureCanvasTkAgg(fig, master=win2)
    canvas.get_tk_widget().place(x=620, y=50)
    canvas.draw()

def RK2():
    h=0.1
    y1=2
    y2=-1
    x=0
    X=[]
    Y1=[]
    Y2=[]
    Y1_t=[]
    Y2_t=[]
    columns = ("i","xi","yi1",'y1 точное','abs1',"yi2",'y2 точное','abs2') #таблица
    tree = ttk.Treeview(win2,columns=columns, show="headings")
    tree.place(x=10, y=440,height=150)
    tree.heading("i", text="№", anchor=CENTER)
    tree.heading("xi", text="X", anchor=CENTER)
    tree.heading("yi1", text="Y1", anchor=CENTER)
    tree.heading("y1 точное", text="Y1 точное", anchor=CENTER)
    tree.heading("abs1", text="Абсолютная погр.", anchor=CENTER)
    tree.heading("yi2", text="Y2", anchor=CENTER)
    tree.heading("y2 точное", text="Y2 точное", anchor=CENTER)
    tree.heading("abs2", text="Абсолютная погр.", anchor=CENTER)
    
    tree.column("#1", stretch=NO, width=30)
    tree.column("#2", stretch=NO, width=50)
    tree.column("#3", stretch=NO, width=65)
    tree.column("#4", stretch=NO, width=90)
    tree.column("#5", stretch=NO, width=105)
    tree.column("#6", stretch=NO, width=65)
    tree.column("#7", stretch=NO, width=90)
    tree.column("#8", stretch=NO, width=105)
    
    for i in range(11):
        X.append(x)
        Y1.append(y1)
        Y2.append(y2)
        yi1=round(f1(y1,y2),5)
        yi2=round(f2(x,y1,y2),5)
        y1_toch=round(toch_resh1(x),5)
        Y1_t.append(y1_toch)
        y2_toch=round(toch_resh2(x),5)
        Y2_t.append(y2_toch)
        pogr1=round(abs(y1_toch-y1),5)
        pogr2=round(abs(y2_toch-y2),5)
        k1=h*f1(y1,y2)
        p1=h*f2(x,y1,y2)
        k2=h*f1(y1+k1/2,y2+p1/2)
        p2=h*f2(x+h/2,y1+k1/2,y2+p1/2)
        k3=h*f1(y1+k2/2,y2+p2/2)
        p3=h*f2(x+h/2,y1+k2/2,y2+p2/2)
        k4=h*f1(y1+k3,y2+p3)
        p4=h*f2(x+h,y1+k3,y2+p3)
        next_y1=round((k1+2*k2+2*k3+k4)/6,5)
        next_y2=round((p1+2*p2+2*p3+p4)/6,5)
        tree.insert('','end', values=(i,x,y1,y1_toch,pogr1,y2,y2_toch,pogr2))
        x=round(x+h,1)
        y1=round(next_y1+y1,5)
        y2=round(next_y2+y2,5)
    
    fig = plt.figure(figsize=(7, 3), dpi=110)
    ax = fig.add_subplot(1, 2, 1)
    ax.plot(X, Y1, X, Y1_t)
    ax.scatter(X, Y1_t)
    ax.grid(True)
    bx = fig.add_subplot(1, 2, 2)
    bx.plot(X, Y2, X, Y2_t)
    bx.scatter(X, Y2_t)
    bx.grid(True)
    canvas = FigureCanvasTkAgg(fig, master=win2)
    canvas.get_tk_widget().place(x=620, y=350)
    canvas.draw()
        

window = Tk()
window.title("Решение дифференциальных уравнений")
window.geometry('1366x768')
window.state('zoomed')

tab_control=ttk.Notebook(window)
win1=ttk.Frame(tab_control)
win2=ttk.Frame(tab_control)
tab_control.add(win1, text='Дифференциальное уравнение №1')
tab_control.add(win2, text='Дифференциальное уравнение №2')
tab_control.pack(expand=1, fill='both')

img1 = PhotoImage(file="primer1.png")
label = Label(win1, image=img1)
label.image_ref = img1
label.place(x=0,y=0)

k_lb = Label(win1, text="Введите k", font=("Times New Roman", 16),bg='#B0FEDD')  
k_lb.place(x=600, y=20)
k_en = Entry(win1,font=("Times New Roman Bold", 16))
k_en.place(x=700, y=20, width = 75, height = 26)

a_lb = Label(win1, text="Введите α", font=("Times New Roman", 16),bg='#B0FEDD')  
a_lb.place(x=600, y=70)
a_en = Entry(win1,font=("Times New Roman Bold", 16))
a_en.place(x=700, y=70, width = 75, height = 26)

btn_eil1 = Button(win1, text="Метод Эйлера", font=("Times New Roman", 16), bg='#8CEB2D', command=Eil1)  
btn_eil1.place(x=50, y=140)
btn_rk1 = Button(win1, text="Метод Рунге-Кутта", font=("Times New Roman", 15), bg='#8CEB2D', command=RK1)  
btn_rk1.place(x=10, y=320)
btn_rk1 = Button(win1, text="Метод Адамса", font=("Times New Roman", 15), bg='#8CEB2D', command=AD)  
btn_rk1.place(x=50, y=500)

img1 = PhotoImage(file="primer2.png")
label = Label(win2, image=img1)
label.image_ref = img1
label.place(x=0,y=0)

btn_eil2 = Button(win2, text="Метод Эйлера", font=("Times New Roman", 16), bg='#8CEB2D', command=Eil2)  
btn_eil2.place(x=10, y=120)
btn_rk1 = Button(win2, text="Метод Рунге-Кутта", font=("Times New Roman", 15), bg='#8CEB2D', command=RK2)  
btn_rk1.place(x=10, y=400)

bt_b=Button(win1, text="График Scipy", font=("Times New Roman", 16), bg='#8CEB2D',command=scipy)  
bt_b.place(x=800, y=50)

window.mainloop()