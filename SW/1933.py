def oss(num):
    result = []
    for i in range(num):
        if num % (i+1) == 0:
            result.append(i+1)
    return result

testcase = int(input())

print(' '.join(map(str,oss(testcase))))
