CREATE TABLE IF NOT EXISTS moedas (
    simbolo varchar(10) primary key not null,
    nome_moeda varchar(100) not null,
    tipo_moeda varchar(10) not null,
    data_inclusao timestamp default current_timestamp
)