from math import abs

"""
rankList = ["D","C","B","A","S"]
rank = []
count = 0

def normalization(List):
    for i in List:
        rank.append((List.index(i)/(len(List)-1)))
    return rank

print(normalization(rankList))


def my_distance(input1,input2):
    x = rankList.index(input1)
    y = rankList.index(input2)

    return abs(rank[x]-rank[y])



#----------------------------
inputnumeric=[]

def distance(input,ranks):
    for i in range(len(input)):
        for k in ranks:
            if input(i) == ranks[k]:
                inputnumeric.append(k/len(ranks)-1)
#---------------------------------------------------------"""

testData = [300, 250, 220, 190, 100, 160]

def normalizeData(data):
    newData = []
    for i in range(len(data)):
        newValue = (data[i] - min(data))/ (max(data) - min(data))
        newData.append(newValue)
    return newData

normalizeData(testData)