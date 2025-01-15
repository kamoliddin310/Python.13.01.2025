n = int(input("n = "))

for i in range(1, n+1):
    n = int(input(f"{i} - sonni kiriting = "))
    if n % 3 == 0 and n % 2 == 1:
        print(n)