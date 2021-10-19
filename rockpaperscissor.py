#importing packages
from tkinter import *
import random


#defining the window
root = Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title('Rock,Paper,Scissors')
root.config(bg ='teal')


#Title label specifications
Label(root, text = 'Rock, Paper ,Scissors' , font='Broadway 20 bold', bg = 'seashell2').pack()


#Input label specifications
user_take = StringVar()
Label(root, text = 'choose any one: rock, paper ,scissors' , font='Broadway 15 bold', bg = 'gray').place(x = 20,y=70)
Entry(root, font = 'Jokerman 15', textvariable = user_take , bg = 'seashell2').place(x=90 , y = 130)


#Computer's Choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
    
Result = StringVar()


#User's Choice
def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('TIE :P , You both selected same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('You loose :( , Computer selected Paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('You win :) , Computer selected Scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('You loose :( , Computer selected Scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('You win :) , Computer selected Rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('You loose :( , Computer selected Rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('You win :) , Computer selected Paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')
        
        
def Reset():
    Result.set("") 
    user_take.set("")


def Exit():
    root.destroy()
    
# Output label specifications    
Entry(root, font = 'Jokerman 10', textvariable = Result, bg ='seashell2',width = 50,).place(x=25, y = 250)

Button(root, font = 'Broadway 13 bold', text = 'PLAY'  ,padx =5,bg ='gray' ,command = play).place(x=150,y=190)

Button(root, font = 'Broadway 13 bold', text = 'RESET'  ,padx =5,bg ='gray' ,command = Reset).place(x=70,y=310)

Button(root, font = 'Broadway 13 bold', text = 'EXIT'  ,padx =5,bg ='gray' ,command = Exit).place(x=230,y=310)


root.mainloop()
