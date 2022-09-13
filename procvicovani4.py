numbers = (12, 75, 150, 180, 145, 525);
for loop in numbers:
    if loop > 500:
        break
    elif loop > 150:
        continue
    elif loop % 5 == 0:
        print(loop)