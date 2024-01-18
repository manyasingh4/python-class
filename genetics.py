def PatternCount (Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count + 1
    return count

print(PatternCount("GATCGATACGTAGACGTA", "GAT"))

b = [1,2,3,4,6,7,99,88,999]
max_num = 0
for i in b:
    if i > max_num:
        max_num = i
print(max_num)

# Write a Python program that accepts a list of integers and calculates the length and the fifth
# element. Return true if the length of the list is 8 and the fifth element occurs thrice in the 
# said list.
def pillow(listy):
    a = listy[4]
    c = 0
    for i in listy:
        if i == a:
            c = c + 1
    print(len(listy), a)
    if len(listy) == 8 and c == 3:
        return True
    else:
        return False
    
boah = [6, 4, 7, 3, 3, 6, 3, 6]
print(pillow(boah))