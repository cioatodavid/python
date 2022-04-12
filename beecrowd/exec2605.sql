SELECT p.name, f.name
FROM products p INNER JOIN providers f ON
     p.id_providers	= f.id
WHERE p.id_categories = 6

selec p.name, f.name from products p inner join providers f on p.id_providers = f.id 
where p.id_categories = 6