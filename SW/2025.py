def all_sum(num):
    if num <= 1:
        return 1
    else:
        return num + all_sum(num-1)

testcase = int(input())
print(all_sum(testcase))