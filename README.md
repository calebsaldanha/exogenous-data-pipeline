# Exogenous Data Pipeline

Este reposit√≥rio cont√©m um pipeline de engenharia de dados focado na captura de indicadores macroecon√¥micos oficiais para suporte a modelos de **Infer√™ncia Causal** e **Data Science**.

## Ì∫Ä Objetivo
Automatizar a ingest√£o de dados ex√≥genos (Selic, IPCA, C√¢mbio PTAX e Feriados) para permitir o isolamento de fatores externos em estudos de incrementabilidade (Uplift) e comportamento do consumidor.

## Ìª†Ô∏è Tecnologias
* **Python** (Pandas, SQLAlchemy, Requests)
* **PostgreSQL**
* **APIs:** Banco Central do Brasil (SGS e Olinda) e Brasil API.

## Ì≥ä Estrutura
* `/sql`: DDL para cria√ß√£o do schema e tabelas.
* `/src`: Script de ingest√£o robusto com tratamento de dados.

---
*Este projeto faz parte do meu [Portf√≥lio de Data Science](https://github.com/calebsaldanha/calebsaldanha-portfolio).*
