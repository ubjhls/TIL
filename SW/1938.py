def calc(num):
    sum = num[0]+num[1]
    sub = num[0]-num[1]
    mul = num[0]*num[1]
    div = num[0]//num[1]

    return sum, sub, mul, div


testcase = list(map(int, input().split()))
for i in range(4):

    print(calc(testcase)[i])