select  a.id,a.genotype,b.genotype as parent_genotype
from ecoli_data as a , ecoli_data as b
where a.parent_id=b.id and a.genotype&b.genotype=b.genotype
order by a.id asc;