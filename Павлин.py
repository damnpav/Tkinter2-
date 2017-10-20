import sys
from tkinter import font
from tkinter import *

file_name_out = "Павлин_результат.txt"

def magic_print(x, fout):
    global a
    if (x):
        columns = len(x[0])
        titles = ["From", "To", "Flight", "Departure", "Arrival"]
        column_size = [len(titles[i]) for i in range(columns)]
        for i in range(len(x)):
            for j in range(columns):
                column_size[j] = max(column_size[j], len(x[i][j]))

        for i in range(columns):
            column_size[i] += 2

        print((str(len(x)) + " out of " + str(a.count)).ljust(sum(column_size) + 10, "_") + "  ", file=fout)
        print(" | ".join([str(titles[i]).ljust(column_size[i]) for i in range(columns)]), file=fout)
        print("_" * (sum(column_size) + 10) + "  ", file=fout)

        for i in range(len(x)):
            print(" | ".join([str(x[i][j]).ljust(column_size[j]) for j in range(columns)]), file=fout)
        print("_" * (sum(column_size) + 10) + "  ", file=fout)
        print('\n' * 2, file=fout)


class Timetable:
    def __init__(self, file_name):
        self.__a = []
        self.__count = 0
        fin = open(file_name)
        s = fin.readline()
        while (s):
            self.__a.append(s.split())
            self.__count += 1
            s = fin.readline()

    def __str__(self):
        return "Павлин_данные.txt"

    @property
    def count(self):
        return self.__count

    def Print(self, file_name=file_name_out):  # prints all flights to a file if given
        if (not self.__a):
            return

        fout = open(file_name, 'w')
        magic_print(self.__a, fout)
        fout.close()

        return open(file_name_out).read()

    def From(self, city, file_name=file_name_out):  # prints all flights departing from a given city to a file if given
        ans = []

        for i in range(len(self.__a)):
            if (self.__a[i][0] == city):
                ans.append(self.__a[i])

        fout = open(file_name, 'w')
        magic_print(ans, fout)
        fout.close()

        return open(file_name_out).read()

    def To(self, city, file_name=file_name_out):  # prints all flights arriving to a given city to a file if given
        ans = []

        for i in range(len(self.__a)):
            if (self.__a[i][1] == city):
                ans.append(self.__a[i])

        fout = open(file_name, 'w')
        magic_print(ans, fout)
        fout.close()
        
        return open(file_name_out).read()

    def FromTo(self, start, finish, file_name=file_name_out):  # prints all flights departing from a given to a given city to a
                                                    # file if given
        ans = []

        for i in range(len(self.__a)):
            if (self.__a[i][0] == start and self.__a[i][1] == finish):
                ans.append(self.__a[i])

        fout = open(file_name, 'w')
        magic_print(ans, fout)
        fout.close()
        
        return open(file_name_out).read()

    def Add(self, flight):  # adds a flight information
        self.__a.append(flight)
        self.__count += 1

        fout = open(file_name_out, 'a')
        print(*flight, file=fout)
        fout.close()
        fadd = open("Павлин_данные.txt", 'a')
        print(*flight, file=fadd)
        fadd.close()        



def ToList(ev): # New window To
    global a, v
    
    toplevel = Toplevel()
    toplevel.geometry('300x100')
    toplevel.title('To city')
    toplevel.focus_set()
    w = Label(toplevel, text = "To:", justify = LEFT)
    w.place(x = 0, y = 0, width = 50, height = 20)
    e = Entry(toplevel)
    e.pack()
    city = ""

    def close_top(ev):
        city = e.get()
        out = a.To(city)
        v.set(out)
        toplevel.destroy()
    
    OkBtn = Button(toplevel, text = 'Ok!')
    OkBtn.bind("<Button-1>", close_top)
    OkBtn.place(x = 100, y = 30, width = 100, height = 40)


def FromList(ev): # New window From
    global a, v
    
    toplevel = Toplevel()
    toplevel.geometry('300x100')
    toplevel.title('From city')
    toplevel.focus_set()
    w = Label(toplevel, text = "From:", justify = LEFT)
    w.place(x = 0, y = 0, width = 50, height = 20)
    e = Entry(toplevel)
    e.pack()
    city = ""

    def close_top(ev):
        city = e.get()
        out = a.From(city)
        v.set(out)
        toplevel.destroy()
    
    OkBtn = Button(toplevel, text = 'Ok!')
    OkBtn.bind("<Button-1>", close_top)
    OkBtn.place(x = 100, y = 30, width = 100, height = 40)

