select w.id
from Weather as w
    inner join Weather as w2 on datediff(w.recordDate, w2.recordDate) = 1 and w.temperature > w2.temperature
where not isnull(w2.id);