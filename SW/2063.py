def middle(a):
    tmp = sorted(a)
    tmp = tmp[len(a) // 2]
    return tmp

testcase = list(map(int, input().split()))

print(middle(testcase))