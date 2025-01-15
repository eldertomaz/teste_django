# Projeto Django REST API

## Estrutura do Projeto

- **Models**:
  - `Technologies`: Tecnologias utilizadas em projetos e por desenvolvedores.
  - `Programmers`: Desenvolvedores e suas tecnologias associadas.
  - `Projects`: Projetos com tecnologias exigidas e horas diárias alocadas.
  - `Allocations`: Alocação de desenvolvedores em projetos.
  - `BaseModel`: Models base para separação de tenants.
    
- **Serializers**:
  Serialização e validação de dados para os models.

- **Views**:
  Endpoints para realizar operações CRUD.

- **Tests**:
  Testes automatizados para verificar as funcionalidades da API, incluindo:
  - Testes CRUD para todos os modelos.
  - Testes de acesso para todos os modelos.
  - Testes de validações:
    - Validação de tecnologias do desenvolvedor ao alocá-lo em um projeto.
    - Validação de períodos para horas planejadas.
    - Validação do limite de horas alocadas.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados, antes da execução do projeto:

- Python 3.9+
- Django 4.2+
- Django REST Framework
- Django Filter

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/eldertomaz/teste_django
   cd teste_django
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv env
   source env/bin/activate # Linux/MacOS
   env\Scripts\activate   # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4.  Configure o banco de dados:
    
  -   Crie o banco no PostgreSQL:
        
    ```sql
    CREATE DATABASE nome_do_banco;
        
    ```
        
  -   Configure o usuário e permissões:
        
    ```sql
    CREATE USER usuario WITH PASSWORD 'senha';
    GRANT ALL PRIVILEGES ON DATABASE nome_do_banco TO usuario;    
    ```

5. Configure o banco de dados: O projeto utiliza o PostgreSQL como banco de dados. Certifique-se de ter um servidor PostgreSQL ativo e crie um arquivo `.env` baseado no exemplo fornecido (`.env_example`) com as seguintes configurações:
    
  ```env
  DATABASE_NAME=nome_do_banco
  DATABASE_USER=usuario
  DATABASE_PASSWORD=senha
  DATABASE_HOST=localhost
  ```

6. Aplique as migrações:
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

## Suporte a Docker

O projeto possui suporte a Docker. Siga os passos abaixo para configurar e rodar o ambiente com Docker:

1. **Crie o arquivo `.env`** baseado no exemplo fornecido (`.env_example`) com as configurações do banco de dados:
   ```env
   DATABASE_NAME=meu_banco
   DATABASE_USER=meu_usuario
   DATABASE_PASSWORD=minha_senha
   DATABASE_HOST=db
   DATABASE_PORT=5432
   ```

2. **Configure o ambiente com `docker-compose`**:
  Certifique-se de que o arquivo `docker-compose.yml` está no diretório raiz do projeto.

3. **Suba os contêineres**:
   Execute os comandos abaixo para iniciar os contêineres:
   ```bash
   docker-compose build
   docker-compose up
   ```

4. **Acesse a aplicação**:
   Acesse a aplicação em [http://localhost:8000](http://localhost:8000).

5. **Parar os contêineres**:
   Para parar os contêineres, use:
   ```bash
   docker-compose down
   ```

## Suporte a Swagger

O projeto inclui suporte ao Swagger para documentação. Para acessar, siga os passos:

1. **Certifique-se de que o servidor está em execução**:
   ```bash
   python manage.py runserver
   ```
   Ou, se estiver usando Docker:
   ```bash
   docker-compose up
   ```

2. **Acesse os Endpoints do Swagger**:
   - **Swagger UI**: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

## Filtragem de Dados

Os endpoints suportam filtragem utilizando a biblioteca `django-filter`, garantindo que os dados filtrados sejam restritos ao `tenant` (usuário autenticado). 

### Technologies
- **`name`**: Filtra por nome da tecnologia (case-insensitive).

### Programmers
- **`name`**: Filtra por nome do programador (case-insensitive).
- **`technologies`**: Filtra por tecnologias (todas as tecnologias selecionadas devem estar presentes).

### Projects
- **`name`**: Filtra por nome do projeto (case-insensitive).
- **`start_date`**: Filtra projetos iniciados a partir de uma data específica.
- **`end_date`**: Filtra projetos com término até uma data específica.
- **`technologies`**: Filtra projetos com tecnologias específicas (qualquer tecnologia selecionada).

### Allocations
- **`project`**: Filtra por projeto.
- **`programmer`**: Filtra por programador.
- **`hours`**: Filtra alocações com número mínimo de horas.

Para utilizar os filtros, inclua os parâmetros na URL da requisição, por exemplo:
```http
GET /user/programmers/?name=Teste&technologies=1,2
GET /user/projects/?start_date=2025-01-01&end_date=2025-12-31
```

## Autenticação

Os endpoints são protegidos e para serem acessados, é necessário:

1.  **Registrar um novo usuário:** Utilize o endpoint `/user/register/` fazendo um `POST` para criar um novo usuário. Exemplo de payload:
    ```json
    {
        "username": "meu_usuario",
        "password": "minha_senha"
    }
    ```
    
    A resposta:

    ```json
    {
        "message": "User criado.",
        "data": {
            "user_id": "<TENANT_ID>"
        }
    }
    ```

2.  **Obter o token JWT:** Utilize o endpoint `/user/token/` com o `username` e `password` para obter o token de autenticação. Exemplo de payload:
    
    ```json
    {
        "username": "meu_usuario",
        "password": "minha_senha"
    }
    
    ```
    
    A resposta:
    
    ```json
    {
        "access": "<TOKEN_DE_ACESSO>",
        "refresh": "<TOKEN_DE_REFRESH>"
    }
    
    ```



3.  **Usar o token como Bearer Token:** Inclua o token no cabeçalho de cada requisição:
    
    ```
    Authorization: Bearer <TOKEN_DE_ACESSO>
    
    ```

## Como Executar os Testes

Para executar os testes automatizados, use o comando:
```bash
python manage.py test core.apps.user.tests
```

## Endpoints Disponíveis

A API está configurada com os seguintes endpoints:

- **/user/technologies/**:
  - `GET`: Lista todas as tecnologias.
  - `POST`: Cria uma nova tecnologia.
  - `PATCH`: Atualiza uma tecnologia existente.
  - `DELETE`: Remove uma tecnologia.

- **/user/programmers/**:
  - `GET`: Lista todos os programadores.
  - `POST`: Cria um novo programador.
  - `PATCH`: Atualiza um programador existente.
  - `DELETE`: Remove um programador.

- **/user/projects/**:
  - `GET`: Lista todos os projetos.
  - `POST`: Cria um novo projeto.
  - `PATCH`: Atualiza um projeto existente.
  - `DELETE`: Remove um projeto.

- **/user/allocations/**:
  - `GET`: Lista todas as alocações.
  - `POST`: Cria uma nova alocação.
  - `PATCH`: Atualiza uma alocação existente.
  - `DELETE`: Remove uma alocação.

## Observações Importantes

- Apenas objetos associados ao `tenant` (usuário autenticado) são acessíveis.
- As validações nos serializers garantem integridade dos dados e regras de negócio.
- Para autenticação, utilize o mecanismo de autenticação por token JWT, configurado nos endpoints de login.

