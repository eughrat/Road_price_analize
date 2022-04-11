import camelot as cam
import numpy as np
import pandas as pd
import glob
from difflib import get_close_matches


def pdf_reader(path:str):

    pdf_path_list = []
    all_reports_list=[]

#   Import pdf path to path_list to extract them to the df in the next step
    for file in glob.glob(path):
        pdf_path_list.append(file)
        
#   Read all pdf files one after another
    for path in pdf_path_list:
        road_data = cam.read_pdf(path,pages='all', flavor='lattice')

#       Each of pdf file is converted to df with first data clean (erasing first row) 
        for page, pdf_table in enumerate(road_data):
            report = road_data[page].df
            report_cl = report.iloc[1:]
            all_reports_list.append(report_cl)
            
#   Concate all single dfs to one DataFrame
    all_reports_df = pd.concat(all_reports_list)
    
    return all_reports_df

################################################################################################################

def pdf_cleaner(df):
    
    # Setting new column names
    df.columns = 'Lp CPV Numer_Specyfikacji_Technicznej Elementy_rozliczeniowe Jednostka Ilosc Cena_jedn Wartosc_calkowita Droga Rok Kategoria'.split()
    
    #Replace all blank cells with NaN
    df.ffill(axis=0,inplace=True)
    df.replace({'\n': '',
               '': np.nan}, regex=True, inplace=True)
        
    # Columns "Lp CPV Numer_Specyfikacji_Technicznej" are not essential to road costs analysis so its ok to drop them    
    df.drop(['Lp','CPV','Numer_Specyfikacji_Technicznej'], axis=1, inplace=True)
    
    # Now we can see that our dataframe have NaN cells only in dexcription rows, so we can drop rows with NaN.
    df.dropna(inplace=True)
        
    return df

################################################################################################################

def match_category(row):
#   List of accepted categories of construction work
    correct_cat = ['ROBOTY PRZYGOTOWAWCZE',
                    'OZNAKOWANIA DROG',
                    'ZIELEN DROGOWA',
                    'PODBUDOWY',
                    'NAWIERZCHNIE',
                    'ROBOTY WYKONCZENIOWE',
                    'ELEMENTY ULIC',
                    'WARUNKI OGOLNE',
                    'ROBOTY ZIEMNE',
                    'ODWODNIENIE',
                    'ODWODNIENIE KORPUSU DROGOWEGO',
                    'INNE ROBOTY']
    
#   Return a list of the best “good enough” matches
    match = get_close_matches(row, correct_cat, n=1,cutoff=0.3)
    
    return match[0] if match else ''





















