for i in range(0,5):
    if i != 0:
        print('')
    for j in range(0,5):
        if i==j:
            print('#',end='')
        else:
            print('+',end='')