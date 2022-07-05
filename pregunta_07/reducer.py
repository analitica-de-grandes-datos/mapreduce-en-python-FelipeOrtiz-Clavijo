#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import collections

data_list = dict()

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    col1, col3, row = line.split(',')
    
    # convert col3 to a int
    try:
        col3 = int(col3)
    except ValueError as e:
        continue

    data_list[(col1, col3)] = row

for k, v in collections.OrderedDict(sorted(data_list.items())).items():
    print('%s' %(v), end='')
