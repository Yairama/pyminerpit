import numpy as np

# file="Datalog.txt"
# data=np.loadtxt(file,delimiter='\t',skiprows=0)


# importation of data
file = "Datalog.txt"

(name_file, type_file) = file.split('.')

print(type_file)

if type_file=='txt':
    data_original = np.loadtxt(file, delimiter='\t', skiprows=0)
elif type_file=='csv':
    data_original = np.loadtxt(file, delimiter=',', skiprows=0)
else:
    print('-----------file not defined-------')
    exit()

# determination of fil and column

fil, column = data_original.shape


print(data_original)
Section_cone = data_original


print('-----------------------------------------------------------------')

Sum_Sum_columns = 0
for position_fil in range(fil):

    for position_column in range(column):

        Sum_columns = 0
        value_positive = Section_cone[position_fil][position_column]
        Array_zero=[]
        # the position_fil to define the size cone

        # Restrictions for the formation of floating cone to 45°
        if value_positive >= 0 and position_fil <= position_column and position_column<=((column-1)-position_fil):


            #print('---------'+ str(value_positive))

            # travel in column from location actual (position_fil,position_column) to the formation of cone

            for return_fil in range(position_fil, -1, -1):

                # print(return_fil)

                # range of influence vertical of the floating cone

                return_column = return_fil


                # print(return_fil, return_column)
                Value_Center = Section_cone[position_fil - return_column][position_column]

                # print(str(position_fil - return_column),str(position_column),'--------- '+str(Value_Center))

                Array_zero.append((position_fil - return_column, position_column))

                if (position_fil-return_column) >= 0:



                    # print(Value_Center, position_fil-return_column, position_column, Sum_columns)


                    Sum_columns=Sum_columns+int(Value_Center)

                    # print(Sum_columns)


                    # travel horizontal of position original for the construction of cone

                    for n in range(return_column):

                        Value_right = Section_cone[position_fil-return_column][position_column+(n+1)]
                        Array_zero.append((position_fil-return_column, position_column+(n+1)))

                        Value_left = Section_cone[position_fil - return_column][position_column - (n + 1)]
                        Array_zero.append((position_fil - return_column, position_column - (n + 1)))

                        Sum_columns = Sum_columns + int(Value_left)+int(Value_right)

                        # print(Value_left,Value_right)


                    # print(Sum_columns)

            if Sum_columns >= 0:

                #print(Array_zero)
                for i in Array_zero:
                    #print(Section_cone[i[0]][i[1]])
                    Section_cone[i[0]][i[1]] = 0

                Sum_Sum_columns=Sum_Sum_columns+Sum_columns


    print(Section_cone)
    print('Fil: '+str(position_fil)+' -------Accumulated value of cone = ' + str(Sum_Sum_columns) )
