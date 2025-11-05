import csv



from faker import Faker
from faker.providers import DynamicProvider
from random import randint

fake = Faker('pt_BR')
departamentos = DynamicProvider(
    provider_name = "departamento_provider", elements = ["matematica", "computaçao", "civil", "eletrica", "fisica", "producao", "ciencias sociais", "quimica"]
)
#8
cursos = DynamicProvider(
    provider_name = "curso_provider", elements = ["Eng. Eletrica","Eng. Mecanica", "Eng. Quimica", "Administração", "Eng. Automação", "Eng. de Materiais", "Eng. Robos", "Ciencia da Computação", "Ciencia de Dados", "Eng. de Produção"]
)
#10
disciplinas = DynamicProvider(
    provider_name = "disciplina_provider", elements = ["Cálculo I", "Cálculo II", "Cálculo III", "Álgebra Linear", "Geometria Analítica",
        "Física I", "Física II", "Física III", "Química Geral", "Mecânica dos Sólidos",
        "Resistência dos Materiais", "Mecânica dos Fluidos", "Termodinâmica", "Eletromagnetismo",
        "Circuitos Elétricos", "Eletrônica", "Processos de Fabricação", "Engenharia de Materiais",
        "Sistemas Dinâmicos", "Controle e Automação", "Hidráulica", "Pneumática",
        "Gestão de Projetos", "Segurança do Trabalho", "Desenho Técnico", "Ciência dos Materiais",
        "Algoritmos e Estruturas de Dados", "Programação Orientada a Objetos", "Banco de Dados",
        "Sistemas Operacionais", "Redes de Computadores", "Compiladores", "Engenharia de Software",
        "Inteligência Artificial", "Aprendizado de Máquina", "Visão Computacional",
        "Criptografia e Segurança", "Computação Gráfica", "Arquitetura de Computadores",
        "Teoria da Computação", "Matemática Discreta", "Computação em Nuvem",
        "Desenvolvimento Web", "Computação Móvel", "Big Data", "Sistemas Distribuídos",
        "Métodos Numéricos", "Equações Diferenciais Ordinárias", "Equações Diferenciais Parciais",
    "Cálculo Numérico", "Física Moderna", "Física Quântica para Engenharia",
    "Estatística e Probabilidade", "Análise Real", "Análise Complexa",
    "Instrumentação e Medidas", "Dinâmica de Sistemas Mecânicos", "Elementos de Máquinas",
    "Transferência de Calor", "Sistemas Térmicos", "Projeto Mecânico",
    "Máquinas Hidráulicas", "Eficiência Energética", "Engenharia Econômica",
    "Engenharia de Produção", "Engenharia de Controle", "Robótica Industrial",
    "Manutenção Industrial", "Engenharia de Requisitos", "Testes de Software",
    "Desenvolvimento de Aplicativos", "Interface Humano-Computador (IHC)",
    "Sistemas Embarcados", "Computação Quântica", "Computação Paralela", "Engenharia de Dados",
    "DevOps", "Análise de Dados", "Deep Learning", "Processamento de Linguagem Natural (PLN)",
    "Blockchain e Aplicações", "Internet das Coisas (IoT)", "Segurança Cibernética",
    "Empreendedorismo e Inovação", "Ética Profissional e Engenharia", "Comunicação Científica",
    "Design Thinking", "Sustentabilidade e Meio Ambiente", "Liderança e Trabalho em Equipe",
    "Propriedade Intelectual", "Metodologia Científica", "Projetos Interdisciplinares"]
)

periodos = DynamicProvider(
    provider_name = "periodo_provider", elements = ["diurno" ,"vespertino", "noturno"]
)

semestres = DynamicProvider(
    provider_name = "semestre_provider", elements = ["1º","2º"]
)

