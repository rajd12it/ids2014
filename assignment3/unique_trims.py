import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence id 
    # value: sequence of nucleotides
    key = record[0]
    sequence = record[1]
    # trim last 10, remove duplicates
    trim = sequence[:-10]
    mr.emit_intermediate(trim, 0)

def reducer(key, list_of_values):
    # key: sequence id
    # list_of_values: trim sequence of nucleotides
    # print all unique keys
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
