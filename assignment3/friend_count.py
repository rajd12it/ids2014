import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: assigned to person 
    # value: assigned to friend
    key = record[0]
    friend = record[1]
    mr.emit_intermediate(key, friend)

def reducer(key, list_of_values):
    # key: assigned to person
    # list_of_values: list to store all friends
    mr.emit((key, len(list_of_values)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
