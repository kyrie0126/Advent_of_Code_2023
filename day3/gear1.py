
import numpy as np

with open("day3\day3_input.txt", "r") as f:
    vals = f.readlines()


# need to modify functionality to identify chunks of numbers, not as individuals
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


def detect_syms(row):
    nums = ("0","1","2","3","4","5","6","7","8","9")
    x = 0
    x_syms = []
    for i in row.strip():
        if i not in nums and i !='.':
            x_syms.append(x)
        x += 1
    return x_syms


# initialize total
total = 0

# first row edge case
cur_nums, cur_valid = detect_nums(vals[0])
cur_sym = detect_syms(vals[0])
after_sym = detect_syms(vals[1])

tot_sym = list(set(cur_sym + after_sym))
for id, num in enumerate(cur_valid):
    if len(np.intersect1d(num, tot_sym)) > 0:
        total += cur_nums[id]

# body
for row in range(1, len(vals)-1):
    row_print = ""
    cur_nums, cur_valid = detect_nums(vals[row])
    before_sym = cur_sym
    cur_sym = after_sym
    after_sym = detect_syms(vals[row+1])
    tot_sym = list(set(before_sym + cur_sym + after_sym))
    
    for id, num in enumerate(cur_valid):
        if len(np.intersect1d(num, tot_sym)) > 0:
            total += cur_nums[id]
    
# last row edge case
cur_nums, cur_valid = detect_nums(vals[-1])
before_sym = detect_syms(vals[-2])
cur_sym = detect_syms(vals[-1])

tot_sym = list(set(before_sym + cur_sym))

for id, num in enumerate(cur_valid):
    if len(np.intersect1d(num, tot_sym)) > 0:
        total += cur_nums[id]

print("total:", total)