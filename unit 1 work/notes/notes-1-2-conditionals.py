# Conditionals
# Kate Jiang
# 2/15/2024

# Implement the flowchart from notes
x = 1_000_000
y = -5.7

# If x is less than y, say so
# If x is greater than y, say so
#If x is equal to y, say so

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
    
foo = int(input("Enter a number: "))  # string
if foo < -1 or foo == 0:
    print("Foo is less than 1")
    print("or it's equal to zero.")

# Check if foo is inside a range
# Greater than one and less than 1000

if foo > 1 and foo < 1000:
    print("Foo is in the range 2 - 999")
else:
    print("Foo is outside the range 2 - 999")