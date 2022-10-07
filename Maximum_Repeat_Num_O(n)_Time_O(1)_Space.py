arr = [2, 3, 3, 5, 3, 4, 1, 7]
k = 8
n = 8
#Modifying array
for i in range(0, n):
    arr[arr[i] % k] += k

# Find index of the maximum repeating element
max = arr[0]
result = 0
for i in range(1, n):

    if arr[i] > max:
        max = arr[i]
        result = i
print(result)
