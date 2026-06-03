'''
Calculator functions module
'''
M = 100
def add(a:int,b:int, c:int=None, name=None, city=None) -> int:
    '''
    Returns Sum of a,b
    '''
    if name != None:
        print(f"My name is: {name}")

    if c != None:
        return a + b + c
    else:
        return a + b

def sub(a,b):
    return a-b

print(add(2,3))
print(add(45,56, name="Alice"))