tccs = DynamicProvider(
    provider_name = "tcc_provider", elements = ["Análise e Otimização de Processos Industriais com Inteligência Artificial",
        "Desenvolvimento de Materiais Sustentáveis para Construção Civil",
        "Aplicação da Internet das Coisas (IoT) em Sistemas de Automação Residencial",
        "Modelagem Computacional de Estruturas para Prevenção de Colapsos",
        "Estudo de Energias Renováveis: Viabilidade de Painéis Solares em Ambientes Urbanos",
        "Impacto da Impressão 3D na Engenharia de Produção",
        "Desenvolvimento de um Veículo Elétrico de Baixo Custo para Mobilidade Urbana",
        "Aplicação da Engenharia de Materiais na Indústria Aeroespacial",
        "Sistemas de Gestão de Manutenção Preditiva com Aprendizado de Máquina",
        "Desenvolvimento de um Sistema Inteligente para Monitoramento de Barragens",
        "Desenvolvimento de um Algoritmo de Machine Learning para Diagnóstico Médico",
        "Análise de Segurança Cibernética em Aplicações Web",
        "Desenvolvimento de um Assistente Virtual Baseado em Processamento de Linguagem Natural",
        "Blockchain: Aplicações Além das Criptomoedas",
        "Criação de um Sistema de Recomendação Usando Redes Neurais",
        "Automação de Testes de Software com Inteligência Artificial",
        "Desenvolvimento de um Jogo Educacional para Ensino de Programação",
        "Uso de Visão Computacional para Identificação de Placas de Trânsito",
        "Desenvolvimento de um Chatbot para Atendimento ao Cliente",
        "Computação Quântica: Algoritmos e Perspectivas Futuras"]
)

fake.add_provider(tccs)
fake.add_provider(departamentos)
fake.add_provider(cursos)
fake.add_provider(disciplinas)
fake.add_provider(periodos)
fake.add_provider(semestres)

def gerarDepartamento(n):
    deptos = []
    nomes = []
    ids = []
    for i in range(n):
        aux = 1
        aux1 = 1 
        nome = fake.departamento_provider()
        while aux == 1:
            if nome in nomes:
                nome = fake.departamento_provider()
            else:
                aux = 0
        cod = fake.numerify(text='DE-%%%')

        while aux1 == 1:
            if cod in ids:
                cod = fake.numerify(text='DE-%%%')
            else:
                aux1 = 0
        depart = {"id": cod, "nome": nome, "ra_coordenador": None}
        nomes.append(nome)
        ids.append(cod)
        deptos.append(depart)
    return deptos

def gerarProfessor(n):
    profs = []
    ras = []
    nomes = []
    for i in range(n):
        aux = 1
        aux1 = 1
        ra = fake.numerify(text='12.%%%.%%%-%')
        while aux == 1:
            if ra in ras:
                ra = fake.numerify(text='12.%%%.%%%-%')
            else:
                aux = 0
        
        n1 = fake.first_name()
        n2 = fake.last_name()
        nome = n1 + " " + n2
        while aux1 == 1:
            if nome in nomes:
                nome = fake.name()
            else:
                aux1 = 0
        prof = {"ra": ra, "nome": nome, "id_departamento": None}
        nomes.append(nome)
        ras.append(ra)
        profs.append(prof)
    return profs

def gerarCurso(n):
    cursos = []
    ids = []
    nomes = []
    for i in range(n):
        aux = 1
        aux1 =  1
        nome = fake.curso_provider()
        while aux1 == 1:
            if nome in nomes:
                nome = fake.curso_provider()
            else:
                aux1 = 0
        if "Eng" in nome:
            p = "ENG"
        elif "Ciencia" in nome:
            p = "C"
        else:
            p = "ADM"
        id = fake.numerify(text= p +'-%')
        while aux == 1:
            if id in ids:
                id = fake.numerify(text= p +'-%')
            else:
                aux = 0
        nomes.append(nome)
        ids.append(id)
        curs = {"id": id, "nome": nome, "ra_coordenador": None}
        cursos.append(curs)
    return cursos
        
