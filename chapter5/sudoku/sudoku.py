def checkBoard(arr):
    # cek kotak 3x3
    for a in range(3):
        for b in range(3):
            temp = set()
            for c in range(3):
                for d in range(3):
                    num = arr[c+a*3][d+b*3]
                    if num in temp:
                        return False
                    else:
                        temp.add(num)
    # cek baris
    for elem in arr:
        if len(set(list(elem))) != 9:
            return False
    # cek kolom
    for col in range(9):
        temp = set()
        for row in range(9):
            num = arr[row][col]
            if num in temp:
                return False
            else:
                temp.add(num)
    return True

print("Enter numbers:")
lst = []
for _ in range(9):
    lst.append(input().strip())
if checkBoard(lst):
    print("Yes")
else:
    print("No")
    