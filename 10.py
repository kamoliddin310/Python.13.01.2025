a = input()
arr = a.split()
max = arr[0]

for i in range(1, len(arr)):
    if len(max) < len(arr[i]):
        max = arr[i]
print(max)