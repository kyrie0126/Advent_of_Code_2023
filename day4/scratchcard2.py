with open("day4\day4_input.txt", "r") as f:
    rows = f.readlines()
    
    
card_dict = {}    

for row in rows:
    card_num = int(row.split(':')[0].split()[1])
    win_nums = row.split(':')[1].split('|')[0].strip().split()
    my_nums = row.split(':')[1].split('|')[1].strip().split()
    
    card_dict[card_num] = {
        'copies': 1,
        'win_nums': win_nums,
        'my_nums': my_nums
    }

for id, val in card_dict.items():
    num_wins = 0
    for num in val['my_nums']:
        if num in val['win_nums']:
            num_wins += 1
    for i in range(val['copies']):
        for i in range(id + 1, id + num_wins + 1):
            card_dict[i]['copies'] += 1

total = 0
for val in card_dict.values():
    total += val['copies']

print(total)