"""
Determine which games would have been possible if the bag had been loaded with only:
    12 red cubes
    13 green cubes
    14 blue cubes
What is the sum of the IDs of those games?
"""

import re

with open('day2\day2_input.txt', 'r') as f:
    vals = f.readlines()
    
tot = 0
possible = []

for val in vals:

    id = int(val.split(':')[0].split(' ')[1])
    scores = val.split(':')[1]
    max_blue = max([int(match.group(1)) for match in re.finditer(r'(\d+) blue', val)])
    max_red = max([int(match.group(1)) for match in re.finditer(r'(\d+) red', val)])
    max_green = max([int(match.group(1)) for match in re.finditer(r'(\d+) green', val)])
    if max_blue <= 14 and max_red <= 12 and max_green <= 13:
        tot += id

print(tot)




