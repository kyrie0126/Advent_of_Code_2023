with open("day5\day5_input.txt", "r") as f:
    groups = f.read().split('\n\n')
    

# organize text file data
seeds = [int(seed) for seed in groups[0].split(':')[1].split()]
seed_to_soil = [[int(i) for i in val.split()] for val in groups[1].split(':')[1].strip().split('\n')]
soil_to_fert = [[int(i) for i in val.split()] for val in groups[2].split(':')[1].strip().split('\n')]
fert_to_water = [[int(i) for i in val.split()] for val in groups[3].split(':')[1].strip().split('\n')]
water_to_light = [[int(i) for i in val.split()] for val in groups[4].split(':')[1].strip().split('\n')]
light_to_temp = [[int(i) for i in val.split()] for val in groups[5].split(':')[1].strip().split('\n')]
temp_to_humid = [[int(i) for i in val.split()] for val in groups[6].split(':')[1].strip().split('\n')]
humid_to_loc = [[int(i) for i in val.split()] for val in groups[7].split(':')[1].strip().split('\n')]


# function to check for and update conversions
def conv_checker(input_vals, conversions):
    temp_out = []
    for i in input_vals:
        missing = True
        for j in conversions:
            if i >= j[1] and i <= j[1]+j[2]:
                val_out = j[0]+i-j[1]
                temp_out.append(val_out)
                missing = False
        if missing:
            temp_out.append(i)
    return temp_out


# iterative conversions
soils = conv_checker(seeds, seed_to_soil)
ferts = conv_checker(soils, soil_to_fert)
waters = conv_checker(ferts, fert_to_water)
lights = conv_checker(waters, water_to_light)
temps = conv_checker(lights, light_to_temp)
humids = conv_checker(temps, temp_to_humid)
locs = conv_checker(humids, humid_to_loc)

# print minimum location
print(min(locs))