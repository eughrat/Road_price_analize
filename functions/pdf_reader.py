import camelot as cam
import pandas as pd
import glob

def pdf_reader(path:str):

    pdf_path_list = []
    all_reports_list=[]

    for file in glob.glob(path):
        pdf_path_list.append(file)

    for path in pdf_path_list:
        road_data = cam.read_pdf(path,pages='all', flavor='lattice')

        for page, pdf_table in enumerate(road_data):
            report = road_data[page].df
            all_reports_list.append(report)

    all_reports_df = pd.concat(all_reports_list)
    
    return all_reports_list
            