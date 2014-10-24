import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: matrix (a, b)
    # value: i, j, value
    key = record[0]
    # cross product a*b
    if key == 'a':
         # emit a for i, j, value
         mr.emit_intermediate(key, [record[1], record[2], record[3]])
    else:
         # emit b for j, i, value
         mr.emit_intermediate(key, [record[1], record[2], record[3]])

def reducer(key, list_of_values):
    # key: matrix (a, b)
    # list_of_values: values of a for i, j ,value and values of b for j, i, value
    # mr.intermediate: dictionary to store all values from both a and b values stored in seperate dictionaries
    a = {}
    b = {}
    # cross product a*b
    if key == 'a':
         for v in list_of_values:
              a[(v[0], v[1])]=v[2]  
         for r in mr.intermediate['b']:  
              b[(r[0], r[1])]=r[2]
         # store '0' for blanks
         for i in range(0,5):  
              for j in range(0,5):  
                   if (i,j) not in a.keys():  
                        a[(i,j)]=0  
                   if (j,i) not in b.keys():  
                        b[(j,i)]=0
         result=0  
         # Multiply: (a*b)ij = sum(aik * bkj) for k in 0..4  
         for i in range(0,5):  
              for j in range(0,5):  
                   for k in range(0,5):  
                        result+=a[(i,k)]*b[(j,k)]  
                   mr.emit((i,j,result))  
                   result=0

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
