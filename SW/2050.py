def change(a):
    result = []
    tmp = 0
    for i in range(len(a)):
        tmp = ord(f'{a[i]}')-64
        result.append(tmp)
    return result

testcase = input()
tmp = change(testcase)

for j in range(len(tmp)):
    print(tmp[j], end=' ')