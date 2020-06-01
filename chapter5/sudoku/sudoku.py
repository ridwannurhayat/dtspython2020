def checkBoard(arr):
    for a in range(3):
        for b in range(3):
            temp = set()
            for c in range(3):
                for d in range(3):
                    num = lst[c+a*3][d+b*3]
                    if num in temp:
                        return False
                    else:
                        temp.add(num)
    return True

print("Enter numbers:")
lst = []
for _ in range(9):
    lst.append(list(map(int, list(input().strip()))))
if checkBoard(lst):
    print("Yes")
else:
    print("No")
    