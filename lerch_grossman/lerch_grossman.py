import numpy as np
import tkinter as tkr

print('********** ALGORITMO DE LERSCH-GROSSMAN **********', '\n')

# Importemos la matriz de bloques
name = input('Ingrese el nombre del archivo: ')
matriz = np.loadtxt(name + '.txt')
print('\n*** La matriz inicial es:')
print(matriz)
# Se inserta una fila de ceros para los calculos posteriores
(fil, col) = np.shape(matriz)
M1 = matriz.copy()
f_cero = [list(np.zeros(col))]  # Para generar un arreglo 2D (lista de lista)
M1 = np.append(f_cero, M1, axis=0)
print(f'\n***** Numero de filas: {fil} y columnas: {col} *****')

# Se realiza la suma escalonada
M2 = M1.copy()
for j in range(col):
    for i in range(1, fil + 1):
        M2[i, j] = M2[i, j] + M2[i - 1, j]
print('\n*** Matriz con la suma escalonada:')
print(M2, '\n')

# Suma de la 1ra Columna agregando los bloques de valor (-2)
M3 = M2.copy()
val = int(input('Valor de los bloques estéril: '))
for i in range(1, fil + 1):
    M3[i, 0] = M3[i, 0] + (i * (i - 1) / 2) * val

print('\n*** Veamos la Primera fila ***')
print(M3[:, 0:1])  # imprime primera columna de matriz M3

# Se escoje el maximo valor de los 3 bloques más cercanos
for j in range(1, col):
    for i in range(1, fil + 1):
        if i != fil:
            M3[i, j] = M3[i, j] + max(M3[i - 1, j - 1], M3[i, j - 1], M3[i + 1, j - 1])
        else:
            M3[i, j] = M3[i, j] + max(M3[i - 1, j - 1], M3[i, j - 1])

# Viendo la Matriz real
MO = M3.copy()
MO = MO[1:, :]
print('\n*** Matriz del Pit Optimo:')
print(MO)

# Identificando el contorno del Pit Optimo
L_fil = []
L_col = []
fila = 1
maximo = max(M3[fila])
colu = np.where(M3[fila] == maximo)[0][0]  # inicia la busqueda en la fila 1 y obtiene la columna del mayor
while maximo != 0:  # sirve mucho xd
    L_fil.append(fila)
    L_col.append(colu)
    valores = [M3[fila - 1, colu - 1], M3[fila, colu - 1], M3[fila + 1, colu - 1]]
    maximo = max(valores)

    colu = colu - 1
    if maximo == valores[0]:
        fila = fila - 1  # hace que suba hacia la superficie
    elif maximo == valores[2]:
        fila = fila + 1
        # hace que baje al fondo del pit

# L_fil.reverse()
# L_col.reverse()

### Creando la Interfaz
# La raiz
matriz = tkr.Tk()
matriz.title('Pit Óptimo')
geo = str(col * 80) + 'x' + str(fil * 60)
matriz.geometry(geo)

# El frame o ambiente
myFrame = tkr.Frame()
myFrame.pack(fill='both', expand=True)
myFrame.config(background='lightyellow')
# Labels para los bloques valorizados
final_value = 0
for j in range(0, col):
    for i in range(1, fil + 1):
        texto = str(int(M1[i, j]))
        if j in L_col:
            indice = L_col.index(j)
            if i <= L_fil[indice]:
                myLabel = tkr.Label(myFrame, text=texto, font=('Arial', 28),
                                    # verde cuando está por encima de la linea final del pit optimo
                                    background='lightgreen', width=3)
                final_value = final_value + int(M1[i, j])

            else:
                myLabel = tkr.Label(myFrame, text=texto, font=('Arial', 28),
                                    # rojo cuando está por debajo de la linea final del pit optimo
                                    background='red', width=3)
        else:
            myLabel = tkr.Label(myFrame, text=texto, font=('Arial', 28),  # rojo cuando la columna no está en L_col
                                background='red', width=3)
        myLabel.grid(row=i + 1, column=j + 1, padx=3, pady=3)

print('\n******valor final del pit optimo es', final_value, '********')
matriz = tkr.mainloop()
