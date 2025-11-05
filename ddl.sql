  create table departamento(
    id varchar(6)
    ,ra_professor varchar(15)
    ,nome varchar(30)
    ,primary key (id)
  );

   create table professor(
    ra varchar(15)
    ,nome varchar(30)
    ,id_departamento varchar(6)
    ,primary key (ra)
    ,foreign key (id_departamento) references departamento(id)

  );

  create table curso(
    id varchar(6)
    ,nome varchar(30)
    ,ra_coordenador varchar(15)
    ,primary key (id)
    ,foreign key (ra_coordenador) references professor(ra)
  );

create table aluno(
  ra varchar(15),
  id_curso varchar(6),
  nome varchar(30),
  primary key (ra)
  ,foreign key (id_curso) references curso(id)
  );

  create table disciplina(
  id varchar(6)
  ,nome varchar(50)
  ,id_departamento varchar(6)
  ,id_curso varchar(6)
  ,ra_coordenador varchar(15)
  ,primary key (id)
  ,foreign key (id_departamento) references departamento(id)
  ,foreign key (id_curso) references curso(id)
  ,foreign key (ra_coordenador) references professor(ra) 
);

create table turma(
  id varchar(10)
  ,id_disciplina varchar(6)
  ,semestre varchar(10)
  ,ano varchar(4)
  ,periodo varchar(10)
  ,ra_professor varchar(15)
  ,primary key (id)
  ,foreign key (ra_professor) references professor(ra)
);

create table TCC(
  nome varchar(150)
  ,ra_professor varchar(15)
  ,id varchar(10)
  ,primary key (id)
  ,foreign key (ra_professor) references professor(ra)
);

create table TCC_aluno(
  id_tcc varchar(10)
  ,ra_aluno varchar(15)
  ,foreign key (id_tcc) references TCC(id)
  ,foreign key (ra_aluno) references aluno(ra)
);

create table matriz_curricular(
  id_curso varchar(6)
  ,id_disciplina varchar(6)
  ,foreign key (id_curso) references curso(id)
  ,foreign key (id_disciplina) references disciplina(id)
);

create table historico(
  ra_aluno varchar(15)
  ,id_disciplina varchar(6)
  ,id_turma varchar(10)
  ,nota varchar(10)
  ,foreign key (ra_aluno) references aluno(ra)
  ,foreign key (id_disciplina) references disciplina(id)
  ,foreign key (id_turma) references turma(id)
);

ALTER TABLE matriz_curricular ADD COLUMN semestre varchar;

ALTER TABLE departamento ADD CONSTRAINT ra FOREIGN KEY (ra_professor) REFERENCES professor(ra);
