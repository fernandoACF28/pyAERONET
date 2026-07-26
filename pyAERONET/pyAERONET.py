import os
import time
import httpx
import random
import requests
import numpy as np
import pandas as pd
import polars as pl
from lxml import html
from tqdm import tqdm
from .functions import *
from warnings import filterwarnings
filterwarnings('ignore')



class Organizer:
    def __init__(self,path):
        self.path = path
        self.dataframe = None
    def _toDateTime(self):
        '''internal method to treat datatime'''
        self.dataframe['Date(dd:mm:yyyy)'] = pd.to_datetime(self.dataframe['Date(dd:mm:yyyy)'],format ='%d:%m:%Y')
        self.dataframe['Time(hh:mm:ss)'] = pd.to_timedelta(self.dataframe['Time(hh:mm:ss)'])
        old_var,new_var = self.dataframe.columns[-1], self.dataframe.columns[-1][:-4]+'_'
        self.dataframe = self.dataframe.rename(columns={old_var:new_var})
        self.dataframe['time'] = self.dataframe['Date(dd:mm:yyyy)']+self.dataframe['Time(hh:mm:ss)']
        self.dataframe = self.dataframe.drop(columns=['Date(dd:mm:yyyy)','Time(hh:mm:ss)'])
        self.dataframe[new_var] = self.dataframe[new_var].replace('-999.<br>',np.nan)
        self.dataframe.insert(0, 'time', self.dataframe.pop('time'))
        return self.dataframe
    # Organize dataframe and save
    def treat_and_save(self,skip_rows):
        self.dataframe = pd.read_csv(self.path,
                        skiprows=skip_rows,
                        encoding='latin1')[:-1]
        self._toDateTime()
        self.dataframe.to_csv(self.path,index=False)

def RewriteTheFile(path):
    # checking the bytes of file
    if os.path.exists(path) and os.path.getsize(path) > 15:
        organizer = Organizer(path)
        success = False
        for i in range(15):
            try:
                organizer.treat_and_save(skip_rows=i)
                success = True
                break
            except Exception as e: pass
        if not success: print('impossible to process the file')
            
    else: print('the file is empty')

def download(station:str,
                  start_date:str,
                  end_date:str,
                  vars:str,
                  data_frequency:str,
                  inversion_type=None,
                  user_name=None):
    '''
    station: Name of your station
    start_date: start date of type: YYYY-MM-DD
    end_date: start date of type: YYYY-MM-DD
    vars: name of vars type: AOD10 or AOD15
    data_frequency: 'all' for all data, 'daily' for Daily Mean
    inversion_type: inv ex: ALM15 or HYB20
    user_name: inser your e-mail to contact
    '''
    if data_frequency == 'all': AVG = 10
    elif data_frequency =='daily': AVG = 20
    else: AVG = 20

    def _download(path,station,user_name):
        name_file = f'{station}_{vars}.csv'

        if os.path.exists(name_file): return 
        if user_name == None:headers = {'User-Agent': f'Python Script for Aerosol Research'}
        else:headers = {'User-Agent': f'Python Script for Aerosol Research (contact {user_name})'}
        progress_bar.set_description(f'Download for station: {station}...') # (Opcional) Atualiza o texto
        time.sleep(1)
        progress_bar.update(1)
        response = requests.get(path, headers=headers)
        response.raise_for_status() 
        with open(name_file, 'w', encoding='utf-8') as f:
            f.write(response.text)
        progress_bar.set_description(f'Download in: {name_file}')
        time.sleep(1)
        progress_bar.update(1)
        return response, name_file
    
    YEAR_1,MONTH_1,DAY_1,YEAR_2,MONTH_2,DAY_2 = typingDate(start_date=start_date,
                                                           end_date=end_date)
    PATH_DOWNLOAD = path_download(vars=vars,inversion_type=inversion_type,station=station,
                                  AVG=AVG,YEAR_1=YEAR_1,MONTH_1=MONTH_1,DAY_1=DAY_1,
                                  YEAR_2=YEAR_2,MONTH_2=MONTH_2,DAY_2=DAY_2)
    
    with tqdm(total=3, desc='downloading your data') as progress_bar:
        try:
            response,name_file = _download(PATH_DOWNLOAD[0],station,user_name)
            RewriteTheFile(name_file)
        except requests.exceptions.HTTPError as errh:
            print(f"Erro de HTTP: {errh}")
            if response.status_code == 429:
                print(">> (Too Many Requests). icrease the sleep time <<<")
        except requests.exceptions.ConnectionError as errc:
            print(f"Connection Error: {errc}")
        except Exception as e: print(f'Error! : {e}')
            
        # time for not crash for 
        delay = random.uniform(4, 8)
        progress_bar.set_description(f'Wait for {delay:.1f} seconds...')
        time.sleep(delay)
        progress_bar.update(1) 
        progress_bar.set_description('Finish Download')


