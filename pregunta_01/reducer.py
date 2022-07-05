#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import collections

counts = dict()

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    credit_history, cnt = line.split(',')
    
    # convert year and price (currently a string) to int/float
    try:
        cnt = int(cnt)
    except ValueError as e:
        continue
    
    if credit_history in counts:
        counts[credit_history] += cnt
    else:
        counts[credit_history] = cnt

for k, v in collections.OrderedDict(sorted(counts.items())).items():
    print('%s\t%d' %(k, v))
