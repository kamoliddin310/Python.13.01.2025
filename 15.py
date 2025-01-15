a = input()

curr = 0
count = 1
new_word = ""

while curr + 1 < len(a):
    if a[curr] == a[curr + 1]:
        count += 1
    else:
        new_word += f"{count}{a[curr]}"
        count = 1
    curr += 1

new_word += f"{count}{a[curr]}"
print(new_word)