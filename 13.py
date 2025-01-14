a = int(input())
for i in range(2, a + 1):
    d = 2
    while i % d != 0 :
        d += 1    
    if i == d:
        print(i)
        
