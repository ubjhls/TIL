def madi(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if str(a[i])==str(a[j]) and str(a[i-1])==str(a[j-1]):
                count = i+1
                break
            
    return count

testcase = int(input())

for j in range(testcase):
    a = list(map(str, input().split()))
    print(f'#{j+1} {madi(a)}')