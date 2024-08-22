# fastapi-async-project
Project to self improvement. Using Fastapi, Postgres, Async SQLAlchemy, Async requests with Aiohttp.


## Frameworks utilizados
### FastAPI
O FastAPI é um framework moderno de alta performace que foi projetado para construção de APIs RESTful de maneira rápida com o mínimo de código possível oferecendo diversas vantagens para o desenvolvimento, como:

- **Validação automática de dados**: O FastAPI utiliza o Pydantic para verificar os dados de entrada assegurando que os dados de entrada estejam no formato esperado.
- **Documentação automática**: Gera automaticamente a documentação da API (Swagger). 

Além de outras vantagens como escalabilidade, suporte nativo a tipagem e suporte a WebSockets e GrapghQL.

### SQLAlchemy
O SQLAlchemy é uma biblioteca em Python que facilita a interação com bancos de dados relacionais, como MySQL, PostgreSQL, SQLite, entre outros. Ele serve como uma ponte entre o código Python e o banco de dados, permitindo que você trabalhe com os dados de forma mais simples e eficiente.

Existem duas principais funcionalidades no SQLAlchemy:

**Core:** É a camada mais próxima do SQL, permitindo que você escreva consultas SQL de forma programática em Python, mas ainda muito próximas do que seria escrever SQL puro.

**ORM (Object-Relational Mapping):** Essa camada permite que você trabalhe com o banco de dados usando objetos Python. Em vez de escrever consultas SQL diretamente, você pode interagir com classes e objetos que representam suas tabelas e linhas no banco de dados. Isso facilita a manipulação dos dados, tornando o código mais limpo e mais fácil de manter.

### Asyncpg

asyncpg é uma biblioteca em Python projetada para acessar bancos de dados PostgreSQL de forma assíncrona. Ela é baseada em corrotinas e usa a biblioteca asyncio do Python para permitir operações de banco de dados que não bloqueiam a execução do código, o que pode melhorar o desempenho de aplicações que precisam realizar muitas operações de E/S (Entrada/Saída) simultaneamente.

### aiohttp

aiohttp é uma biblioteca em Python que facilita a criação de clientes e servidores HTTP de forma assíncrona. Ela é construída sobre a biblioteca asyncio, permitindo que você faça requisições HTTP ou crie APIs e servidores web sem bloquear a execução do código, o que pode melhorar o desempenho de aplicações que lidam com várias conexões simultâneas.

### requests

requests é uma das bibliotecas mais populares e amplamente usadas em Python para fazer requisições HTTP de forma simples e intuitiva. Ela é conhecida por sua facilidade de uso e por fornecer uma API elegante para realizar operações comuns de HTTP, como GET, POST, PUT, DELETE, entre outras.

### psycopg2-binary 
psycopg2-binary é uma versão pré-compilada da biblioteca psycopg2, que é a biblioteca mais popular para conectar aplicações Python a bancos de dados PostgreSQL. Ela permite que você execute consultas SQL, manipule dados e interaja com um banco de dados PostgreSQL de maneira eficiente e direta.

## Melhorias

- Alterar ids para UUID nas tabelas []
- Testar outra modelagem de banco []
- Dockerizar api []

## Dicas

### Pydantic no View e Services
Usar o Pydantic diretamente no serviço pode criar acoplamento entre a lógica de negócios e a lógica de apresentação, tornando o código mais difícil de manter. Se você decidir mudar o formato da resposta da API, teria que ajustar tanto o serviço quanto o endpoint.
Manter os serviços desacoplados dos modelos de saída permite maior flexibilidade. Se você precisar mudar o formato da resposta no futuro, as mudanças ficam limitadas ao endpoint.

### Docker Network
- A string de conexão do banco deve ser alterada para referenciar a DNS interna do docker quando utilizado. 