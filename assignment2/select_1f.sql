select count(*)
from
(select distinct docid from frequency where term = 'transactions'
INTERSECT
select distinct docid from frequency where term = 'world');
