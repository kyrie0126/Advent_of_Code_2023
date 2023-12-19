with open('day1\day1_input.txt', 'r') as f:
    vals = f.readlines()

# running sum
tot = 0

# numbers
nums = ["0","1","2","3","4","5","6","7","8","9"]

# turn into loop after testing    
for val in vals:

    cur = ""
    for dig in val:
        if dig in nums:
            cur += dig
            break
    for dig in val[::-1]:
        if dig in nums:
            cur += dig
            break

    tot += int(cur)

print(tot)