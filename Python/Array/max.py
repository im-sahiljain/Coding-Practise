arr = [1, 1, 2, 2, 2, 3, 3]
max = arr[0]

n = len(arr)
for i in range(0,n):
    if(max < arr[i]):
        max = arr[i]
print(max)
print(i)