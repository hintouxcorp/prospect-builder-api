# API – Sistema de Prospecção Comercial

API REST desenvolvida para gerenciamento de leads comerciais, controle de status de prospecção e fornecimento de dados para dashboard analítico.

Projeto em desenvolvimento.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Django
- Django REST Framework
- Banco de dados: (PostgreSQL ou SQLite – ajuste aqui)

---

## 🏗 Arquitetura

A API segue o padrão REST, com separação entre:

- Models (modelagem relacional das entidades)
- Serializers (serialização e validação de dados)
- Views / ViewSets (regras de negócio)
- Rotas organizadas por app

Estrutura simplificada:

```
project/
│
├── leads/
├── interactions/
├── config/
├── manage.py
└── requirements.txt
```

A aplicação foi estruturada para ser consumida por um frontend desacoplado, permitindo escalabilidade independente das camadas.

---

## 📌 Funcionalidades Implementadas

- Cadastro de leads
- Atualização de status de prospecção
- Registro de interações comerciais
- Listagem e filtragem de registros
- Endpoints RESTful estruturados

---

## 🔐 Autenticação

Atualmente a API não possui autenticação implementada.

A implementação de autenticação baseada em JWT e controle de permissões está prevista como próxima etapa de evolução do projeto.

---

## ▶ Como Executar Localmente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

Ativar:

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar migrações

```bash
python manage.py migrate
```

### 5️⃣ Executar servidor

```bash
python manage.py runserver
```

A API estará disponível em:
```
http://127.0.0.1:8000/
```

---

## 🔄 Roadmap

- Implementação de autenticação JWT
- Controle de permissões por usuário
- Paginação otimizada
- Documentação automática com Swagger/OpenAPI
- Testes automatizados
- Deploy em ambiente de produção

---

## 📌 Observação

Este projeto faz parte de uma aplicação full-stack onde o frontend (React) consome esta API de forma desacoplada.