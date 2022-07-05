#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import collections

counts = dict()

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    col, val = line.split(',')
    
    # convert count to int/float
    try:
        val = int(val)
    except ValueError as e:
        continue
    
    if col in counts:
        counts[col] += val
    else:
        counts[col] = val

for k, v in collections.OrderedDict(sorted(counts.items())).items():
    print('%s,%d' %(k, v))
