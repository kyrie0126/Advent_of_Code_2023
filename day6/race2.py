"""
Two approaches jumped out at me while reading this problem.
1. Binary Search: Search for the minimum Hold that breaks the Distance record. Multiply it by 2 since there are compliments above the median.
2. Quadratic Formula: Since there are compliments (aka symmetry) around the median, a parabola is created. Find intersections with Distance record.

The approaches are identical in goal - find min/max Hold values to break the Distance record without brute force.
I'm more familiar with quadratics than data structures & algorithms, so I chose binary search as a personal growth challenge.
"""

with open("day6\day6_input.txt", "r") as f:
    temp = f.readlines()
    time = int(temp[0].split(':')[1].replace(' ',''))
    distance = int(temp[1].split(':')[1].replace(' ',''))


"""
Approach: Binary Search

We can use binary search to find the first Hold that allows for record distance.

Distance = Hold * (Time - Hold)
Every value below the median will be multiplied by it's compliment above the median.
So, we only need to search the bottom half of the time range.
Then, we can multiply the output by 2 to account for upper half (aka compliments).
Finally, account for duplicates at the median value if time is odd.
"""

# modified setup without defining a list since linear increment between values
def binary_search(time: int, distance: int):
    low, high = 1, time // 2
    mid = (low + high) // 2

    while low <= high:
        mid = (low + high) // 2
        score = mid * (time - mid)
        
        if score == distance:
            return mid
        elif score < distance:
            low = mid + 1
        else:
            high = mid - 1
    
    # if time is odd, account for middle value being duplicated
    if time % 2 == 0:
        return time - (low - 1)*2
    else:
        return time - (low - 1)*2 - 1
    
print(binary_search(time, distance))
