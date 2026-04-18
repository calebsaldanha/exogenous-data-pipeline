# Exogenous Data Pipeline

Este repositorio contem um pipeline de engenharia de dados automatizado, focado na captura, transformacao e armazenamento de indicadores macroeconomicos oficiais e dados de calendario.

## Objetivo do Projeto
O principal objetivo deste pipeline e fornecer uma base de dados externa (schema `exogenas`) limpa e consolidada. Estes dados sao essenciais para isolar o efeito de sazonalidades e fatores economicos em modelos preditivos complexos, tais como **Inferencia Causal**, **Marketing Mix Modeling (MMM)** e **Credit Scoring dinamico**.

## Fontes de Dados (Integracao de APIs)
O processo de Extracao (Extract) consome dados diretamente de fontes governamentais e abertas:
* **Banco Central do Brasil (SGS):** Taxa Selic (Meta e Diaria) e IPCA (Mensal e Acumulado).
* **Banco Central do Brasil (API Olinda):** Cotacao cambial do Dolar (PTAX Compra e Venda).
* **Brasil API:** Calendario oficial de Feriados Nacionais.

## Arquitetura e Stack Tecnologica
* **Linguagem:** Python
* **Processamento:** Pandas e Requests
* **Banco de Dados:** PostgreSQL
* **Integracao de Banco:** SQLAlchemy
* **Design Pattern:** Carga idempotente (previne duplicacao de dados historicos)

## Estrutura do Repositorio
* `/sql/schema_exogeno.sql`: Script DDL para a criacao das tabelas no PostgreSQL.
* `/src/ingest_macro_data.py`: Script principal de ETL que orquestra a chamada as APIs e a injecao no banco de dados.
* `requirements.txt`: Dependencias do projeto.

## Como Executar

### 1. Configuracao do Ambiente
O script utiliza variaveis de ambiente para garantir a seguranca das credenciais do banco de dados. Configure as seguintes variaveis no seu sistema ou em um arquivo `.env` (caso utilize ferramentas como python-dotenv):

    DB_USER=seu_usuario
    DB_PASS=sua_senha
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=seu_banco

### 2. Instalacao de Dependencias
Instale os pacotes necessarios executando:

    pip install -r requirements.txt

### 3. Criacao do Schema
Execute o script SQL fornecido na pasta `/sql` diretamente no seu banco de dados PostgreSQL para criar a estrutura e as tabelas necessarias.

### 4. Execucao do Pipeline
Para iniciar a ingestao de dados, execute na raiz do projeto:

    python src/ingest_macro_data.py

---
*Nota: Este projeto e um modulo independente que compoe a infraestrutura de Central Data Hub do meu portfolio principal de Data Science.*
