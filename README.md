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
    
  O `settings.py` carrega essas configurações utilizando o módulo `os`:
    
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DATABASE_NAME'),
            'USER': os.environ.get('DATABASE_USER'),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
            'HOST': os.environ.get('DATABASE_HOST'),
            'PORT': '5432',
        }
    }
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

