select count(*)
from
(select docid, count
from frequency 
group by docid
having SUM(count) > 300);
