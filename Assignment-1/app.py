import matplotlib.pyplot as plt
import os
from queue import PriorityQueue
import Preprocessing as prp
from tkinter import ttk
from tkinter import *
import Similarity as csim
from tkinter import messagebox

'''The date gets pre-processed first'''
ll = {}
def store():
    tar = open('store.txt', "w")
    tar.write(str(ll))
    tar.close()

def pp():
    file = [doc for doc in os.listdir() if (doc!='temp.txt' and doc!='store.txt') and (doc.endswith('.txt'))]
    for doc in file:
        ll[doc] = prp.Preprocess(doc).tri
    #the prp corpus is stored in a file

#A plot betweeen similarity of the test document and a similar document from database is drawn here
root = Tk()
root.title("Plagiarism Detector") #heading of the main window
Label(root, text="File Name").grid(row=0)
Label(root, text="Input").grid(row=7)
root.geometry("800x450")
b = Entry(root, width=75) # taking name of input file
b.grid(row=0, column=1)

t = Text(root, width=65, height=20) #inputting text to check for Similarity
t.grid(row=7,column=1)
def PreProc():
    pp()
    store()

def checkPlot(): #runs on clicking the check button
    u = t.get("1.0",END)
    w = b.get()
    w = w+'.txt'
    f=open(w,"w")
    f.write(u)
    f.close()
    inp = prp.Preprocess(w).tri
    Y = []
    X = []
    rank = csim.Calculate(ll,inp).rank
    for i in range(len(ll)):
        c = rank.get()
        Y.append(c[0])
        X.append(c[1])
    #plot the similarity graph
    fig = plt.subplots(figsize=(10, 5))
    plt.title("Document Similarity Plot")
    plt.bar(X,Y, color='green',align='center')
    plt.ylabel("Similarity Percentage")
    plt.xlabel("Document Name")
    plt.xticks(rotation = 90)
    plt.tight_layout()
    plt.show()

btn2 = ttk.Button(root, text='Pre-Process', command=PreProc) #button for preprocessing
btn2.grid(row=7,column=2)

btn1 = ttk.Button(root, text='Check Plagiarism', command=checkPlot) #check button
btn1.grid(row=7,column=4)

root.mainloop()
