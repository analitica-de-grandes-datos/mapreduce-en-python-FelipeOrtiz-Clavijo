#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import collections

data_list = dict()

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    col3, row = line.split(',')
    
    # convert count to int/float
    try:
        col3 = int(col3)
    except ValueError as e:
        continue

    data_list[col3] = row

cnt=0
for k, v in collections.OrderedDict(sorted(data_list.items())).items():
    if cnt > 5:
        break
    print('%s' %(v), end='')
    cnt += 1
