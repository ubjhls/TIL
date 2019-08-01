def sum(a):
    tmp = 0
    for i in range(len(a)):
        tmp += a[i]
    return tmp

testcase = list(map(int, list(input())))

print(sum(testcase))