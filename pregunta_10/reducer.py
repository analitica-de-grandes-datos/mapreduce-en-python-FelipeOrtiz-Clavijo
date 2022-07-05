#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import collections

data_list = dict()

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    letters, idx = line.split('\t')

    # convert letters to a list
    try:
        letters_list = [letter.strip() for letter in letters.split(',')]
        idx = int(idx)
    except ValueError as e:
        continue

    for letter in letters_list:
        if letter in data_list.keys():
            vals = data_list[letter]
            vals.append(idx)
            data_list[letter] = vals
        else:
            data_list[letter] = [idx]
#print(data_list)

for k, v in collections.OrderedDict(sorted(data_list.items())).items():
    index_list = ','.join(str(x) for x in sorted(v))
    print('%s\t%s' %(k, index_list))
