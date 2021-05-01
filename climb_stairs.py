def climbStairs(n):
        x = 1
        y = 1
        z = 0
        while z < n - 1:
            x, y = y, x + y
            z += 1
        return y

print(climbStairs(4))