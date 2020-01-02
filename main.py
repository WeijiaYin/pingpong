import numpy as np
import generate
import readFile
import strassen
import find_playerx
import tkinter as tk


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

window.geometry('500x800')

label_iput = tk.Label(window, text="Please input the number of player or the file path")
label_iput.pack()
e_generate = tk.Entry(window)
e_generate.pack()

bt_generate = tk.Button(window, text='ok', command=calcuate_matrix)
bt_generate.pack()

label_matrix = tk.Label(window, text="matrix:")
label_matrix.pack()
var1 = tk.StringVar()
l = tk.Label(window, width=500, textvariable=var1)
l.pack()

label_k2 = tk.Label(window, text="k = 2")
label_k2.pack()
var2 = tk.StringVar()
l2 = tk.Label(window, width=500, textvariable=var2)
l2.pack()

label_k12 = tk.Label(window, text="k = 1 and k =2")
label_k12.pack()
var3 = tk.StringVar()
l3 = tk.Label(window, width=500, textvariable=var3)
l3.pack()

label_playerX = tk.Label(window, text="playerX:")
label_playerX.pack()
var4 = tk.StringVar()
l4 = tk.Label(window, width=500, textvariable=var4)
l4.pack()

window.mainloop()
