def longestCommonPrefix(strs):
    strs.sort(key=len)
    val = ""
    y = 0
    z = 1
    for x in strs[0]:
        for z in strs:
            if x == z[y]:
                continue
            else:
                return val
        y+= 1
        val += x

    return val

print(longestCommonPrefix(["flower","flow","flight"]))