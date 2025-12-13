with open("input.txt") as f:

    ranges = []
    ids = []
    for l in f:
        if l.rstrip() == '':
            break
        a, b = l.rstrip().split('-')
        ranges.append([int(a), int(b)])
    

for r in ranges:
    print(r)

"""
naive 
go through all ids and add them to a set
then return the length of the set

"""
def naive():
    s = set()

    for a, b in ranges:
        print(a, b)
        for i in range(a, b+1):
            s.add(i)
    return len(s)

"""
improved

try to reconcile the ranges

a, b
b, c
=> a, c

i compare to  j

if combine, update j to be 0, 0
update i to be a, c



"""

def improved():

    ranges.sort()
    for i in range(len(ranges)):
        for j in range(len(ranges)):
            # input()
            if i == j:
                # dont compare the same ranges
                continue
            if ranges[i] == [0,0] or ranges[j] == [0,0]:
                # placeholders
                continue
            # print(ranges[i], ranges[j])

            a, b = ranges[i]
            c, d = ranges[j]

            merged_min = None
            merged_max = None

            if c <= a <= d:
                merged_min = c
            if a <= c <= b:
                merged_min = a
            
            if c <= b <= d:
                merged_max = d
            if a <= d <= b:
                merged_max = b
            

            if merged_max is not None and merged_min is not None:
                ranges[j] = [0,0]
                ranges[i] = [merged_min, merged_max]
                print('merge', [merged_min, merged_max])
                

    ranges.sort()
   

    total_ids = 0
    for a, b in ranges:
        print(a, b)
        if [a, b] != [0, 0]:
            print(b-a+1)
            total_ids += (b-a+1)
    return total_ids

print(improved())


# 342437184136857
