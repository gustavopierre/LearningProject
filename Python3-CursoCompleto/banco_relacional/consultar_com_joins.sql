select * from prefeitos;
select * from cidades;
SELECT * FROM cidades c inner join prefeitos p on c.id = p.cidade_id;
SELECT * FROM cidades c left join prefeitos p on c.id = p.cidade_id;
SELECT * FROM cidades c left outer join prefeitos p on c.id = p.cidade_id;
SELECT * FROM prefeitos p left join cidades c on c.id = p.cidade_id;
SELECT * FROM cidades c right join prefeitos p on c.id = p.cidade_id;
-- SELECT * FROM cidades c full join prefeitos p on c.id = p.cidade_id;
SELECT * FROM cidades c left join prefeitos p on c.id = p.cidade_id
union
SELECT * FROM cidades c right join prefeitos p on c.id = p.cidade_id;