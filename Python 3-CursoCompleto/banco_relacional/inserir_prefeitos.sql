select * from cidades;

insert into prefeitos
    (nome, cidade_id)
VALUES
    ('Rodrigo Neves', 2),
    ('Raquel Lyra', 3),
    ('Zenaldo Coutinho', null);

insert into prefeitos
    (nome, cidade_id)
VALUES
    ('Rafael Greca', null);

insert into prefeitos
    (nome, cidade_id)
VALUES
    ('Rodrigo Pinheiro', 3);

select * from prefeitos;