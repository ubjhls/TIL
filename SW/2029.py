# def calc(num):
#     mok = num[0]//num[1]
#     nameji = num[0]%num[1]
#     return mok, nameji

# testcase = int(input())

# for j in range(testcase):
#     a = list(map(int, input().split()))
#     print(f'#{j+1} {calc(a)}')

def calc(num):
    mok = num[0] // num[1]
    return mok
def calc_2(num):
    nameji = num[0] % num[1]
    return nameji

testcase = int(input())

for j in range(testcase):
    a = list(map(int, input().split()))
    print(f'#{j+1} {calc(a)} {calc_2(a)}')
