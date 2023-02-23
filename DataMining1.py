my_list = [23,15,75,56,90,40]

def my_min_max(list):
    maxVal = max(list)
    minVal = min(list)

    for i in list:
        norm = (i-minVal)/(maxVal-minVal)
        print(norm)

my_min_max(my_list)
