def insertSort(data):
    for index in range(1, len(data)):
        position = index
        currentvalue = data[index]
        while position > 0 and data[position-1]>currentvalue:
            data[position] = data[position-1]
            position = position-1
        data[position] = currentvalue
    return data

data = [18, 12, 59, 45, 72, 51]
print(insertSort(data))
