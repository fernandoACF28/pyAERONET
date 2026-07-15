# pyAERONET

Este pacote é um software livre para acessar os dados 
das estações AERONET.

AErosol RObotic NETwork <a href='https://aeronet.gsfc.nasa.gov/' target='_blank'>AERONET</a>
é uma rede de fotômetros solares da <a href='https://www.nasa.gov/', target='_blank'>NASA</a>.


# Utilidade 

<ul>
  <li>Leituras da rede de fotômetros (AERONET);</li>
  <li>Download dos dados;</li>
  <li>Funções úteis, como interpolação de <i>AOD 550 nm</i>.</li>
</ul>


# Função de interpolação
<p style="text-align: justify;">
Este pacote é útil para realizar leituras da rede de fotômetros (AERONET), além de poder realizar o download.
Neste pacote também contém algumas funções úteis como a de interpolação da profundidade óptica em <i>550 nm</i>,
utilizando o método logarítimo (<a href="https://doi.org/10.1002/2016JD026301" target="_blank">Martins et. al, 2017</a>; <a href="https://doi.org/10.1029/92JD02427" target="_blank">Kaufman et. al, 1993</a>). Além do método de calcular as propriedades ópticas em banda larga ponderando os pesos, entre outras.
</p>

<p style="text-align: justify;">
Abaixo segue uma tabela de algumas variáveis que podem ser obtidas das estações AERONET.
Os prefixos terminados estão terminados em valores numéricos, sendo 10,15 e 20, os níveis de recuperação.
Os dados de nível 1, são dados brutos, dados de nível 1,5 com filtro de nuvens, enquanto dados de nível 2 com correções de medições.
</p>

| Variables (parameter `vars`)  | Explanation |
| --- | --- |
| AOD10  | Aerosol Optical Depth Level 1.0 |
| AOD15  | Aerosol Optical Depth Level 1.5 |
| AOD20  | Aerosol Optical Depth Level 2.0 |
| SDA10  | SDA Retrieval Level 1.0 |
| SDA15  | SDA Retrieval Level 1.5 |
| SDA20  | SDA Retrieval Level 2.0 |
| TOT10  | Total Optical Depth based on AOD Level 1.0 (all points only) |
| TOT15  | Total Optical Depth based on AOD Level 1.5 (all points only) |
| TOT20  | Total Optical Depth based on AOD Level 2.0 (all points only) |
| LWN10  | Normalized Water Leaving Radiances Level 1.0 |
| LWN15  | Normalized Water Leaving Radiances Level 1.5 |
| LWN20 (not yet available)  | Normalized Water Leaving Radiances Level 2.0 |
| ZEN00  | Raw Zenith Sky Scan Radiance |
| ALM00  | Raw Almucantar Sky Scan Radiance |
| HYB00  | Raw Hybrid Sky Scan Radiance |
| PPL00  | Raw Principal Plane Sky Scan Radiance |
| PPP00  | Raw Polarized Principal Plane Sky Scan Radiance and Degree of Polarization |
| ALP00  | Raw Polarized Almucantar Sky Scan Radiance and Degree of Polarization |
| HYP00  | Raw Polarized Hybrid Sky Scan Radiance and Degree of Polarization |
