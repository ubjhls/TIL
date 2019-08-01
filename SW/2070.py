def val(a):
    if a[0]>a[1]:
        return '>'
    elif a[0]<a[1]:
        return '<'
    else:
        return '='

testcase = int(input())

for j in range(testcase):
    a = list(map(int, input().split()))
    print(f'#{j+1} {val(a)}')