#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the record into fields
    fields = line.split('   ')
    print('%s,%s' % (fields[0], 1))
