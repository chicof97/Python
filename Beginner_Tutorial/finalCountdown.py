# logical operators = evaluate multiple conditions (or,and,not)
#                   or = at least one conditions must be TRUE
#                   and = all conditions must be TRUE
#                   not = inverts the condition

# conditional expression = a one-line shortcut for if else statement (ternary operator)
#                          Print/ assign one of two value on a condition
#                           X if condition else Y

# for loops - executes a block of code an exact number of times
#             it's possible to iterate over a range, string, sequence, etc



import time 

countdown_time = 0

while countdown_time <= 0:
    countdown_time= int(input("Enter time in seconds: ") )

for x in range(countdown_time,0,-1):
    seconds = x % 60;
    minutes = int(x / 60 ) % 60
    hours = int(x /3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Your time is up buddy. Hasta la vista")