
from tkinter import*

window = Tk()

photo = PhotoImage(file='esp32pinout.png')
photo2 = PhotoImage(file= 'click.png')

window.geometry("1250x500")
window.title("GUI")
window.config(background= "#d4f8f6")
#--------------------------------------------------------------------------
#label = Label(window, text="Hello world", 
 #             bg="#d4f8f6", 
  #            font = ('Bookman Old Style', 40, 'bold'),
   #           foreground="black",
    #          bd="5",
     #         relief= RAISED,
      #        padx = 10,
       #       pady = 10,
#)
#label.pack()

#label2 = Label(window,
 #              image=photo,)
#label2.pack()


#label.place(x = 700, y = 500)
#---------------------------------------------------------------------------
#----------------------------------------------------------------------------
count = 0

def click():
    global count
    print("Click")
    count += 1


button = Button(window,
                text = "click me",
                font=('Bookman Old Style', 40, 'bold'),
                bg = "#d4f8f6",
                relief=RAISED,
                activebackground= "#d4f8f6",
                image= photo2,
                compound=BOTTOM,
                bd= 15,
                command= click,
                state= ACTIVE,)
button.pack()

def Count():
    print(count)

countButton = Button(window,
                text = "Count",
                font=('Bookman Old Style', 40, 'bold'),
                bg = "#d4f8f6",
                relief=RAISED,
                activebackground= "#d4f8f6",
                command= Count,
                state= ACTIVE,)
countButton.pack()

def DeleteCount():
    global count
    count = 0
    print("The Variable Named 'count' has been reset ")

countDelete = Button(window,
                text = "Reset Count",
                font=('Bookman Old Style', 40, 'bold'),
                bg = "#d4f8f6",
                relief= RAISED,
                activebackground= "#d4f8f6",
                command= DeleteCount,
                state= ACTIVE,)
countDelete.pack()

#---------------------------------------------------------------
#-----------------------------------------------------------------

def printCom():
    username = entry.get()
    print("Print: " + username)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

def enable():
    entry.config(state= NORMAL)

def disable():
    entry.config(state=DISABLED)

entry = Entry(window,
              font=('Bookman Old Style', 20 ,'bold'),
              bg= "#d4f8f6",
              bd = 15,
              relief= RAISED,
              show= "*",)
entry.insert(0, "Insert")

entry.pack(side = LEFT)

boton = Button(window,
                text = "Print It",
                font=('Bookman Old Style', 10, 'bold'),
                bg = "#d4f8f6",
                relief=RAISED,
                activebackground= "#d4f8f6",
                command= printCom,
                state= ACTIVE,
                bd = 10,
                padx = 5,)

boton.pack(side = RIGHT)

deleteBut = Button(window,
                text = "Delete",
                font=('Bookman Old Style', 10, 'bold'),
                bg = "#d4f8f6",
                relief=RAISED,
                activebackground= "#d4f8f6",
                command= delete,
                state= ACTIVE,
                bd = 10,
                padx = 5)

deleteBut.pack(side = RIGHT)

backspace = Button(window,
                text = "Backspace",
                font=('Bookman Old Style', 10, 'bold'),
                bg = "#d4f8f6",
                relief=RAISED,
                activebackground= "#d4f8f6",
                command= backspace,
                state= ACTIVE,
                bd = 10,
                padx = 5,)

backspace.pack(side = RIGHT)

enable = Button(window,
                text = "Enable",
                font=('Bookman Old Style', 10, 'bold'),
                bg = "#d4f8f6",
                relief=RAISED,
                activebackground= "#d4f8f6",
                command= enable,
                state= ACTIVE,
                bd = 10,
                padx = 5,)

enable.pack(side = LEFT)

disable = Button(window,
                text = "disable",
                font=('Bookman Old Style', 10, 'bold'),
                bg = "#d4f8f6",
                relief=RAISED,
                activebackground= "#d4f8f6",
                command= disable,
                state= ACTIVE,
                bd = 10,
                padx = 5,)

disable.pack(side = LEFT)
#-----------------------------------------------------------------
#------------------------------------------------------------

def check():
    if (x.get()==1):
        print("Agree")
    else:
        print("Disagree")


x = IntVar()

cb = Checkbutton(window,
                 text= "Check",
                 font=('Bookman Old Style', 10, 'bold'),
                 foreground='black',
                 bg= '#d4f8f6',
                 activebackground='#d4f8f6',
                 bd= '5',
                 variable= x,
                 onvalue= 1,
                 offvalue= 0,
                 command= check,)

cb.pack()




window.mainloop()

