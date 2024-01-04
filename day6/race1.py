with open("day6\day6_input.txt", "r") as f:
    races = f.read().strip().split('\n')
    

time = [int(i) for i in races[0].strip().split(':')[1].split()]
distance = [int(i) for i in races[1].strip().split(':')[1].split()]

inputs = []

for i in range(len(time)):
    inputs.append((time[i],distance[i]))

test = time[0], distance[0]

out = []

for val in inputs: 
    temp = 0
    for i in range(val[0]):
        if i * (val[0] - i) > val[1]:
            temp += 1
    out.append(temp)
    temp = 0

tot = 1
for i in out:
    tot *= i

print(tot)