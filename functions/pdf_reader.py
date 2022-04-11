import camelot as cam
import pandas as pd
import glob

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

            