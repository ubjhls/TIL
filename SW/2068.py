def max(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i+1] = a[i]
        else:
            a[i+1] = a[i+1]
    return a[i+1]

testcase = int(input())

for j in range(testcase):
    a = list(map(int, input().split()))
    print(f'#{j+1} {max(a)}')