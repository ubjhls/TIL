testcase = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(0,len(b)-2):
    count = 0
    if b[i+1]-b[i] > a[0]:
        count = 0
        break
    else:
        if b[i+2]-b[i] <=a[0]:
            b[i] = b[i+2]
            count+=1
        elif b[i+1]-b[i] <= a[0]:
            b[i]=b[i+1]
            count+=1
    print(f'#{i+1} {count}')