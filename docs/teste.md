## Abrindo arquivo csv


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


