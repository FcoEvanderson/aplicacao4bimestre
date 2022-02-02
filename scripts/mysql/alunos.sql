create database Alunos;
use Alunos;
create table alunos(
    nome varchar(30) not null,
    matricula varchar(10) not null,
    PRIMARY KEY(matricula)
);