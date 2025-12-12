with open("input.txt") as f:

    pointer = 50
    limit = 99
    password = 0
    for l in f:
        step = l.rstrip()


        direction = step[:1]
        val = int(step[1:])

        print(direction, val)

        if direction == 'L':
            pointer -= val 
            while pointer < 0: 
                pointer += (limit + 1)
        else:
            pointer += val
            while pointer > limit: 
                pointer -= (limit + 1)

        if pointer == 0:
            password += 1

        print(pointer)
    print("password", password)





