# site_cadastros
 Site que permite cadastros (CRUD) e tals. Desenvolvido para a situação de aprendizagem 5 do curso de ADS do SENAI. Se você é o professor, leia o README que está dentro da pasta de entrega.

----------------------------------------------------------------------------
Olá,

O arquivo backup.sql está disposto dentro da pasta principal do projeto, caso queira importar o banco totalmente configurado diretamente no MySQL. Se você estiver usando configurações padrão no Django, talvez seja necessário ajustar as configurações do banco de dados em "settings" para corresponder à sua conexão. Se houver algum problema de conexão, verifique essa parte.

Para importar, basta seguir estes passos:

Abra o MySQL e vá para "Server" > "Import Data".
Selecione o arquivo backup.sql.
Certifique-se de marcar a opção "self-contained file" durante a importação.
Verifique se o nome do banco de dados no Django corresponde ao nome do banco que está sendo importado.
------------------------------------------------------------------------------------------------------

Se, por algum motivo, o arquivo não funcionar, você pode criar um banco de dados, fazer dele conexão no Django, realizar as migrações e aplicar as migrações dentro do próprio django. Depois disso, insira manualmente os seguintes valores no MySQL:

    INSERT INTO app_cadastro_pessoa (nome, email, nascimento, pais)
     VALUES
         ('Jorge da Silva', 'jorge.silva@email.com', '1980-01-01', 'Estados Unidos'),
         ('Amanda de Sá Campos', 'julia.campos@yahoo.com', '1990-02-02', 'Índia'),
         ('Lucas Alves', 'lucas.bernardi@yahoo.com', '2000-03-03', 'Japão'),
         ('Luis Cesar', 'luis.hryckiv@gmail.com', '1970-04-04', 'Reino Unido'),
         ('Marco Villas', 'marco.villasboas@gmail.com', '1960-05-05', 'Japão'),
         ('Matheus Farias', 'matheus.farias@gmail.com', '2010-06-06', 'Austrália'),
         ('Mickael Hespanhol', 'mickael.hespagnol@yahoo.com', '2005-07-07', 'Austrália'),
         ('Antonieta Jamile', 'otto.becker@valvesoftware.com', '1950-08-08', 'China'),
         ('André Becker', 'otto.becker@valvesoftware.com', '1950-08-08', 'China'),
         ('Rafael', 'rafael.rosso@gmail.com', '1940-09-09', 'Reino Unido'),
         ('Adriano Becker', 'otto.becker@valvesoftware.com', '1950-08-08', 'Índia'),
         ('Akabei dedarocul', 'rafael.rosso@gmail.com', '1940-09-09', 'Japão'),
         ('Marco Antôny Jamaica', 'rafael.rosso@gmail.com', '1940-09-09', 'Reino Unido');