def From_ToList(ev): # New window From city To city
    global a, v
    
    toplevel = Toplevel()
    toplevel.geometry('300x150')
    toplevel.title('From city')
    toplevel.focus_set()
    w1 = Label(toplevel, text = "From:", justify = LEFT)
    w1.place(x = 0, y = 0, width = 50, height = 20)
    e1 = Entry(toplevel)
    e1.pack()
    w2 = Label(toplevel, text = "To:", justify = LEFT)
    w2.place(x = 0, y = 19, width = 50, height = 20)
    e2 = Entry(toplevel)
    e2.pack()
    start = ""
    finish = ""

    def close_top(ev):
        start = e1.get()
        finish = e2.get()
        out = a.FromTo(start, finish)
        v.set(out)
        toplevel.destroy()
    
    OkBtn = Button(toplevel, text = 'Ok!')
    OkBtn.bind("<Button-1>", close_top)
    OkBtn.place(x = 100, y = 100, width = 100, height = 40)

def AddFlight(ev): # New window "Add flight"
    global a, v
    
    toplevel = Toplevel()
    toplevel.geometry('400x200')
    toplevel.title('From city')
    toplevel.focus_set()
    w1 = Label(toplevel, text = "From:", justify = LEFT)
    w1.place(x = 0, y = 0, width = 100, height = 20)
    e1 = Entry(toplevel)
    e1.pack()
    w2 = Label(toplevel, text = "To:", justify = LEFT)
    w2.place(x = 0, y = 19, width = 100, height = 20)
    e2 = Entry(toplevel)
    e2.pack()
    w3 = Label(toplevel, text = "Flight:", justify = LEFT)
    w3.place(x = 0, y = 38, width = 100, height = 20)
    e3 = Entry(toplevel)
    e3.pack()
    w4 = Label(toplevel, text = "Dep. Time:", justify = LEFT)
    w4.place(x = 0, y = 57, width = 100, height = 20)
    e4 = Entry(toplevel)
    e4.pack()
    w5 = Label(toplevel, text = "Arr. Time:", justify = LEFT)
    w5.place(x = 0, y = 76, width = 100, height = 20)
    e5 = Entry(toplevel)
    e5.pack()
    start = ""
    finish = ""

    def close_top(ev):
        From = e1.get()
        To = e2.get()
        f = e3.get()
        dep = e4.get()
        arr = e5.get()
        out = a.Add([From, To, f, dep, arr])
        toplevel.destroy()
    
    OkBtn = Button(toplevel, text = 'Ok!')
    OkBtn.bind("<Button-1>", close_top)
    OkBtn.place(x = 175, y = 150, width = 100, height = 40)

def PrintList(ev): # prints all flights
    global a, v
    out = a.Print()
    v.set(out)

def Quit(ev): # Close
    global root
    root.destroy()

def Str(ev): # Show File name
    global a
    
    toplevel = Toplevel()
    toplevel.geometry('300x100')
    toplevel.title('Str')
    toplevel.focus_set()
    w = Label(toplevel, text = str(a), justify = LEFT)
    w.place(x = 0, y = 0, width = 300, height = 30)

    def close_top(ev):
        toplevel.destroy()
    
    OkBtn = Button(toplevel, text = 'Ok!')
    OkBtn.bind("<Button-1>", close_top)
    OkBtn.place(x = 100, y = 30, width = 100, height = 40)




a = Timetable("Павлин_данные.txt")


root = Tk()

panelFrame = Frame(root, height = 110, width = 1000)
textFrame = Frame(root, height = 700, width = 1000)

panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

my_font = font.Font(family='Consolas', size=12)

v = StringVar()
v.set("Hello, world!")

lll = Label(textFrame, textvariable = v, justify = LEFT, font = my_font)
lll.place(x = 0, y = 10, width = 890, height = 700)


ToBtn = Button(panelFrame, text = 'To')
FromBtn = Button(panelFrame, text = 'From')
From_ToBtn = Button(panelFrame, text = 'From To')
AddBtn = Button(panelFrame, text = 'Add')
PrintBtn = Button(panelFrame, text = 'Print All')
QuitBtn = Button(panelFrame, text = 'Quit')
StrBtn = Button(panelFrame, text = 'Str')

ToBtn.bind("<Button-1>", ToList)
FromBtn.bind("<Button-1>", FromList)
From_ToBtn.bind("<Button-1>", From_ToList)
AddBtn.bind("<Button-1>", AddFlight)
PrintBtn.bind("<Button-1>", PrintList)
QuitBtn.bind("<Button-1>", Quit)
StrBtn.bind("<Button-1>", Str)

ToBtn.place(x = 10, y = 10, width = 100, height = 40)
FromBtn.place(x = 120, y = 10, width = 100, height = 40)
From_ToBtn.place(x = 230, y = 10, width = 100, height = 40)
AddBtn.place(x = 10, y = 60, width = 100, height = 40)
PrintBtn.place(x = 120, y = 60, width = 100, height = 40)
QuitBtn.place(x = 230, y = 60, width = 100, height = 40)
StrBtn.place(x = 340, y = 10, width = 100, height = 40)

root.mainloop()
