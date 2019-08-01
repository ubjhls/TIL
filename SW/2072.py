def sum(a):
    tmp = 0
    for i in a:
        if i % 2 == 1:
      	    tmp += i
    return tmp
testcase = int(input())

for j in range(testcase):
    a = list(map(int, input().split()))
    print(f'#{j+1} {sum(a)}')