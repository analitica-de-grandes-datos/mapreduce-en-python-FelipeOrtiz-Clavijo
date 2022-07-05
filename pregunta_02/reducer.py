#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import collections

max_value = dict()

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    purpose, val = line.split(',')
    
    # convert val to int/float
    try:
        val = int(val)
    except ValueError as e:
        continue
    
    if purpose in max_value:
        if max_value[purpose] >= val:
            continue
        else:
            max_value[purpose] = val
    else:
        max_value[purpose] = val

for k, v in collections.OrderedDict(sorted(max_value.items())).items():
    print('%s\t%d' %(k, v))
