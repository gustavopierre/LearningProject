alter table empresas modify cnpj varchar(14);

insert into empresas
    (nome, cnpj)
VALUES
    ('Bradesco', 79011066000137),
    ('Vale', 33821182000110),
    ('Cielo', 50782243000105);

