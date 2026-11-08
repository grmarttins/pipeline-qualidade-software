CREATE TABLE IF NOT EXISTS moedas (
    simbolo varchar(10) primary key not null,
    nome_moeda varchar(100) not null,
    tipo_moeda varchar(10) not null,
    dt_criacao timestamptz default CURRENT_TIMESTAMP,
    dt_atualizacao timestamptz 
)