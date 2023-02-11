total = 0
tickets = int(input('Enter please amount of tickets\n'))
for i in range(tickets):
    age = int(input('Enter please age of each visitor\n'))
    if age < 18:
        continue
    elif 18 <= age <= 25:
        total += 990
    else:
        total += 1390
if tickets > 3:
    print('Your total is', (total * 0.9))
else:
    print('Your total is', total)