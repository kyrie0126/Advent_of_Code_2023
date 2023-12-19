import re

with open('day2\day2_input.txt', 'r') as f:
    vals = f.readlines()
    
tot = 0

for val in vals:
    max_blue = max([int(match.group(1)) for match in re.finditer(r'(\d+) blue', val)])
    max_red = max([int(match.group(1)) for match in re.finditer(r'(\d+) red', val)])
    max_green = max([int(match.group(1)) for match in re.finditer(r'(\d+) green', val)])
    power = max_blue * max_red * max_green
    tot += power

print(tot)