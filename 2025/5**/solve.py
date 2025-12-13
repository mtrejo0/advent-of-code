with open("input.txt") as f:

    ranges = []
    ids = []
    for l in f:
        if l.rstrip() == '':
            break
        a, b = l.rstrip().split('-')
        ranges.append([int(a), int(b)])
        
    
    for l in f:
        ids.append(int(l.rstrip()))

print(ranges)
print(ids)

fresh_count = 0

for id in ids:

    for a, b in ranges:
        if id >= a and id <= b:
            fresh_count += 1
            break
print(fresh_count)


        
    
