# Planejador de Viagem Multicritério ✈️

Este projeto é um protótipo de sistema para planejamento de viagens otimizadas. A aplicação modela cidades como um grafo e utiliza uma busca heurística para maximizar a satisfação do turista, respeitando restrições de orçamento financeiro e tempo de viagem.

## 🛠️ Tecnologias Utilizadas

* **Backend/Algoritmo:** [Python 3.14](https://www.python.org/downloads/)
* **Framework Web:** [Django](https://docs.djangoproject.com/pt-br/6.0/) + [django_bootstrap](https://django-bootstrap5.readthedocs.io/en/latest/)
* **Frontend:** HTML5 e [Bootstrap 5](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

## 🚀 Como executar o projeto localmente

Siga o passo a passo abaixo para rodar a aplicação no seu ambiente de desenvolvimento.

### 1. Clonar o repositório (ou acessar a pasta do projeto)
Abra o seu terminal e navegue até a pasta raiz do projeto onde está o arquivo `manage.py`:
```bash
cd caminho/para/o/projeto/triplanner
```

### 2. Criar o Ambiente Virtual (venv)
O ambiente virtual isola as dependências do projeto para não conflitar com outras bibliotecas do seu sistema operacional.

```bash
python -m venv venv
```
### 3. Ativar o Ambiente Virtual
O comando varia dependendo do seu sistema operacional:

* Linux / macOS:

```bash
source venv/bin/activate
```

* Windows:

```bash
venv\Scripts\activate
```
(Quando o ambiente estiver ativo, você verá o prefixo (venv) no seu terminal).

### 4. Instalar as Dependências
Com o ambiente ativado, instale as dependências:

```bash
pip install -r requirements.txt
```

> Após instalar/remover uma dependência, execute `pip freeze > requirements.txt` para recriar o arquivo de _requirements_ atualizado.

### 5. Executar as Migrações do Django
Para preparar o banco de dados padrão do Django (SQLite) e evitar avisos de erro no terminal:

```bash
python manage.py migrate
```
### 6. Iniciar o Servidor de Desenvolvimento

```bash
python manage.py runserver
```
### 7. Acessar a Aplicação
Abra o seu navegador web e acesse o endereço fornecido pelo terminal, geralmente:
👉 http://127.0.0.1:8000
