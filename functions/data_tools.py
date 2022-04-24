import numpy as np
import pandas as pd


# class PdfDataFrame():
    
#     def _init_(self):
#         self.df = df

def get_element(df, word:str, col_to_group='Elementy_rozliczeniowe', col_groupby= 'Droga', agg_dict={'Ilosc': 'sum','Dlugosc_drogi':'max'}):

    road_elem_df = df[df[col_to_group].str.contains(word)]
    road_elem_df = road_elem_df.groupby(col_groupby).agg(agg_dict)

    return road_elem_df

def get_multiple_elem_method_or(df, *args, col_to_group='Elementy_rozliczeniowe', col_groupby= 'Droga', agg_dict={'Ilosc': 'sum','Dlugosc_drogi':'max'}):

    search = list(args)
    road_elem_df = df[df[col_to_group].str.contains('|'.join(search))]
    road_elem_df = road_elem_df.groupby(col_groupby).agg(agg_dict)

    return road_elem_df

def get_multiple_elem_method_and(df, *args, col_to_group='Elementy_rozliczeniowe', col_groupby= 'Droga', agg_dict={'Ilosc': 'sum','Dlugosc_drogi':'max'},):

    base = r'^{}'
    expr = '(?=.*{})'
    words = list(args)
    search = base.format(''.join(expr.format(w) for w in words))
    road_elem_df = df[df[col_to_group].str.contains(search)]
    road_elem_df = road_elem_df.groupby(col_groupby).agg(agg_dict)

    return road_elem_df

def col_per_km(df, col_name:str, col_origin:str):

    df[col_name] = df[col_origin] / df['Dlugosc_drogi']

    return df


def map_col_type(df, names:list):
    
    for i in range(names):
         type = set(df[names[i]].map(type))
         return print(f"Column {names[i]} type: {type[0]}")