def view_data(station:str,
                  start_date:str,
                  end_date:str,
                  vars:str,
                  data_frequency:str,
                  inversion_type=None):
    '''
    station: Name of your station
    start_date: start date of type: YYYY-MM-DD
    end_date: start date of type: YYYY-MM-DD
    vars: name of vars type: AOD10 or AOD15
    data_frequency: 'all' for all data, 'daily' for Daily Mean
    inversion_type: inv ex: ALM15 or HYB20
    user_name: inser your e-mail to contact
    '''
    if data_frequency == 'all': AVG = 10
    elif data_frequency =='daily': AVG = 20
    else: AVG = 20
    def get_PI_contact(rows):
        return rows[5].split('Contact:')[1].strip()
    def fetch_aeronet_data(path):
        response = httpx.get(path)
        if response.status_code == 200:
            return response.text
        else:
            print(f'Erro na requisição: {response.status_code}')
            return None
    def ViewDataAERONET(path):
        data = fetch_aeronet_data(path)
        if not data:
            return None
        tree = html.fromstring(data)
        texto = tree.text_content()
        linhas_iniciais = texto.split('\n', 7)
        PI = ""
        if len(linhas_iniciais) >= 7:
            try: PI = get_PI_contact(linhas_iniciais)
            except:   print('Verify the name of principal investigator to citate')
        else: 
            print('There are no data in these period')
            return None
        df_polars = pl.read_csv(
            texto.encode('utf-8'), 
            skip_rows=6, 
            separator=',',
            ignore_errors=True,
            infer_schema_length=10000 
        )
        # insert principal invertigator
        df_polars = df_polars.with_columns(pl.lit(PI).alias('Principal_Investigator'))
        # return dataframe
        return df_polars.to_pandas()

    YEAR_1,MONTH_1,DAY_1,YEAR_2,MONTH_2,DAY_2 = typingDate(start_date=start_date,
                                                               end_date=end_date)
    PATH_DOWNLOAD = path_download(vars=vars,inversion_type=inversion_type,station=station,
                                      AVG=AVG,YEAR_1=YEAR_1,MONTH_1=MONTH_1,DAY_1=DAY_1,
                                      YEAR_2=YEAR_2,MONTH_2=MONTH_2,DAY_2=DAY_2)

    return ViewDataAERONET(PATH_DOWNLOAD[0])


def compute_AOD550nm(df,
                    columns_aod=['AOD_440nm','AOD_500nm','AOD_675nm'],
                    wavelenght_nm=[440,500,675],
                    return_columns=None):
    ''' 
    interpolate AOD to 550 nm using model quadratic log de Eck et al.,
    (https://doi.org/10.1029/1999JD900923).
    ln AOD = beta_2x(ln lambda)**2+beta_1x(ln lambda)+beta_0 
    Parameters:
    - df: dataframe with columns of AOD
    - columns_aod:  list with name the columns of AOD (ex: ['AOD_440nm', 'AOD_500nm', 'AOD_675nm'])
    - wavelenght_nm: list of corresponding wavelenght with columns (ex: [440, 500, 675])
    return:
    - copy of dataframe with AOD 550nm: 'AOD_550nm'
    '''
    # converting to polars to acelerate the compute
    if type(df) is not pl.dataframe.frame.DataFrame:
        df = pl.from_pandas(df)
    # filtering with none values
    df = df.with_columns(pl.col(columns_aod).replace(-999.0,None))
    # calculate log of aod values
    df_new = df.with_columns([pl.col(column).log().alias(f'ln_{column}')
                               for column in columns_aod])
    list_ln_vars = [f'ln_{column}' for column in columns_aod]
    ln_lambda,ln_target = np.log(wavelenght_nm),np.log(550)
    df_lns_test = df_new.select(pl.col(list_ln_vars))
    # interpolate polinomial of second order
    coef = np.polyfit(ln_lambda,df_lns_test.to_numpy().T,deg=2)
    ln_aod_550 = coef[0]*ln_target**2 + coef[1]*ln_target + coef[2]
    # create a new column
    df_new_2 = df_new.with_columns(pl.Series(name='AOD_550nm',values=np.exp(ln_aod_550)))
    # returning a exception
    if return_columns is not None:
        df_new_2 = df_new_2.select(pl.col(return_columns))

    return df_new_2.to_pandas()

def Select(df:pl.dataframe.frame.DataFrame,vars_return:list):
    return df.select(pl.col(vars_return))


PESOS_AERONET = {
    '440': 1884.0,  
    '675': 1475.0,
    '870': 963.0,
    '1020': 733.0
}

def compute_broadband(dataframe):
    soma_pesos = sum(PESOS_AERONET.values())

    # converting to polars to acelerate the compute
    if type(dataframe) is not pl.dataframe.frame.DataFrame:
        dataframe = pl.from_pandas(dataframe)
    
    # compute single scattering albedo
    ssa_expr = (
        (pl.col('Single_Scattering_Albedo[440nm]') * PESOS_AERONET['440']) +
        (pl.col('Single_Scattering_Albedo[675nm]') * PESOS_AERONET['675']) +
        (pl.col('Single_Scattering_Albedo[870nm]') * PESOS_AERONET['870']) +
        (pl.col('Single_Scattering_Albedo[1020nm]') * PESOS_AERONET['1020'])
    ) / soma_pesos

    # compute asymmetry factor
    asy_expr = (
        (pl.col('Asymmetry_Factor-Total[440nm]') * PESOS_AERONET['440']) +
        (pl.col('Asymmetry_Factor-Total[675nm]') * PESOS_AERONET['675']) +
        (pl.col('Asymmetry_Factor-Total[870nm]') * PESOS_AERONET['870']) +
        (pl.col('Asymmetry_Factor-Total[1020nm]') * PESOS_AERONET['1020'])
    ) / soma_pesos

    # compute broadband surface albedo
    albedo_expr = (
        (pl.col('Surface_Albedo[440m]') * PESOS_AERONET['440']) +
        (pl.col('Surface_Albedo[675m]') * PESOS_AERONET['675']) +
        (pl.col('Surface_Albedo[870m]') * PESOS_AERONET['870']) +
        (pl.col('Surface_Albedo[1020m]') * PESOS_AERONET['1020'])
    ) / soma_pesos

    # return broadband variables
    return dataframe.with_columns([
        ssa_expr.alias('ssa_broadband'),
        asy_expr.alias('asy_broadband'),
        albedo_expr.alias('surface_albedo_broadband')
    ]).to_pandas()