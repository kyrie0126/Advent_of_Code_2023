import numpy as np

with open("day3\day3_input.txt", "r") as f:
    vals = f.readlines()


def detect_nums(row):
    nums = ("0","1","2","3","4","5","6","7","8","9")
    x = []
    x_val = []
    x_valid = []
    x_nums = []
    for i in range(len(row.strip())):
        
        # edge case if last character is a number
        if row[i] in nums and i == max(range(len(row.strip()))):
            x.append(row[i])
            x_val.append(i)
            temp = ""
            for char in x:
                temp += char
            x_nums.append(int(temp))
                        
            x_val.append(max(x_val)+1)
            x_val.insert(0,min(x_val)-1)
            x_valid.append(x_val)
            
            x = []
            x_val = []
        
        # regular case for detecting the start of a number grouping
        elif row[i] in nums:
            x.append(row[i])
            x_val.append(i)
        
        # case for detecting the end of a number grouping
        elif row[i] not in nums and len(x) > 0:
            temp = ""
            for char in x:
                temp += char
            x_nums.append(int(temp))
                        
            x_val.append(max(x_val)+1)
            x_val.insert(0,min(x_val)-1)
            x_valid.append(x_val)
            
            x = []
            x_val = []

    return x_nums, x_valid


def detect_gears(row):
    x = 0
    x_syms = []
    for i in row.strip():
        if i == '*':
            x_syms.append(x)
        x += 1
    return x_syms


# initialize total
total = 0

# iterate through rows and check for pairs of numbers linked to * symbols
for row in range(len(vals)):

    # identify * symbols in current row
    gears = detect_gears(vals[row])
    
    # first row edge case
    if row == 0:
        curr = detect_nums(vals[row])
        after = detect_nums(vals[row+1])
        
        nums = curr[0] + after[0]
        valid = curr[1] + after[1]
    
    # body
    elif row == len(vals)-1:
        before = detect_nums(vals[row-1])
        curr = detect_nums(vals[row])
        
        nums = before[0] + curr[0]
        valid = before[1] + curr[1]
        
    # last row edge case        
    else:
        before = detect_nums(vals[row-1])
        curr = detect_nums(vals[row])
        after = detect_nums(vals[row+1])
        
        nums = before[0] + curr[0] + after[0]
        valid = before[1] + curr[1] + after[1]

    matches = []

    # identify numbers adjacent to * symbols
    for id, val in enumerate(valid):
        intersections = np.intersect1d(val, gears)
        if len(intersections) > 0:
            matches.append((int(intersections), nums[id]))
            
    pair_check_dict = {}
    
    # identify numbers adjacent to * symbols
    for item in matches:
        if item[0] in pair_check_dict:
            pair_check_dict[item[0]].append(item[1])
        else:
            pair_check_dict[item[0]] = [item[1]]

    # if two values are linked to * symbol, multiply the values and add to total
    for nums in pair_check_dict.values():
        if len(nums) == 2:
            temp = 1
            for num in nums:
                temp *= num
            total += temp

print(total)