def gerarAlunos(n):
    alunos = []
    ras = []
    nomes = []
    for i in range(n):
        aux = 1
        aux1 = 1
        ra = fake.numerify(text='24.%%%.%%%-%')
        while aux == 1:
            if ra in ras:
                ra = fake.numerify(text='24.%%%.%%%-%')
            else:
                aux = 0
        
        n1 = fake.first_name()
        n2 = fake.last_name()
        nome = n1 + " " + n2
        while aux1 == 1:
            if nome in nomes:
                nome = fake.name()
            else:
                aux1 = 0
        aluno = {"ra": ra,"id_curso": None, "nome": nome}
        nomes.append(nome)
        ras.append(ra)
        alunos.append(aluno)
    return alunos

def gerarDisciplina(n):
    discips = []
    nomes = []
    ids = []
    for i in range(n):
        aux = 1
        aux1 =  1
        id = fake.numerify(text='MT-%%%')
        while aux == 1:
            if id in ids:
                id = fake.numerify(text='MT-%%%')
            else:
                aux = 0
        nome = fake.disciplina_provider()
        while aux1 == 1:
            if nome in nomes:
                nome = fake.disciplina_provider()
            else:
                aux1 = 0
        nomes.append(nome)
        ids.append(id)
        discip = {"id": id, "nome": nome, "id_departamento": None, "id_curso": None, "ra_coordenador": None}
        discips.append(discip)
    return discips

def gerarTurma(n):
    turs = []
    ids = []
    for i in range(n):
        aux = 1
        periodo = fake.periodo_provider()
        if periodo == "noturno":
            p = "NO"
        elif periodo == "vespertino":
            p = "VE"
        else:
            p = "DI"
        id = fake.numerify(text= p + '-%%%')
        while aux == 1:
            if id in ids:
                id = fake.numerify(text= p + '-%%%')
            else:
                aux = 0
        ano = randint(2015,2025)
        semestre = fake.semestre_provider()
        ids.append(id)
        turm = {"id": id, "id_disciplina": None, "semestre": str(semestre), "ano": str(ano), "periodo": periodo, "ra_professor": None}
        turs.append(turm)
    return turs

def gerarMatrizCurricular(curso,disciplina, semestre):
    matri_cur = {"id_curso": curso, "id_disciplina": disciplina, "semestre": semestre}
    return matri_cur

def gerarHistorico(aluno,disc,turma,nota):
    hist = {"ra_aluno": aluno, "id_disciplina": disc, "id_turma": turma, "nota": nota}
    return hist

def gerarTCC(n):
    tccs = []
    ids = []
    nomes = []
    for i in range(n):
        aux = 1
        aux1 = 1
        id = fake.numerify(text='TCC-%%%%')
        while aux == 1:
            if id in ids:
                id = fake.numerify(text='TCC-%%%%')
            else:
                aux = 0
        
        nome = fake.tcc_provider()
        while aux1 == 1:
            if nome in nomes:
                nome = fake.tcc_provider()
            else:
                aux1 = 0
        tc_c = {"id": id, "nome": nome, "ra_professor": None}
        nomes.append(nome)
        ids.append(id)
        tccs.append(tc_c)
    return tccs

def gerarTCC_aluno(tcc,aluno):
    tcc_alun = {"id_tcc": tcc, "ra_aluno": aluno}
    return tcc_alun

