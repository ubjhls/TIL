result = [1]
number = 1
n=0
testcase = int(input())
while n<(testcase):
    number = number * 2
    result.append(number)
    n+=1

print(' '.join(map(str,result)))