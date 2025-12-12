from collections import defaultdict

with open('input.txt') as f:

    l = f.read()

    print(l)

    res = 0

    ranges = l.split(",")

    ranges = [each.split('-') for each in ranges]

    ranges = [(int(a), int(b)) for a,b in ranges]

    distinct = set()

    for start, end in ranges:

        for num in range(start, end+1):
            # print(num)
            num = str(num)
            l = len(num)

            for t in range(1,l+1):
                s = defaultdict(int)

                for i in range(0, l, t):
                    s[str(num)[i:i+t]] += 1
                # print(s)
                if len(s) == 1:
                    v = list(s.keys())[0]
                    if s[v] >= 2:
                        distinct.add(int(num))
                        # print("winner", num)
                        # print(s)
                        continue

    res = sum(list(distinct))

    print(res)
        
# 31210613313
# 31210617420
    
# 4174379265
# 4174379265