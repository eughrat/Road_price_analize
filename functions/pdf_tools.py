import camelot as cam
import numpy as np
import pandas as pd
import glob
from difflib import get_close_matches

new_col_names = ['Lp', 'CPV', 'Numer_Specyfikacji_Technicznej',
                'Elementy_rozliczeniowe', 'Jednostka', 'Ilosc', 'Cena_jedn',
                'Wartosc_calkowita', 'Droga' ,'Rok', 'Kategoria']

cor_cat_list = ['ROBOTY PRZYGOTOWAWCZE', 'OZNAKOWANIA DROG', 'ZIELEN DROGOWA', 
                'PODBUDOWY','NAWIERZCHNIE', 'ROBOTY WYKONCZENIOWE', 
                'ELEMENTY ULIC', 'WARUNKI OGOLNE', 'ROBOTY ZIEMNE', 
                'ODWODNIENIE', 'ODWODNIENIE KORPUSU DROGOWEGO', 'INNE ROBOTY']


def read_pdfs(path:str, new_col_names = new_col_names):
    pdf_path_list = []
    all_reports_list=[]

    # Import pdf path to path_list to extract them to the df in the next step
    for file in glob.glob(path):
        pdf_path_list.append(file)

    # Read all pdf files one after another
    for path in pdf_path_list:
        road_data = cam.read_pdf(path,pages='all', flavor='lattice')

        # Each of pdf file is converted to df with first data clean (erasing first row) 
        for page, pdf_table in enumerate(road_data):
            report = road_data[page].df
            report_cl = report.iloc[1:]

            # Setting new column names
            report_cl.columns = new_col_names
            all_reports_list.append(report_cl)

    # Concate all single dfs to one DataFrame
    all_reports_df = pd.concat(all_reports_list)
    return all_reports_df

def clean_pdf(df, words_to_replace={'\n': '','': np.nan}, 
                col_to_drop=['Lp','CPV','Numer_Specyfikacji_Technicznej']):

    #Replace all blank cells with NaN
    df.ffill(axis=0,inplace=True)
    df.replace(words_to_replace, regex=True, inplace=True)

    # Columns "Lp CPV Numer_Specyfikacji_Technicznej" are not essential to road costs analysis so its ok to drop them    
    df.drop(col_to_drop, axis=1, inplace=True)

    # Now we can see that our dataframe have NaN cells only in dexcription rows, so we can drop rows with NaN.
    df.dropna(inplace=True)

    return df

def match_category(row, cor_cat_list = cor_cat_list):
#   List of accepted categories of construction work
    correct_cat = cor_cat_list

#   Return a list of the best “good enough” matches
    match = get_close_matches(row, correct_cat, n=1,cutoff=0.3)
    return match[0] if match else ''

       


        
        
        
     