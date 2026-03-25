#  Script para Limpeza de Dados 

Este projeto consiste em um script robusto de ETL (Extract, Transform, Load) desenvolvido em Python para a limpeza e normalização de um conjunto de dados de vendas de uma cafeteria. O foco principal é transformar dados brutos e inconsistentes em um formato pronto para análise estatística e visualização.

## Objetivo

O objetivo deste script é automatizar o tratamento de erros comuns em coleta de dados, como valores sentinela ("ERROR", "UNKNOWN"), inconsistências de tipos de dados e falhas de integridade matemática.

## O Dataset

O arquivo original `dirty_cafe_sales.csv` contém aproximadamente 10.000 registros com os seguintes observações:
- **Valores Nulos Mascarados:** Uso de strings como "UNKNOWN" e "ERROR" em vez de valores nulos reais.
- **Tipagem Incorreta:** Datas e valores numéricos lidos como "object".
- **Inconsistência Lógica:** Valores de `Total Spent` que não correspondiam à multiplicação de `Quantity` por `Price Per Unit`.
- **Nomes de Colunas:** Presença de espaços e capitalização inconsistente.

## 🛠️ Tecnologias Utilizadas

- **Python 3.11.14** (Ambiente Linux Fedora)
- **Pandas:** Manipulação e análise de dados.
- **NumPy:** Suporte para operações matemáticas e valores nulos (NaN).

## 🚀 Pipeline de Limpeza

O processo de tratamento segue seis etapas fundamentais:

1.  **Normalização de Metadados:** Conversão dos nomes das colunas para o padrão `snake_case`.
2.  **Tratamento de Sentinelas:** Conversão global de strings de erro para `np.nan`.
3.  **Conversão de Tipos:** Forçagem de tipos numéricos (`float64`, `Int64` nullable) e datas (`datetime`).
4.  **Imputação de Preços:** Recuperação de preços unitários faltantes através de um mapeamento lógico por item.
5.  **Integridade Matemática:** Recálculo da coluna de faturamento total para garantir consistência.
6.  **Validação e Deduplicação:** Remoção de transações duplicadas e registros irrecuperáveis.
