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
    # mr.intermediate: dictionary to store all person-friends
    # for each friend
    for v in list_of_values:
    # person has no friend - asymmetric
         if v not in mr.intermediate.keys():
              mr.emit((key, v))
              mr.emit((v, key))
         else:
              # no person - asymmetric
              if key not in mr.intermediate[v]:
                    mr.emit((key, v))
                    mr.emit((v, key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
