def plusOne(digits):
        x = int("".join(map(str,digits)))+1
        return [int(y) for y in str(x)]

print(plusOne([1,2,3]))
