def two_are_positive(a, b, c):
    if(a == 0): a = -1
    if(b == 0): b = -1
    if(c == 0): c = -1
    if(a < 0 and b < 0 and c <0):
        return False
    else:
        if((a * b * c) > 0):
            print(False)
            return False 
        else:
            print(True)
            return True
        
two_are_positive(-4, 6, 0)