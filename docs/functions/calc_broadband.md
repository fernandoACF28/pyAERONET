```markdown
# pyAERONET.calcular_broadband_aeronet

Calcula as propriedades ópticas integradas em banda larga (broadband) ponderando os valores espectrais das estações AERONET com os pesos solares característicos.

Esta função é particularmente útil para preparar dados de entrada para modelos de transferência radiativa, como o libRadtran.

---

`calcular_broadband_aeronet(df)`

**Parâmetros:**

*   **df** : *polars.DataFrame*
    DataFrame contendo os dados invertidos da AERONET. As colunas devem obrigatoriamente incluir os dados de *Single Scattering Albedo*, *Asymmetry Factor* e *Surface Albedo* nos comprimentos de onda de 440, 675, 870 e 1020 nm.

**Retorna:**

*   **df_out** : *polars.DataFrame*
    Retorna o DataFrame original expandido com 3 novas colunas resultantes do cálculo ponderado:
    *   `ssa_broadband`: Albedo de Espalhamento Simples em banda larga.
    *   `asy_broadband`: Fator de Assimetria em banda larga.
    *   `surface_albedo_broadband`: Albedo de Superfície em banda larga.