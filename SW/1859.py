def calc(num):
    result=[]
    for i in range(len(num)):
        tmp = i.replace("3", "-", num)
        result.append(tmp)
    return result

testcase = int(input())

for j in range(testcase):
    a = list(map(int, input().split()))
    print(f'#{j+1} {calc(a)}')