"""
Lukas Maynard, Caige Rogers, Beethoven Meginnis
"""
from math import fabs

#-------------------------------------------
def normalizeData(data):
    newData = []
    for i in range(len(data)):
        newValue = (data[i] - min(data))/ (max(data) - min(data))
        newData.append(round(newValue,3))
    return newData

#-------------------------------------------
def computeDistanceMatrix(data):
    distanceMatrix = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data)):
            difference = round(fabs(data[i] - data[j]), 2)
            temp.append(difference)
        distanceMatrix.append(temp)
    return distanceMatrix

#-------------------------------------------
def computeDistanceNominal(data):
    distanceMatrix = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data)):
            if (data[i] != data[j]):
                difference = 1
            else: 
                difference = 0
            temp.append(difference)
        distanceMatrix.append(temp)
    return distanceMatrix

#-------------------------------------------
def computeDistanceOrdinal(data):
    distanceMatrix = []
    rank_order = ['Samsung', 'Nokia', 'Apple', 'Huawei',"Xiaomi","Motorola","LG","Sony Ericsson","HTC","Research In Motion (RIM)","Oppo"]
    for i in range(len(data)):
        temp = []
        for j in range(len(data)):
            rank_i = 0
            rank_j = 0
            for k in range(len(rank_order)):
                if (data[i] == rank_order[k]):
                    rank_i = k+1
                if (data[j] == rank_order[k]):
                    rank_j = k+1
                difference = round((fabs(rank_i-rank_j))/(len(rank_order) - 1), 2)           
            temp.append(difference)
        distanceMatrix.append(temp)
    return distanceMatrix

#-------------------------------------------
def computeDistanceFinal(distance_num, distance_cat, distance_or):
    distanceMatrix = []
    for i in range(len(distance_num)):
        temp = []
        for j in range(len(distance_num)):
            average = round((distance_num[i][j] +  distance_cat[i][j] + distance_or[i][j])*(1/3),2)          
            temp.append(average)
        distanceMatrix.append(temp)
    return distanceMatrix
#--------------------------------------------

data_raw = []
Numerical_Data = []
Nominal_Data =[]
Ordinal_Data = []

# open csv and skip the header, add everything to a list
with open("cs455_homework2_Maynard_dataset.csv" ,'r') as csvFile:
    next(csvFile)
    for line in csvFile:
        data_raw.append(line.strip().split(','))
    csvFile.close()

# get needed data from specific columns
for i in data_raw:
    Numerical_Data.append(float(i[-1]))
    Nominal_Data.append(i[-4])
    Ordinal_Data.append(i[1])


distance_Ordinal = computeDistanceOrdinal(Ordinal_Data)
distance_Nominal = computeDistanceNominal(Nominal_Data)

Final_NumericalData = normalizeData(Numerical_Data)
Final_Numerical_Matrix = computeDistanceMatrix(Final_NumericalData)

Distance_Final = computeDistanceFinal(Final_Numerical_Matrix,distance_Nominal,distance_Ordinal)

desired_i = int(input("Input the first object index (0-99): "))
desired_j = int(input("Input the second object index (0-99): "))

output = Distance_Final[desired_i][desired_j]
#print(Distance_Final)
print(output)