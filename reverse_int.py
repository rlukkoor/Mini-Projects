def reverse(x):
        if x >= 0:
            x = int(str(x)[::-1])
        else:
            x = -1*int(str(x)[:0:-1])
            
        if -pow(2, 31) <= x <= pow(2, 31) - 1:    
            return x
        else:
            return 0

print(reverse(123))