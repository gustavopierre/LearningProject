select e.nome as Empresa, c.nome as Cidade
from empresas e, empresas_unidades eu, cidades c
where e.id = eu.empresa_id 
and c.id = cidade_id
and sede;
