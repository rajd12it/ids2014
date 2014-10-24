select sum(mul)
from
(select A.value * B.value as mul
from a as A inner join b as B on A.col_num=B.row_num
where A.row_num = 2 and B.col_num=3);
