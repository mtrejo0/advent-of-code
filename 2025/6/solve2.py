with open("input.txt") as f:

    arr = []
    for l in f:
        line = l[:-1]
        arr.append(line)

    
line_0 = arr[0]
breaks_size = len(line_0.split())
print(breaks_size)
breaks = [0]*(breaks_size-1)
i = 0
for j in range(len(line_0)):
    is_empty_col = True
    for k in range(len(arr)-1):
        is_empty_col = is_empty_col and arr[k][j] == ' '
    if is_empty_col:
        breaks[i] = j
        i += 1



breaks = [-1]+breaks+[len(line_0)+1]
print(breaks)

arr_vals = []

for each in arr:
    print(each+'.')
    arr_val_i = []
    for i in range(len(breaks)-1):
        start = breaks[i] + 1
        end = breaks[i+1]
        # print(end)
        print(each[start:end], start, end)
        arr_val_i += [each[start:end]]
    arr_vals.append(arr_val_i)

for each in arr_vals:
    print(each)
    

    

total = 0
for j in range(len(arr_vals[0])):
    nums = []
    max_sig_fig = 0
    for i in range(len(arr_vals)-1):
        nums.append(arr_vals[i][j])
        max_sig_fig = max(max_sig_fig, len(nums[-1]))
    print(nums)
    print("max_sig_fig",max_sig_fig)


    rep_list = []

    for jj in range(max_sig_fig):

        rep = ''
        for ii in range(len(nums)):
            rep+=nums[ii][jj]
        rep_list.append(rep)
    print(rep_list)



    exp = (arr_vals[len(arr_vals)-1][j].rstrip()).join(rep_list)
    print(exp)
    val = eval(exp)
    print(val)
    total += val
print(total)




        

        
    
