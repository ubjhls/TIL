def calc(num):
    result=[]
    for i in range(len(num)):
        if i==3*(i/3):
            result.append('-')
        else:
            result.append(i)
    return result

testcase = int(input())

for j in range(testcase):
    a = list(map(str, input().split()))
    print(f'#{j+1} {calc(a)}')