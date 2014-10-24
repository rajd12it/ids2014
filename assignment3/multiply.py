import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

N = 5

def mapper(record):

    matrix, row, col, value = record   
    if matrix == 'a':
        for n in range(N):
            k = record[1]
            mr.emit_intermediate((k, n),[matrix, col, value])
    else:
        for n in range(N):
            k = record[2]
            mr.emit_intermediate((n, k),[matrix, row, value])
 

def reducer(key, list_of_values):

    a_value= [e for e in list_of_values if e[0] == 'a' ]
    b_value = [e for e in list_of_values if e[0] == 'b']
    result = 0
    for a in a_value:
        for b in b_value:
            if a[1] == b[1] :
                result += a[2] * b[2]
    mr.emit( ( key[0], key[1], result ) )

        
# Do not modify below this line
# =============================

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
