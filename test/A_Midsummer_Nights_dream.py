import matplotlib.pyplot as plt
import numpy as np
import csv
text = open("william.txt", "r")
counts = dict()

for line in text:
    line = line.strip()

    line = line.lower()

    words = line.split()

    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1


sorted_dict = sorted(counts.items(), key=lambda x: x[1])
converted_dict = dict(sorted_dict)

for key, value in converted_dict.items():

    if value > 40:

        print(key + "," + str(value))


with open('william.csv', 'w') as f:

    for key,value in counts.items():
        if value > 40:
            f.write("%s,%s\n" % (key,str(value)))


