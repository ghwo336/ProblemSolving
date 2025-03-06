SELECT COUNT(*) AS count
FROM ecoli_data AS e
WHERE (e.genotype&2!=2) and (e.genotype&4=4 or e.genotype&1=1)