dictionary_addresses = dict()  # Initialize variables
lst = list()

#fhand = open('mbox-short.txt')

import urllib.request

for line in urllib.request.urlopen('http://www.py4inf.com/code/mbox-short.txt'):
    words = line.split()

    if len(words) < 2 or words[0] != b'From':
        continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1  # First entry
        else:
            dictionary_addresses[words[1]] += 1      # Additional counts

for key, val in list(dictionary_addresses.items()):
    lst.append((val, key))  # Fills list with value, key of dict

lst.sort(reverse=True)  # Sorts by highest value

for count, email in lst[:1]:  # Only displays the largest value
    print(email, count)