import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Connect to the database
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    ) #dados para conseguir conectar com o banco de dados (usar arquivo .env)
    print("Connection successful!")
    
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    # Example query
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)
    def inserção(dicionario, tabela): #função para inserção de dados no banco de dados. Virou função para ter mais reusabilidade sem sujar o código inteiro. TEM QUE ESTAR DEPOIS DA CONEXÃO COM O BANCO. 
        """
        Inserção dos dados vindos de um dicionário para dentro do banco de dados.

        Args:
            dicionario(string): dicionario do qual serão retiradas as informações para inserir no banco de dados
            tabela(string): nome da coluna da tabela do banco de dados na qual serão inseridos os dados do dicionário 

        Returns:
        nada kkkkkkk
        """
        tabelaNome = tabela #tabela na qual as informações serão inseridas
        query = "INSERT INTO " + tabelaNome + "("  #começo da query
        query1 = "" #query com todas as colunas
        query2 = "" #query com todos os valores que serão inseridos
        for chave, valor in dicionario.items(): #navegar pelo dicionario para adicionar os nomes e valores à query
            query1+=   chave + "," #string das colunas exemplo: nome,id,departamento,RA,
            query2+= "'" + valor + "'" + "," #string dos valores | exemplo: jeremias,1234,robotica,24.123.035-8
        query1 = query1.rstrip(",") # tira a última vírgula da string | exemplo: ANTES: nome,id,departamento,RA,  DEPOIS: nome,id,departamento,RA
        query2 = query2.rstrip(",") #mesma coisa do comentário acima(linha 48)

        print(query1) #imprimir cada parte da query para ver como está 
        print(query2)
        query+= query1 + ") VALUES ("  #final da parte INSERT INTO tabela(coluna1,coluna2,coluna3) e começo da inserção dos valores
        query+= query2 + ")" #inserção dos valores na query e fechamento de parenteses do VALUES()
        print(query) #imprimir query completa para checar

    

        cursor.execute(query) #execução da query para inserir no banco de dados 
        cursor.execute("commit") # confirmação da alteração no banco de dados 
    def update(dicionario):
        query = "UPDATE departamento SET ra_professor = '" + dicionario["ra_coordenador"] + "' WHERE id = '" + dicionario["id"] + "'"
        cursor.execute(query)
        cursor.execute("commit")
    def resetarDB():
        cursor.execute('ALTER TABLE departamento DROP CONSTRAINT IF EXISTS ra;')
        tabelas = [
        'historico',
        'matriz_curricular',
        'tcc_aluno',
        'tcc',
        'turma',
        'disciplina',
        'aluno',
        'curso',
        'professor',
        'departamento'
        ]
        for tabela in tabelas:
            cursor.execute(f'DROP TABLE IF EXISTS {tabela} CASCADE;')
        cursor.execute("commit")
    def criarDB():
        cursor.execute("""
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

        ALTER TABLE matriz_curricular
        ADD COLUMN semestre varchar;

        ALTER TABLE departamento
        ADD CONSTRAINT ra FOREIGN KEY (ra_professor)
        REFERENCES professor(ra);
        """)
        cursor.execute("commit")


    #Main
    resetarDB()
    criarDB()
    n = randint(3,8)
    #gera o numero de departamentos e professores
    l_aux = []
    depart = gerarDepartamento(n)
    aux = []
    for i in range(len(depart)):
        depar = {"id": depart[i]["id"], "nome": depart[i]["nome"]}
        aux.append(depar)

    for x in aux:
        inserção(x,"departamento")

    professores = gerarProfessor(2*n + 10)
    #relação professor - departamento
    for i in range(len(professores)):
        r = randint(0,len(depart)-1)
        professores[i]["id_departamento"] = depart[r]["id"]

    for l in professores:
        inserção(l, "professor")


    #relação departamento - professor
    for i in range(len(depart)):
        lpro = []
        for j in range(len(professores)):
            if professores[j]["id_departamento"] == depart[i]["id"]:
                lpro.append(professores[j]["ra"])
        r = randint(0, len(lpro)-1)
        coord_dep = lpro[r]
        depart[i]["ra_coordenador"] = coord_dep

    for i in depart:
        update(i)


    #Criação de cursos
    cursos = gerarCurso(randint(4,10))
    #Relaçao curso e professor
    for i in range(len(cursos)):
        aux = 1
        r = randint(0,len(professores)-1)
        coord_cu = professores[r]["ra"]
        while aux == 1:
            if coord_cu in l_aux:
                r = randint(0,len(professores)-1)
                coord_cu = professores[r]["ra"]
            else:
                aux = 0
        cursos[i]["ra_coordenador"] = coord_cu
        l_aux.append(coord_cu)
    l_aux.clear()



    #criação do aluno
    alunos = gerarAlunos(len(professores)*3)
    #Relação aluno e curso
    for i in range(len(alunos)):
        if i < len(cursos):
            alunos[i]["id_curso"] = cursos[i]["id"]
        else:
            r = randint(0,len(cursos)-1)
            alunos[i]["id_curso"] = cursos[r]["id"]


    #Criar as disciplinas
    disciplinas = gerarDisciplina(4*len(cursos))

    #Relações das disciplinas - curso
    for i in range(len(disciplinas)):
        #relação com o departamento
        if i < len(depart):
            disciplinas[i]["id_departamento"] = depart[i]["id"]
        else:
            r = randint(0,len(depart)-1)
            disciplinas[i]["id_departamento"] = depart[r]["id"]
        #relação com o professor
        for j in range(len(professores)):
            if professores[j]["id_departamento"] == disciplinas[i]["id_departamento"]:
                l_aux.append(professores[j]["ra"])
        r2 =  randint(0,len(l_aux)-1)
        disciplinas[i]["ra_coordenador"] = l_aux[r2]
        l_aux.clear()



    #Criação matriz
    matrizes = []
    for i in range(len(cursos)):
        curso = cursos[i]["id"]
        for j in range(randint(15, 20)):
            r = randint(0, len(disciplinas) - 1)
            disciplina = disciplinas[r]["id"]
            #vendo se ja tem essa disciplina nesse curso
            aux = 0
            while aux == 0:
                if disciplina in l_aux:
                    r = randint(0, len(disciplinas) - 1)
                    disciplina = disciplinas[r]["id"]
                else:
                    aux = 1
            l_aux.append(disciplina)
            matrizes.append(gerarMatrizCurricular(curso,disciplina,randint(1,4)))
            disciplinas[r]["id_curso"] = curso
        l_aux.clear()


    matrizes2 = []
    for i in range(len(matrizes)):
        matri_cur = {"id_curso": matrizes[i]["id_curso"], "id_disciplina": matrizes[i]["id_disciplina"], "semestre": str(matrizes[i]["semestre"])}

        matrizes2.append(matri_cur)



    #Criação da turma
    turmas = gerarTurma(len(disciplinas)*2)
    #relações de turma
    for i in range(len(turmas)):
        #relação turma e disciplina
        if i < len(disciplinas):
            turmas[i]["id_disciplina"] = disciplinas[i]["id"]
        else:
            r = randint(0,len(disciplinas)-1)
            turmas[i]["id_disciplina"] = disciplinas[r]["id"]
        #relação turma e professor
        if i < len(professores):
            turmas[i]["ra_professor"] = professores[i]["ra"]
        else:
            r = randint(0,len(professores)-1)
            turmas[i]["ra_professor"] = professores[r]["ra"]
        


    #Criação históricos
    historicos = []
    # Relações histórico e tcc 
    nAlunosTcc = 0
    alunTcc = []
    for i in range(len(alunos)):
        curso = alunos[i]["id_curso"]
        al_semestre = randint(1,4)
        for j in range(len(matrizes)):
            if matrizes[j]["id_curso"] == curso:
                semestre = matrizes[j]["semestre"]
                if al_semestre <= semestre:
                    
                    #print(turmas)
                    for k in range(len(turmas)):
                        
                        if turmas[k]["id_disciplina"] == matrizes[j]["id_disciplina"]:
                            
                            l_aux.append(turmas[k]["id"]) 
                    r = randint(0,len(l_aux)-1)
                    
                    historicos.append(gerarHistorico(alunos[i]["ra"],matrizes[j]["id_disciplina"],l_aux[r],randint(0,10)))
                    
                    l_aux.clear()
        if al_semestre == 4:
            nAlunosTcc += 1  
            alunTcc.append(alunos[i]["ra"])
    #print(turmas)
    print("\n")
    #Reprovação
    rep = []
    teste = []
    for i in range(len(historicos)):
        if historicos[i]["nota"] < 5:
            turma_atual = {}
            for j in range(len(turmas)):
                if historicos[i]["id_turma"] == turmas[j]["id"]:
                    turma_atual = turmas[j].copy()
            aux = turma_atual["id"]
            id_aux = aux[3] + aux[4] + aux[5]  
            id_tu = "DP-" + id_aux
            
            if turma_atual["semestre"] == "1º":
                turma_atual["semestre"] = "2º"
            else:
                turma_atual["semestre"] = "1º"
                turma_atual["ano"] = str(int(turma_atual["ano"]) + 1)
            nota_nova = randint(5,10)
            turma_atual["id"] = id_tu
            cp = {"ra_aluno": historicos[i]["ra_aluno"], "id_disciplina": historicos[i]["id_disciplina"], "id_turma": turma_atual["id"], "nota": nota_nova}
            teste.append(turma_atual)
            historicos.append(cp)

    #for i in range(len(teste)):
    #   print(teste[i]["id"])

    #limpar a teste -> que tem dicionarios de turmas de DP, mas com repetição
    vistos =[]
    teste_final = []
    for turma in teste:
        if turma["id"] not in vistos:
            vistos.append(turma["id"])
            teste_final.append(turma)

    #print("Apos limpa")
    #for i in range(len(teste_final)):
    #    print(teste_final[i]["id"])

    #Adição das turmas de dp a lista de turmas principal
    for i in range(len(teste_final)):
        turmas.append(teste_final[i])

    #for i in range(len(turmas)):
    #    print(turmas[i]["id"])

    historicos2 = []
    for i in range(len(historicos)):
        nota = str(historicos[i]["nota"])
        hist = {"ra_aluno": historicos[i]["ra_aluno"], "id_disciplina": historicos[i]["id_disciplina"], "id_turma": historicos[i]["id_turma"], "nota": nota}
        historicos2.append(hist)
    #print(turmas)

    #TCC 
    nTccs = int(nAlunosTcc/3)
    tccs = gerarTCC(nTccs) 
    for i in range(len(tccs)):
        r = randint(0,len(professores)-1)
        coordenador = professores[r]["ra"]
        aux = 0
        while aux == 0:
            if coordenador in l_aux:
                r = randint(0,len(professores)-1)
                coordenador = professores[r]["ra"]
            else:
                aux = 1
        
        tccs[i]["ra_professor"] = coordenador
    l_aux.clear()

    #criação do TCC_aluno
    tccs_aluno = []
    for i in range(len(tccs)):
        id_t = tccs[i]["id"]
        for j in range(randint(1,3)):
            r = randint(0,len(alunTcc)-1)
            aluno = alunTcc[r]
            tccs_aluno.append(gerarTCC_aluno(id_t,aluno))
            del alunTcc[r]
    if len(alunTcc) != 0:
        for i in range(len(alunTcc)):
            r = randint(0,len(tccs)-1)
            tccs_aluno.append(gerarTCC_aluno(tccs[r]["id"],alunTcc[i]))


    
    #Conexões -> curso aluno disciplina turma matriz historicos tcc tcc-aluno
    for i in cursos:
        inserção(i,"curso")
    for i in alunos:
        inserção(i,"aluno")
    for i in disciplinas:
        inserção(i,"disciplina")
    for i in turmas:
        inserção(i,"turma")
    for i in matrizes2:
        inserção(i,"matriz_curricular")
    for i in historicos2:
        inserção(i, "historico")
    for i in tccs:
        inserção(i,"tcc")
    for i in tccs_aluno:
        inserção(i,"tcc_aluno")
    #inserção(dictionary,"instructor")
    # Close the cursor and connection
    cursor.close() #sem cursor
    connection.close() #fim da conexão com o banco de dados 
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")
