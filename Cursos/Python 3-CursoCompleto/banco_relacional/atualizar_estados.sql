update estados
set nome = 'Maranhão'
where sigla = 'MA';

select est.nome from estados est where sigla = "MA";

select nome, populacao from estados where sigla = 'PR';

update estados
set nome = 'Paraná', populacao = 11.32
where sigla = 'PR';