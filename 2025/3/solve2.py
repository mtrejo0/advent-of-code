# greedy algorithm
def biggest_num(str, n):
    choice_i = 0
    last_idx = -1
    num_choices = [0] * n

    def biggest_num_range():
        idx = last_idx + 1
        print(choice_i, str[last_idx], last_idx,  len(str) - n + choice_i-1)
        for i in range(last_idx + 1, len(str) - n + choice_i + 1):
            if int(str[idx]) < int(str[i]):
                idx = i
        return idx
    
    while choice_i < n:
        i = biggest_num_range()
        num_choices[choice_i] = str[i]
        last_idx = i
        choice_i += 1

    
    return int("".join(num_choices))

    

    


with open("input.txt") as f:

    res = 0
    for l in f:
        
        v = biggest_num(l.rstrip(), 12)
        print(v)
        res += v

    print(res)







