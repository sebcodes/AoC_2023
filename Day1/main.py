file1 = open('day1.txt', 'r')
Lines = file1.readlines()

summe = 0

for line in Lines:
    nummers = [int(s) for s in line.strip() if s.isdigit()]
    summe += int(str(nummers[0]) + str(nummers[len(nummers)-1]))

print(summe)


