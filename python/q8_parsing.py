import math
import csv
f1 = 'football.csv'
difference = []

with open(f1, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        gf = int(row['Goals'])
        ga = int(row['Goals Allowed'])
        difference.append((row['Team'], math.fabs(gf-ga)))

print(sorted(difference, key=lambda x: x[1])[0][0])
  
      
