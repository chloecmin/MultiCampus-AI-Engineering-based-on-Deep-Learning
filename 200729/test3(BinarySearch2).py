def BinarySearch2(data, key, low, high):
    if low <= high:
        mid = (low + high) // 2
        if data[mid] == key:
            return mid
        elif data[mid] > key:
            return BinarySearch2(data, key, low, mid-1)
        elif data[mid] < key:
            return BinarySearch2(data, key, mid+1, high)


data = [2,4,7,8,10,12,44,67]
key = 10
low = 0
high = len(data)-1
bs = BinarySearch2(data, key, low, high)
print(bs)

