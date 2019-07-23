def sum(a,b):
    return a + b
   
def sub(a,b):
    return a - b
    
def mul(a, b):
    return a * b
    
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('\'0\'으로 나누려고 하는 경우에는 문자열 \'0으로는 나눌 수 없습니다.\'')