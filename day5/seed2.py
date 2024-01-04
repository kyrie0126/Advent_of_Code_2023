with open("day5\day5_input.txt", "r") as f:
    groups = f.read().split('\n\n')
    
# logic - move through conversions and create sets of (start, end) outputs for sets of inputs
# comparisons will be min/max based, without brute force iteration

# organize text file data (same as part 1)
seeds = [int(seed) for seed in groups[0].split(':')[1].split()]
seed_to_soil = [[int(i) for i in val.split()] for val in groups[1].split(':')[1].strip().split('\n')]
soil_to_fert = [[int(i) for i in val.split()] for val in groups[2].split(':')[1].strip().split('\n')]
fert_to_water = [[int(i) for i in val.split()] for val in groups[3].split(':')[1].strip().split('\n')]
water_to_light = [[int(i) for i in val.split()] for val in groups[4].split(':')[1].strip().split('\n')]
light_to_temp = [[int(i) for i in val.split()] for val in groups[5].split(':')[1].strip().split('\n')]
temp_to_humid = [[int(i) for i in val.split()] for val in groups[6].split(':')[1].strip().split('\n')]
humid_to_loc = [[int(i) for i in val.split()] for val in groups[7].split(':')[1].strip().split('\n')]

# convert seeds into pairs (start, range)
seed_ranges = [[seeds[i], seeds[i]+seeds[i+1]]for i in range(len(seeds))[::2]]

# check conversions in terms of (start,end) pairings
def conv_checker2(input_vals: list, conversions: list) -> list:
    """
    input_vals: (start, end)
    conversions: (destination, source, range)
    """

    out_vals = []
    
    for i in input_vals:
        input_start = i[0]
        input_end = i[1]

        missing_conv = True
        
        for j in conversions:
                        
            conv_start = j[1]
            conv_end = j[1] + j[2]
            conv_out = j[0]
            conv_range = j[2]
            # case 1:
            # input: [xxx]xxx
            # conv:  xx[xxx]x
            if input_start < conv_start and input_end >= conv_start and input_end <= conv_end:
                out_vals.append([input_start, conv_start - 1])
                extra = input_end - conv_start
                out_vals.append([conv_out, conv_out + extra])
                missing_conv = False
            
            # case 2:
            # input: xx[xxx]x
            # conv:  [xxx]xxx
            elif input_start >= conv_start and input_start <= conv_end and input_end > conv_end:
                extra = conv_end - input_start
                out_vals.append([conv_out + conv_range - extra, conv_out + conv_range])
                out_vals.append([conv_end + 1, input_end])
                missing_conv = False
            
            # case 3:
            # input: xx[xx]xx
            # conv:  x[xxxx]x
            elif input_start >= conv_start and input_end <= conv_end:
                extra_start = input_start - conv_start
                extra_end = conv_end - input_end
                out_vals.append([conv_out + extra_start, conv_out + conv_range - extra_end])
                missing_conv = False
            
            # case 4:
            # input: x[xxxx]x
            # conv:  xx[xx]xx
            elif input_start < conv_start and input_end > conv_end:
                extra_start = conv_start - input_start
                extra_end = input_end - conv_end
                out_vals.append([input_start, conv_start - 1])
                out_vals.append([conv_out, conv_out + conv_range])
                out_vals.append([conv_end + 1, input_end])
                missing_conv = False
        
        if missing_conv:
            out_vals.append([input_start, input_end])

    return out_vals


def overlap_check(input_vals):
    out_vals = []
    nums = sorted(input_vals)
    temp_start = nums[0][0]
    temp_end = int
    for i in range(len(nums)-1):
        if nums[i+1][0] <= nums[i][1]+1:
            continue
        else:
            temp_end = nums[i][1]
            out_vals.append([temp_start, temp_end])
            temp_start = nums[i+1][0]
    out_vals.append([temp_start, nums[-1][1]])        
    return out_vals

# print(seed_ranges, "\n")
soils = overlap_check(conv_checker2(seed_ranges, seed_to_soil))
# print(soils, "\n")
ferts = overlap_check(conv_checker2(soils, soil_to_fert))
# print(ferts, "\n")
waters = overlap_check(conv_checker2(ferts, fert_to_water))
# print(waters, "\n")
lights = overlap_check(conv_checker2(waters, water_to_light))
# print(lights, "\n")
temps = overlap_check(conv_checker2(lights, light_to_temp))
# print(temps, "\n")
humids = overlap_check(conv_checker2(temps, temp_to_humid))
# print(humids, "\n")
locs = overlap_check(conv_checker2(humids, humid_to_loc))
print(sorted(humids))

# print(min(locs)[0])