a = input()
arr = a.split()
arr = ""
max = arr[0]


for i in range(1, len(arr)+1):
    if len(max) <= len(arr[i]):
        max = arr[i]
print(max)