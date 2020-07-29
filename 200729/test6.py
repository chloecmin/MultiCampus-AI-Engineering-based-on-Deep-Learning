#다음의 데이터를 bubble sort하고 binary search하여 결과값이 있는지 검색하시오.

def BubbleSort(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
    return data

    # for i in range(len(data)-1, 0, -1):
    #     max_pos = 0
    #     for j in range(1, i+1):
    #         if data[j]>data[max_pos]:
    #             max_pos = j
    #     temp = data[i]
    #     data[i] = data[max_pos]
    #     data[max_pos] = temp
    # return data
def BubbleSort2(data, len):
    if len == 0:
        return data
    for i in range(len):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
    return BubbleSort2(data, len-1)
def BinarySearch(data, key):
    low = 0
    high = len(data)-1

    while low <= high:
        mid = (low+high)//2
        if data[mid] == key:
            return mid
        elif data[mid] < key:
            low = mid+1
        elif data[mid] > key:
            high = mid-1
def SelectionSort(data):
    for i in range(len(data)):
        min_pos = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_pos]:
                min_pos = j
        # temp = data[i]
        # data[i] = data[min_pos]
        # data[min_pos] = temp
        ##### temp대신 바로 바꿔치기 가능
        data[i], data[min_pos] = data[min_pos], data[i]

    return data

data = [20, 1, 10, 3, 12, 18, 21, 100]
key = 12

print(BubbleSort(data))
print(BinarySearch(data, key))
print(SelectionSort(data))
print(BubbleSort2(data, len(data)-1))