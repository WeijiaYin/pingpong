import numpy as np
import generate
import readFile
import strassen
import find_playerx
import tkinter as tk
np.set_printoptions(threshold=np.inf)


def calcuate_matrix():
    if e_generate.get().isdigit():
        matrix = generate.generate_matrix(int(e_generate.get()))
    else:
        matrix = readFile.input_matrix(e_generate.get())
    var1.set(matrix)
    k2 = strassen.strassen(matrix, matrix)
    var2.set(k2)
    k12 = np.array(strassen.matrix_addition(k2,strassen.add_zeros(matrix)))
    var3.set(k12)
    player_x = find_playerx.find_player_x(len(matrix), k12)
    var4.set(player_x)


window = tk.Tk()
window.title('ping pong')
width, height = 500, 600
window.geometry("%dx%d+30+30"%(width,height))
window.resizable(0,0)
canvas=tk.Canvas(window,width=width,height=height,scrollregion=(-1000,-1000,5000,8000))
canvas.place(x = 0, y = 0)
frame = tk.Frame(canvas)
frame.place(width=width, height=height)
label_iput = tk.Label(frame, text="Please input the number of player or the file path")
label_iput.pack()
e_generate = tk.Entry(frame)
e_generate.pack()

bt_generate = tk.Button(frame, text='ok', command=calcuate_matrix)
bt_generate.pack()

label_matrix = tk.Label(frame, text="matrix:")
label_matrix.pack()
var1 = tk.StringVar()
l = tk.Label(frame, width=500, textvariable=var1)
l.pack()

label_k2 = tk.Label(frame, text="k = 2")
label_k2.pack()
var2 = tk.StringVar()
l2 = tk.Label(frame, width=5000, textvariable=var2)
l2.pack()

label_k12 = tk.Label(frame, text="k = 1 and k =2")
label_k12.pack()
var3 = tk.StringVar()
l3 = tk.Label(frame, width=5000, textvariable=var3)
l3.pack()

label_playerX = tk.Label(frame, text="playerX:")
label_playerX.pack()
var4 = tk.StringVar()
l4 = tk.Label(frame, width=500, textvariable=var4)
l4.pack()
vbar=tk.Scrollbar(canvas,orient=tk.VERTICAL)
vbar.place(x = width-20,width=20,height=height)
vbar.configure(command=canvas.yview)
hbar=tk.Scrollbar(canvas,orient=tk.HORIZONTAL)
hbar.place(x =0,y=height-20,width=width,height=20)
hbar.configure(command=canvas.xview)
canvas.config(xscrollcommand=hbar.set,yscrollcommand=vbar.set)
canvas.create_window((width,height), window=frame)
window.mainloop()