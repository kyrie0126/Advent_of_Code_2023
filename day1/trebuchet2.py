import re

# different method - written numbers with numerical values
with open('day1\day1_input.txt', 'r') as f:
    vals = f.readlines()

nums = ["0","1","2","3","4","5","6","7","8","9"]

num_patterns = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

def convert_to_number(letters):
    if letters in num_patterns.keys():
        real_num = num_patterns.get(letters)
        return real_num
    else:
        return letters
    
def extract_word_vals(input_val):
    numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', input_val)
    for i in numbers:
        num = convert_to_number(i)
        new_sub = i[0] + num + i[-1]
        input_val = re.sub(i,new_sub,input_val)
    numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', input_val)
    if len(numbers) == 1:
        number = convert_to_number(numbers[0])
        value = int(number + number)
        return value
    else:
        front = convert_to_number(numbers[0])
        back = convert_to_number(numbers[-1])
        value = int(front + back)
        return value

tot = 0
for val in vals:
    tot += extract_word_vals(val)
print(tot)


