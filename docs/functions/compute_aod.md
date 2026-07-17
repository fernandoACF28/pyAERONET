# pyAERONET.compute_AOD_550_polars

Interpola a Profundidade Óptica dos Aerossóis (AOD) para 550 nm utilizando o modelo log-log quadrático de [Eck et al. (1999)](https://doi.org/10.1029/1999JD900923).

A interpolação baseia-se na seguinte equação polinomial de segunda ordem:

$$\ln(\text{AOD}) = \beta_2(\ln \lambda)^2 + \beta_1(\ln \lambda) + \beta_0$$

---

`compute_AOD_550_polars(df, columns_aod, wavelenght_nm, return_columns)`

**Parâmetros:**

*   **df** : *polars.DataFrame*
    DataFrame do Polars contendo os dados com as colunas de AOD originais.
*   **columns_aod** : *list*, default `['AOD_440nm','AOD_500nm','AOD_675nm']`
    Lista com os nomes das colunas de AOD presentes no DataFrame que serão utilizadas para o ajuste.
*   **wavelenght_nm** : *list*, default `[440, 500, 675]`
    Lista com os comprimentos de onda (em nm) correspondentes às colunas informadas no parâmetro anterior.
*   **return_columns** : *list*, opcional
    Lista de colunas específicas a serem retornadas no DataFrame final. Se `None`, retorna as colunas originais junto com a nova coluna calculada.

**Retorna:**

*   **df_out** : *polars.DataFrame*
    Uma cópia do DataFrame original com a adição de uma nova coluna chamada `AOD_550nm`.