with open("day4\day4_input.txt", "r") as f:
    rows = f.readlines()
    
total = 0    

for row in rows:
    temp = row.split(':')[1].split('|')
    win_nums = temp[0].strip().split()
    my_nums = temp[1].strip().split()
    
    num_wins = 0
    for num in my_nums:
        if num in win_nums:
            num_wins += 1
            
    if num_wins == 0:
        subtotal = 0
    else:
        subtotal = 2**(num_wins-1)
    
    total += subtotal

print(total)