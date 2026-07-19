
# Getting Started

Aqui vamos ensinar como começar utilizando a biblioteca pyAERONET.
Primeiro é necessário realizar a instalação da biblioteca, que pode
ser instalada utilizando gerenciador de pacotes `pip` ou `uv`ultraviolet [[source]](https://docs.astral.sh/uv/guides/install-python/).


=== "pip"

    ```bash
    pip install git+https://github.com/fernandoACF28/pyAERONET.git
    ```

=== "uv"

    ```bash
    uv pip install git+https://github.com/fernandoACF28/pyAERONET.git
    ```

## Download dos dados

Abaixo está um exemplo de como realizar o download do arquivo `csv` 
, ler e processar os dados de aerossóis diretamente no Python [`pyAERONET.GetDataAERONET()`](functions/get_data.md).


=== "Python"

    ```python
    import pyAERONET
    ```

    `pyAERONET` é uma classe que contém funções.
    A função para download é 
    `GetDataAERONET`

    ```python
    pyAERONET.GetDataAERONET(station='Sao_Paulo',start_date='2010-10-10',
                        end_date='2012-10-10',
                        vars='AOD20',
                        temporal_type='ALL',
                        user_name='user@gmail.br')
    ```

        Finish Download: 100%|██████████| 3/3 [00:09<00:00,  3.19s/it]                   

## Leitura dos dados

```python
import polars as pl
```


```python
df = pl.read_csv('Sao_Paulo_AOD20.csv')
df_exemplo = df.select(['time', 'AOD_500nm', 'AERONET_Site']).head(4)
df_exemplo
```




<div><style>
.dataframe > thead > tr,
.dataframe > tbody > tr {
  text-align: right;
  white-space: pre-wrap;
}
</style>
<small>shape: (4, 3)</small><table border="1" class="dataframe"><thead><tr><th>time</th><th>AOD_500nm</th><th>AERONET_Site</th></tr><tr><td>str</td><td>f64</td><td>str</td></tr></thead><tbody><tr><td>&quot;2010-10-12 12:00:00&quot;</td><td>0.099469</td><td>&quot;Sao_Paulo&quot;</td></tr><tr><td>&quot;2010-10-13 12:00:00&quot;</td><td>0.195643</td><td>&quot;Sao_Paulo&quot;</td></tr><tr><td>&quot;2010-10-14 12:00:00&quot;</td><td>0.676282</td><td>&quot;Sao_Paulo&quot;</td></tr><tr><td>&quot;2010-10-16 12:00:00&quot;</td><td>0.481589</td><td>&quot;Sao_Paulo&quot;</td></tr></tbody></table></div>


