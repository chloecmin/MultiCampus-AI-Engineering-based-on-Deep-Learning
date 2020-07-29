def BinarySearch(data, key):
    low, high = 0, len(data)-1
    # print(low, high)

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == key:
            # print("found : ", mid)
            return mid
            break
        elif data[mid] > key:
            high = mid-1
        elif data[mid] < key:
            low = mid+1

data = [2,4,7,8,10,12,44,67] #전제조건 : 정렬이 되어있어야 함.
key = 10
bs = BinarySearch(data, key)
print(bs)