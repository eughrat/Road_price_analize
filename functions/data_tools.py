import numpy as np
import pandas as pd


def get_element(df, word:str):
  
    road_elem_df = df[df['Elementy_rozliczeniowe'].str.contains(word)]
    road_elem_df = road_elem_df.groupby('Droga').agg({'Ilosc': 'sum',
                                  'Dlugosc_drogi':'max'})
    
    return road_elem_df

def get_multiple_elem_method_or(df,*args):
    
    search = list(args)
    road_elem_df = df[df['Elementy_rozliczeniowe'].str.contains('|'.join(search))]
    road_elem_df = road_elem_df.groupby('Droga').agg({'Ilosc': 'sum',
                                                      'Dlugosc_drogi':'max'})
    
    return road_elem_df

def get_multiple_elem_method_and(df,*args):
    
    base = r'^{}'
    expr = '(?=.*{})'
    words = list(args)
    search = base.format(''.join(expr.format(w) for w in words))
    road_elem_df = df[df['Elementy_rozliczeniowe'].str.contains(search)]
    road_elem_df = road_elem_df.groupby('Droga').agg({'Ilosc': 'sum',
                                                      'Dlugosc_drogi':'max'})
    
    return road_elem_df

def col_per_km(df, col_name:str, col_origin:str):
    
    df[col_name] = df[col_origin] / df['Dlugosc_drogi']
    
    return df