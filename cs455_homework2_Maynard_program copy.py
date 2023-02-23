"""
Lukas Maynard, Caige Rogers, Beethoven Meginnis, Hunter Raymond
"""
from math import fabs
import csv

#-------------------------------------------
def normalizeData(data):
    newData = []
    for i in range(len(data)):
        newValue = (data[i] - min(data))/ (max(data) - min(data))
        newData.append(newValue)
    return newData


#output1 = normalizeData(testData)
#print(output1)
#print("------------")

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

#output2 = computeDistanceMatrix(output1)

#for i in output2:
#    print(i)

#print("------------")

testDataNominal = ['blue', 'green', 'red', 'blue', 'white', 'red' ]

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

#output3 = computeDistanceNominal(testDataNominal)

#for i in output3:
#    print(i)

#print("------------")


testDataOrdinal = ['freshman', 'senior', 'junior', 'freshman', 'sophmore', 'junior']

#-------------------------------------------
def computeDistanceOrdinal(data):
    distanceMatrix = []
    rank_order = ['freshman', 'sophomore', 'junior', 'senior']
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

#output4  = computeDistanceOrdinal(testDataOrdinal)

#for i in output4:
#    print(i)

#print("------------")


#-------------------------------------------
def computeDistanceNumerical(data):
    distanceMatrix = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data)):
            difference = round(fabs(data[i] - data[j]), 2)
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



fin = open("cs455_homework2_Maynard_dataset.csv" ,'r')

data_raw = []
for l in fin:
    data_raw.append(l)

data_temp = []

for element in data_raw:
    data_temp.append(element.strip().split(','))

mainData = []
for i in data_temp:
    mainData.append(i[-1])
#print(mainData)

mainData.remove("Million Units")


integerData = []
for i in mainData:
    integerData.append(float(i))

normData = normalizeData(integerData)
#print(normData)
matrixData = computeDistanceMatrix(normData)
#print(matrixData)

desired_i = int(input("Input the first object index (0-99)"))

desired_j = int(input("Input the second object index (0-99)"))


distance = matrixData[desired_i][desired_j]
print(distance)