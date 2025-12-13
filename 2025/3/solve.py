def get_max_voltage(s, n):
    
    max_val = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            max_val = max(max_val, int(s[i] + s[j]))

    return max_val
    


with open("input.txt") as f:

    res = 0
    for l in f:
        
        v = get_max_voltage(l.rstrip(), 12)
        print(v)
        res += v

    print(res)







