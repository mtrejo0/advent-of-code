with open("input.txt") as f:

    arr = []
    for l in f:
        line = l.rstrip()
        print(line.split())
        arr.append(line.split())
    

total = 0
for j in range(len(arr[0])):
    nums = []
    for i in range(len(arr)-1):

        nums.append(arr[i][j])
    print(nums)

    exp = arr[len(arr)-1][j].join(nums)
    print(exp)
    val = eval(exp)
    print(val)
    total += val
print(total)




        

        
    
