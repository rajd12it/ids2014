import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: declare as table. table[1]=order id, order table 10 columns, line table 17 columns  
    # value: all records for order id 
    key = record[0]
    orderid = record[1]
    mr.emit_intermediate(orderid, record)

def reducer(key, list_of_values):
    # key: orderid
    # value: all records for key: orderid
    output = {}
    values = []
    result_cnt =  0
    list_length = len(list_of_values)
    # for each item in list, join order table with line 
    for i in range(1, list_length):
         # first record is from order table
         values += list_of_values[0]
         # join to record in line table for i
         values += list_of_values[i]
         # store the joined record
         output[result_cnt] = values
         values = []
         # MapReduce emit the result
         mr.emit(output[result_cnt])
         # loop to next record
         result_cnt += 1

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
