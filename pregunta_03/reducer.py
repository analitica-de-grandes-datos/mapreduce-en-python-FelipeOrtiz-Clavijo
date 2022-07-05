#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import collections

data_list = dict()

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    second_col, row = line.split('\t')
    
    # convert val to int/float
    try:
        second_col = int(second_col)
    except ValueError as e:
        continue
    
    data_list[second_col] = row

for k, v in collections.OrderedDict(sorted(data_list.items())).items():
    print('%s' %(v), end='')
