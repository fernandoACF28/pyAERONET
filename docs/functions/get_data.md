# pyAERONET.GetDataAERONET

Realiza o download de dados de estações da rede AERONET (NASA) de acordo com o tipo de dado, período e resolução temporal desejada.

---

`GetDataAERONET(station, start_date, end_date, vars, temporal_type, inversion_type, user_name)`

**Parâmetros:**

*   **station** : *str*
    Nome da estação AERONET (ex: `'Sao_Paulo'`).
*   **start_date** : *str*
    Data de início do período desejado no formato `YYYY-MM-DD`.
*   **end_date** : *str*
    Data de fim do período desejado no formato `YYYY-MM-DD`.
*   **vars** : *str*.
    Nome da variável ou nível do produto AERONET a ser baixado (ex: `'AOD10'`, `'AOD15'`, `'AOD20'`)[[source]](retrieval.md).
*   **temporal_type** : *str*
    Resolução temporal dos dados. O pacote converte automaticamente essa entrada para os códigos da API da AERONET (`AVG`):
    *   `'all'` (AVG = 10): Todos os pontos de dados disponíveis.
    *   `'daily'` ou `'daily average'` (AVG = 20): Média diária.
*   **inversion_type** : *str*, opcional
    Tipo de inversão utilizada na recuperação dos dados, necessário para propriedades ópticas avançadas (ex: `'ALM15'` para Almucantar Nível 1.5 ou `'HYB20'` para Hybrid Nível 2.0)[[source]](retrieval.md).
*   **user_name** : *str*, opcional
    Seu endereço de e-mail de contato, recomendado para requisições na plataforma da NASA.

**Exemplo de uso:**

```python
pyAERONET.GetDataAERONET(
    station='Sao_Paulo',
    start_date='2010-10-10',
    end_date='2012-10-10',
    vars='AOD20',
    temporal_type='all',
    user_name='seu_email@dominio.com'
)
```