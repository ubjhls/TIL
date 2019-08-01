def password(num):
    result = num[0]-num[1]
    return result+1


testcase = list(map(int, input().split()))
print(password(testcase))