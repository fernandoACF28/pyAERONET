def typingDate(start_date,end_date):
    try:
        start_date = start_date.split('-')
        end_date = end_date.split('-')
        YEAR_1,MONTH_1,DAY_1 = int(start_date[0]),int(start_date[1]),int(start_date[2])
        YEAR_2,MONTH_2,DAY_2 = int(end_date[0]),int(end_date[1]),int(end_date[2])
    except: print('Your data is not a valid time. Try YYYY-MM-DD.')
    return YEAR_1,MONTH_1,DAY_1,YEAR_2,MONTH_2,DAY_2


def path_download(vars,inversion_type,station,AVG,YEAR_1,MONTH_1,DAY_1,
                  YEAR_2,MONTH_2,DAY_2):

    def PRINTEXCEPT(vars,valid_vars):
            print('#############################################################')
            print(f'{vars} is not valid variable')
            print(f'Are you sure this variable {vars} exists?')
            print(f'Try: {valid_vars}')

    inversion = ['SIZ', 'RIN',	'CAD', 'VOL', 'TAB', 'AOD',
              'SSA', 'ASY', 'FRC', 'LID', 'FLX', 'ALL',
              'PFN', 'U27']
    aod_retrieval = ['AOD10', 'AOD15', 'AOD20',
                    'SDA10', 'SDA15', 'SDA20',
                    'TOT10', 'TOT15', 'TOT20']
    zenith_radiance = ['ZEN00']

    normalize_water = ['LWN10','LWN15','LWN20']

    sky_scan_measurements = ['ALM00','HYB00','PPL00',
                             'PPP00','ALP00', 'HYP00']
    all_vars = inversion+aod_retrieval+zenith_radiance+normalize_water+sky_scan_measurements

    if vars in inversion:
        inversions_types = ['ALM15','ALM20','HYB15','HYB20']
        if inversion_type == None: 
            print(f'You need define type of inversion: \n{inversions_types}')
        else:
            try:PATH_DOWNLOAD = ['https://aeronet.gsfc.nasa.gov/'
                'cgi-bin/print_web_data_inv_v3?'
                f'site={station}'
                f'&year={YEAR_1}&month={MONTH_1}&day={DAY_1}&'
                f'year2={YEAR_2}&month2={MONTH_2}&day2={DAY_2}'
                f'&product={vars}&AVG={AVG}&{inversion_type}=1']
            except Exception as e: print(e)

    elif vars in aod_retrieval:
        try:PATH_DOWNLOAD = ['https://aeronet.gsfc.nasa.gov/'
            'cgi-bin/print_web_data_v3?'
            f'site={station}'
            f'&year={YEAR_1}&month={MONTH_1}&day={DAY_1}&'
            f'year2={YEAR_2}&month2={MONTH_2}&day2={DAY_2}'
            f'&{vars}=1&AVG={AVG}']
        except Exception as e: print(e)

    elif vars in zenith_radiance:
        try:PATH_DOWNLOAD = ['https://aeronet.gsfc.nasa.gov/'
            'cgi-bin/print_web_data_zenith_radiance_v3?'
            f'site={station}'
            f'&year={YEAR_1}&month={MONTH_1}&day={DAY_1}&'
            f'year2={YEAR_2}&month2={MONTH_2}&day2={DAY_2}'
            f'&{vars}=1&AVG={AVG}']
        except Exception as e: print(e)
    elif vars in normalize_water:
        try:PATH_DOWNLOAD = ['https://aeronet.gsfc.nasa.gov/'
            'cgi-bin/print_web_data_v3?'
            f'site={station}'
            f'&year={YEAR_1}&month={MONTH_1}&day={DAY_1}&'
            f'year2={YEAR_2}&month2={MONTH_2}&day2={DAY_2}'
            f'&{vars}=1&AVG={AVG}&if_no_html=1']
        except Exception as e: print(e)
    elif vars in sky_scan_measurements:
        try:PATH_DOWNLOAD = ['https://aeronet.gsfc.nasa.gov/'
            'cgi-bin/print_web_data_raw_sky_v3?'
            f'site={station}'
            f'&year={YEAR_1}&month={MONTH_1}&day={DAY_1}&'
            f'year2={YEAR_2}&month2={MONTH_2}&day2={DAY_2}'
            f'&{vars}=1&AVG={AVG}']
        except Exception as e: print(e)
    
    else: PRINTEXCEPT(vars,all_vars)
    return PATH_DOWNLOAD