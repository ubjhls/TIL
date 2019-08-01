def average(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return round(sum/len(a)) 

testcase = int(input())

for j in range(testcase):
    a = list(map(int, input().split()))
    print(f'#{j+1} {average(a)}')