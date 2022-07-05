#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import collections

max_val = dict()
min_val = dict()

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    col, val = line.split(',')
    
    # convert count to int/float
    try:
        val = float(val)
    except ValueError as e:
        continue
    
    # calculate max
    if col in max_val:
        if max_val[col] < val:
            max_val[col] = val
        else:
            continue
    else:
        max_val[col] = val

    # calculate min
    if col in min_val:
        if min_val[col] > val:
            min_val[col] = val
        else:
            continue
    else:
        min_val[col] = val

for k, v in collections.OrderedDict(sorted(max_val.items())).items():
    print('%s\t%.1f\t%.1f' %(k, max_val[k], min_val[k]))
