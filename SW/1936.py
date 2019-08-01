def kbb(num):
    if num[0]==3 and num[1]==2:
        return 'A'
    elif num[0]==2 and num[1]==1:
        return 'A'
    elif num[0]== 1 and num[1]==3:
        return 'A'
    elif num[0]==3 and num[1]==1:
        return 'B'
    elif num[0]==2 and num[1]==3:
        return 'B'
    elif num[0]== 1 and num[1]==2:
        return 'B'

testcase = list(map(int, input().split()))
print(kbb(testcase))