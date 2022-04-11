import pandas as pd
import numpy as np

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
    
    