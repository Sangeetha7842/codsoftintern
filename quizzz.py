import tkinter as tk
from tkinter import *
import random

questions=[
        "Who developed Python Programming Language?",
        "Which type of Programming does Python support?",
        "Which of the following is the correct extension of the Python file?",
        "Is Python case sensitive when dealing with identifiers?",
        "Which keyword is used for function in Python language?"
        ]

answers_choice=[
        ["Wick van Rossum","Rasmus Lerdorf","Guido van Rossum","Niene Stom"],
        ["object-oriented programming","structured programming","functional programming","all of the mentioned"],
        [".python",".pl",".py",".p"],
        ["no","yes","machine dependent","none of the mentioned"],
        ["Function","def","Fun","Define"],
]

answers = [3,4,3,2,2]

user_answer = []

indexes=[]
def generator():
    global indexes
    while(len(indexes)<5):
        x=random.randint(0,4)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    #print(indexes)
    
def showresult(score):
    labelquestion.destroy()
    op1.destroy()
    op2.destroy()
    op3.destroy()
    op4.destroy()
    labelresult=Label(quiz,text=f'Your score is {score}/5',font=("Times New Roman",50,"bold"),bg="light green")
    labelresult.pack(pady=(100,50))
    labelpercent=Label(quiz,text=f'You secured {score/5*100}%',font=("Times New Roman",50,"bold"),bg="lightgreen")
    labelpercent.pack(pady=(100,50))
    
    
def calc():
    global indexes,user_answer,answers
    x=0
    score=0
    for i in indexes:
        
            score=score+1
       
    print(score)
    showresult(score)
    
    
ques=1
def selected():
    global option,user_answer
    global labelquestion,op1,op2,op3,op4 
    global ques
    
  
    if ques<5:
        labelquestion.config(text=questions[indexes[ques]])
        op1['text']=answers_choice[indexes[ques]][0]   
        op2['text']=answers_choice[indexes[ques]][1] 
        op3['text']=answers_choice[indexes[ques]][2]
        op4['text']=answers_choice[indexes[ques]][3]  
        ques+=1
        
    else:
        print(indexes)
        print(user_answer)
        print(answers)
        calc()

def startquiz():
    global labelquestion,op1,op2,op3,op4 
    labelquestion = Label(quiz,
                          text = questions[indexes[0]],
                          font = ("Times New Roman",30),
                          width = 500,
                          justify = "left",
                          wraplength = 700,
                          bg = 'white')
    labelquestion.pack(pady=(100,30))
    
    global Option
    option = IntVar()
    option.set(-1)
    
    op1 = Radiobutton(quiz,
                      text=answers_choice[indexes[0]][0],
                      font=("Times New Roman",25),
                      value=0,
                      variable=option,
                      command=selected,
                      bg = 'white')
    op1.pack(pady=5)
    
    op2 = Radiobutton(quiz,
                      text=answers_choice[indexes[0]][1],
                      font=("Times New Roman",25),
                      value=1,
                      variable=option,
                      command=selected,
                      bg = 'white')
    op2.pack(pady=5)
    
    op3 = Radiobutton(quiz,
                      text=answers_choice[indexes[0]][2],
                      font=("Times New Roman",25),
                      value=2,
                      variable=option,
                      command=selected,
                      bg = 'white')
    op3.pack(pady=5)
    
    op4 = Radiobutton(quiz,
                      text=answers_choice[indexes[0]][3],
                      font=("Times New Roman",25),
                      value=3,
                      variable=option,
                      command=selected,
                      bg = 'white')
    op4.pack(pady=5)
    
    
def startispressed():
    labeltext.destroy()
    labelinstruction.destroy()
    labelRules.destroy()
    btnStart.destroy()
    generator()
    startquiz()
    
quiz=tk.Tk()
quiz.geometry('800x600')
quiz.title('Quiz Game')

quiz.config(bg='white')


labeltext = Label(quiz,text="Python Quiz",font=("Times New Roman",70,"bold"),bg="white")
labeltext.pack(pady=(0,50))




btnStart = Button(quiz,relief=FLAT,border=0,command = startispressed)
btnStart.pack()

labelinstruction = Label(quiz,text='READ THE RULES AND\nClick Start Once You are Ready',bg='lightgreen',font=("Times New Roman",25),justify="center")
labelinstruction.pack()

labelRules = Label(quiz,
                   text = "1.This Quiz contains 5 questions \n 2.You will get 20 seconds to answer a question.",
                   width = 100,
                   font = ("Times New Roman",15))
labelRules.pack()

quiz.mainloop()   
        
    
                      
                          

