import numpy as np
import tkinter as tkr

print('**********LERSCH-GROSSMAN´s ALGORITHM**********', '\n')

# Let's import the block matrix
name = input('Enter the file name : ')
matrix = np.loadtxt(name + '.txt')
print('\n*** The initial matrix is :')
print(matrix)
# A row of zeros is inserted for subsequent calculations
(fil, col) = np.shape(matrix)
M1 = matrix.copy()
f_cero = [list(np.zeros(col))]  # To generate a 2D array (list list)
M1 = np.append(f_cero, M1, axis=0)
print(f'\n***** Number of rows: {fil} and columns: {col} *****')

# The step sum is performed
M2 = M1.copy()
for j in range(col):
    for i in range(1, fil + 1):
        M2[i, j] = M2[i, j] + M2[i - 1, j]
print('\n*** Matrix with the step sum:')
print(M2, '\n')

# Sum of the 1st Column adding the value blocks (-2)
M3 = M2.copy()
val = int(input('waste blocks value : '))
for i in range(1, fil + 1):
    M3[i, 0] = M3[i, 0] + (i * (i - 1) / 2) * val

print('\n***Lets see the first row ***')
print(M3[:, 0:1])  # print first column of matrix M3

# The maximum value of the 3 closest blocks is chosen
for j in range(1, col):
    for i in range(1, fil + 1):
        if i != fil:
            M3[i, j] = M3[i, j] + max(M3[i - 1, j - 1], M3[i, j - 1], M3[i + 1, j - 1])
        else:
            M3[i, j] = M3[i, j] + max(M3[i - 1, j - 1], M3[i, j - 1])

# Seeing the real Matrix
MO = M3.copy()
MO = MO[1:, :]
print('\n*** Pit Optimum Matrix :')
print(MO)

# Identifying the Pit Optimum contour
L_row = []
L_col = []
row = 1
maximo = max(M3[row])
column = np.where(M3[row] == maximo)[0][0]  # starts the search in row 1 and gets the column of the largest
while maximo != 0:  # avoid zero so as not to take the first row of zeros
    L_row.append(row)
    L_col.append(column)
    values = [M3[row - 1, column - 1], M3[row, column - 1], M3[row + 1, column - 1]]
    maximo = max(values)

    column = column - 1
    if maximo == values[0]:
        row = row - 1  # makes it rise to the surface
    elif maximo == values[2]:
        row = row + 1
        # makes it go down to the bottom of the pit

# Creating the Interface
# The root
matrix = tkr.Tk()
matrix.title('Optimum Pit')
geo = str(col * 80) + 'x' + str(fil * 60)
matrix.geometry(geo)

# El frame o ambiente
myFrame = tkr.Frame()
myFrame.pack(fill='both', expand=True)
myFrame.config(background='lightyellow')
# Labels for the valued blocks
final_value = 0
for j in range(0, col):
    for i in range(1, fil + 1):
        text = str(int(M1[i, j]))
        if j in L_col:
            indexx = L_col.index(j)
            if i <= L_row[indexx]:
                myLabel = tkr.Label(myFrame, text=text, font=('Arial', 28),
                                    # green when above the final line of the optimal pit
                                    background='lightgreen', width=3)
                final_value = final_value + int(M1[i, j])
                # we will use matrix M1 because this is the initial
            else:
                myLabel = tkr.Label(myFrame, text=text, font=('Arial', 28),
                                    # red when below the final line of the optimal pit
                                    background='red', width=3)
        else:
            myLabel = tkr.Label(myFrame, text=text, font=('Arial', 28),  # red when column is not in L_col
                                background='red', width=3)
        myLabel.grid(row=i + 1, column=j + 1, padx=3, pady=3)

print('\n******final value of the optimal pit is', final_value, '********')
matrix = tkr.mainloop()
