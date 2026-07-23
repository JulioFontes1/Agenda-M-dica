# Agenda Médica

Aplicação web para gerenciamento de agendamentos médicos desenvolvida com **Flask**, **SQLAlchemy**, **Flask-Login** e **Tabulator.js**.

## Requisitos

- Python 3.12+
- pip
- Git (opcional)

---

## Criando o ambiente virtual (venv)

Clone o projeto:

```bash
git clone <url-do-repositorio>
cd agenda-medica
```

Crie o ambiente virtual:

### Linux / macOS

```bash
python3 -m venv .venv
```

### Windows

```bash
python -m venv .venv
```

Ative a venv:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

---

## Instalando dependências

Com a venv ativada:

```bash
pip install -r requirements.txt
```

---

## Configurando o banco de dados

Execute as migrações:

```bash
flask --app app.app db upgrade
```

Caso seja a primeira execução e as migrações ainda não existam:

```bash
flask -app app.app db init
flask -app app.app db migrate -m "initial migration"
flask -app app.app db upgrade
```

---

## Executando a aplicação

Defina o módulo Flask:

### Linux / macOS

```bash
export FLASK_APP=app.app
```

### Windows

```powershell
$env:FLASK_APP="app.app"
```

Execute:

```bash
flask run
```

A aplicação estará disponível em:

```
http://127.0.0.1:5000
```

Também é possível executar diretamente:

```bash
python -m app.app
```

---

## Executando os testes

Certifique-se de que a venv está ativada e execute:

```bash
pytest
```

Para visualizar mais detalhes:

```bash
pytest -v
```

---

## Estrutura do projeto

```
agenda-medica/
│
├── app/
│   ├── routes/
│   ├── models/
│   ├── static/
│   ├── templates/
│   └── app.py
│
├── migrations/
├── tests/
├── instance/
│   └── agenda.db
│
├── mock/
│   |── getuser.py
│   └── user.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Tecnologias utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- SQLite
- Tabulator.js
- Pytest
