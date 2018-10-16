from tkinter import *
from tkinter.ttk import *
from time import *
from datetime import *
from ast import*

print('Список задач пуст, для начала работы добавьте задачу')
print('--------------------------------------')

tasklist=[]
timinglist=[]

win=Tk()
win.title("Менеджер задач")
win.geometry("680x260")

def addtasktolist():
    currentlist=[task_current.get(),category_current.get(),date1.get(),time.get()]
    if currentlist in tasklist:
        print('-----------------')
        print('Ошибка! Задача уже добавлена')
    else:
        tasklist.append(currentlist)
        print('Задача добавлена в список')
        print('-----------------')

def currentasks():
    print('Текущие задачи -------------')
    for i in tasklist:
        print("Задача №",tasklist.index(i)+1,' ',i[0],';',"Категория: ",i[1],';',"назначена на ",i[2],', в ',i[3])
    print('--------------------------------------')
    
def when_num():
    a = tasklist[int(tasknum1.get())-1][2]
    a = a.split('-')
    aa =date(int(a[0]),int(a[1]),int(a[2]))
    bb =date.today()
    cc = aa-bb
    dd = str(cc)
    if dd == '0:00:00':
        print(tasklist[int(tasknum1.get())-1][0],' сегодня, в',tasklist[int(tasknum1.get())-1][3],' часов')
    else:
        print(tasklist[int(tasknum1.get())-1][0],' ','через ',dd.split()[0],' дней, в ',tasklist[int(tasknum1.get())-1][3],' часов')

def todaytasks():
    
    print('--------------------------------------')
    i=0
    for element in tasklist:
        a = element[2]
        a = a.split('-')
        aa =date(int(a[0]),int(a[1]),int(a[2]))
        bb =date.today()
        cc = aa-bb
        dd=str(cc)
        if dd == '0:00:00':
            i=i+1
    if i==0:
        print('Нет задач на сегодня')
    else:
        for element in tasklist:
            a = element[2]
            a = a.split('-')
            aa =date(int(a[0]),int(a[1]),int(a[2]))
            bb =date.today()
            cc = aa-bb
            dd=str(cc)
            if dd == '0:00:00':
                print('Задача ', element[0],' назначена на сегодня в ', element[3])
    print('--------------------------------------')

def deletetask():
    del tasklist[deletenum.get()-1]

def savedata():
    my_file = open("taskdata.txt", "w")
    my_file.write(str(tasklist))
    my_file.close()
    print('Список задач сохранен')

def getdata():
    global tasklist
    my_file = open("taskdata.txt")
    tasklist = my_file.read()
    tasklist=literal_eval(tasklist)
    print('Список задач загружен')
    print('--------------------------------------')
    my_file.close()
    
def weektasks():
    print('--------------------------------------')
    i=0
    for element in tasklist:
        a = element[2]
        a = a.split('-')
        aa =date(int(a[0]),int(a[1]),int(a[2]))
        bb =date.today()
        cc = aa-bb
        dd=str(cc)
        if dd == '0:00:00':
            i=i+1
        elif int(dd.split()[0])<= 7:
            i=i+1
    if i==0:
        print('Нет задач на этой неделе')
        print('--------------------------------------')
    else:
        print('Меньше недели до следующих задач:')
        for element in tasklist:
            a = element[2]
            a = a.split('-')
            aa =date(int(a[0]),int(a[1]),int(a[2]))
            bb =date.today()
            cc = aa-bb
            dd=str(cc)
            if dd != '0:00:00':
                if int(dd.split()[0])<= 7:
                    a = element[2]
                    a = a.split('-')
                    aa =date(int(a[0]),int(a[1]),int(a[2]))
                    bb =date.today()
                    c = aa-bb
                    dd = str(cc)
                    print('Задача ', element[0],'через ', dd.split()[0],' дней')
            elif dd == '0:00:00':
                print(element[0],' сегодня, в',element[3],' часов')
    print('--------------------------------------')

def incategory():
    i=0
    for task in tasklist:
        if category_current_1.get() in task:
            i=i+1
    if i==0:
        print('Нет задач данной категории')
    for task in tasklist:
        if category_current_1.get() in task:
            print("Задача №",tasklist.index(task)+1,' ',task[0],"назначена на ",task[2],', в ',task[3])
    print('--------------------------------------')
    
task_current=StringVar()
categoryes=[]
category_current=StringVar()
category_current_1=StringVar()

deletenum=IntVar()
tasknum1=IntVar()
date1=StringVar()
time=DoubleVar()

label_1=Label(win,text='Введите задачу >')
label_1.grid(row=0,column=0)

task=Entry(win,textvariable=task_current)
task.grid(row=0,column=1)

label_2=Label(win,text='Выберете категорию >')
label_2.grid(row=0,column=2)

frame=Frame(win)
frame.grid(row=0,column=3)
combobox= Combobox(frame,textvariable=category_current,values = [u"Работа",u"Дом",u"Отдых",u"Семья",u"Банк",u"Прочее"])
combobox.grid(column=3,row=0)

label_3=Label(win,text='Введите дату гггг-мм-дд')
label_3.grid(row=1,column=0)

year=Entry(win,textvariable=date1)
year.grid(row=2,column=0)

label_6=Label(win,text='Введите время')
label_6.grid(row=1,column=1)

time=Entry(win,textvariable=time)
time.grid(row=2,column=1)


button1=Button(win,text='Добавить задачу', command=addtasktolist)
button1.grid(row=2,column=2)


button2=Button(win,text='Текущие задачи', command=currentasks)
button2.grid(row=3,column=0)

button3=Button(win,text='Сколько дней до задачи № >', command=when_num)
button3.grid(row=4,column=0)

tasknum=Entry(win,textvariable=tasknum1)
tasknum.grid(row=4,column=1)

button4=Button(win,text='Задачи на сегодня: ', command=todaytasks)
button4.grid(row=5,column=0)

button4_1=Button(win,text='Ближайшие задачи: ', command=weektasks)
button4_1.grid(row=5,column=1)

button5=Button(win,text='Удалить задачу № >', command=deletetask)
button5.grid(row=6,column=0)

deliting=Entry(win,textvariable=deletenum)
deliting.grid(row=6,column=1)

button6=Button(win,text='Сохранить данные', command=savedata)
button6.grid(row=7,column=0)

button7=Button(win,text='Загрузить данные', command=getdata)
button7.grid(row=7,column=1)

button8=Button(win,text='Все задачи из категории >', command=incategory)
button8.grid(row=8,column=0)


frame2=Frame(win)
frame2.grid(row=8,column=1)
combobox2= Combobox(frame2,textvariable=category_current_1,values = [u"Работа",u"Дом",u"Отдых",u"Семья",u"Банк",u"Прочее"])
combobox2.grid(column=1,row=8)



win.mainloop()
