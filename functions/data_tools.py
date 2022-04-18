import numpy as np
import pandas as pd


def get_element(df, word:str):
  
    road_elem_df = df[df['Elementy_rozliczeniowe'].str.contains(word)]
    road_elem_df = road_elem_df.groupby('Droga').agg({'Ilosc': 'sum',
                                  'Dlugosc_drogi':'max'})
    
    return road_elem_df
