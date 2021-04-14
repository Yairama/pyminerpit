import numpy as np

file = "Data_Dijkstra.csv"
Data = open(file, 'r').readlines()

unvisited = []
Array_Dijkstra = []
Array_result = []

for i in Data:
    (origen_Data, final_Data, Value) = i.split(',')
    Array_Dijkstra.append([origen_Data, final_Data, int(Value), 0])
    if origen_Data not in unvisited:
        unvisited.append(origen_Data)

        Array_result.append([origen_Data, '', '', 0])

# print(Array_Dijkstra)


origen = 'A'
final = 'P'
count = 1

origen2 = origen

# Initial

Ruta = []

for i in range(0, len(Array_result)):

    if Array_result[i][0] == origen:
        Array_result[i][1] = 0
        Array_result[i][2] = 0
        Array_result[i][3] = 1

ValueMin = 0
count_aux = 1
Ruta.append(origen)

Value_Accumulate = 0

while count <= (len(Array_result) - 1):

    Value_Accumulate = ValueMin

    firs_origen = origen

    Final_Temporal = []

    # print(Array_Dijkstra)

    for i in Array_Dijkstra:
        if i[0] == origen:
            Final_Temporal.append([i[1], i[2]])

    # print(Array_result)

    for i in range(0, len(Array_result)):

        for t in range(len(Final_Temporal)):
            temporal = Final_Temporal[t]

            if Array_result[i][0] == temporal[0]:

                if int(Array_result[i][3]) == 1:

                    t = len(Final_Temporal) + 1
                else:
                    # verify the value to save
                    if count_aux == 1:
                        Array_result[i][2] = temporal[1]
                    else:

                        if Array_result[i][2] == "":
                            ValueSaved = 0

                            C = Value_Accumulate + int(temporal[1])

                        else:
                            ValueSaved = int(Array_result[i][2])
                            C = Value_Accumulate + int(temporal[1])

                            if C >= ValueSaved:
                                C = ValueSaved

                        Array_result[i][2] = C

    Temporal = []

    for i in range(0, len(Array_result)):
        c = Array_result[i][2]
        if c != '':
            c = int(c)
            if c == 0:
                c = 999
            if int(Array_result[i][3]) == 1:
                c = 999
            Temporal.append(c)
        else:
            Temporal.append(999)

    np_array = np.array(Temporal)

    n = np.where(min(np_array) == np_array)

    location_min = (n[0][0])
    Array_result[location_min][1] = min(np_array)
    Array_result[location_min][3] = 1
    origen = Array_result[location_min][0]

    count = count + 1

    count_aux = count_aux + 1
    Ruta.append(origen)
    ValueMin = min(np_array)

# Min = Array_result[i][2]


# Precaution with more of tow values min

Array_result = np.array(Array_result)

count = 1

for i in range(0, len(Array_result)):
    if Array_result[i][0] == final:
        Array_result[i][3] = 2

# 5
verify_origen = False
Road = final
ValueRoad = 0

for i in Array_result:
    if final == i[0]:
        ValueRoad = i[1]


while verify_origen == False:

    FinalOrigen = final

    Value_return = []

    for i in Array_Dijkstra:
        if final == i[0]:
            Value_return.append((i[1], i[2]))

    ValueResult = 0

    for i in Array_result:
        if final == i[0]:
            ValueResult = i[1]


    for vert in Value_return:
        for n in range(len(Array_result)):
            i = Array_result[n]

            if vert[0] == i[0]:
                aux = int(ValueResult) - int(vert[1])
                if aux == int(i[1]):
                    final = vert[0]
                    Array_result[n][3] = 2
                    Road= Road + " --> " + final

                    if final == origen2:
                        verify_origen = True


print(Road + " : with value of " + ValueRoad)

