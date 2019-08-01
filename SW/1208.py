for i in range(10):
    testcase = int(input())
    a = list(map(int, input().split()))
    for j in range(testcase):
        max_index = a.index(max(a))
        min_index = a.index(min(a))
        a[max_index] = a[max_index] - 1
        a[min_index] = a[min_index] + 1
        tmp = a[a.index(max(a))]-a[a.index(min(a))]
    print(f'#{i+1} {tmp}')