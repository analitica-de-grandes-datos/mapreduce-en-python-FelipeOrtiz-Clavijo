#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import collections

sum_vals = dict()
cnt_vals = dict()

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    col, val = line.split(',')
    
    # convert count to int/float
    try:
        val = int(val)
    except ValueError as e:
        continue
    
    # calculate sum
    if col in sum_vals:
        sum_vals[col] += val
    else:
        sum_vals[col] = val

    # calculate counts
    if col in cnt_vals:
        cnt_vals[col] += 1
    else:
        cnt_vals[col] = 1

for k, v in collections.OrderedDict(sorted(sum_vals.items())).items():
    print(k, end='\t')
    print('%.1f' % (sum_vals[k]), end='\t')
    print(sum_vals[k]/cnt_vals[k])
