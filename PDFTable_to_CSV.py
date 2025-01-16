import tabula
import pandas as pd

def create_paths(start_y,max_y):

    path_list = []
    curr_y = start_y
    nsr_dir = '~/NSRData_PDF/'

    while (curr_y <= max_y):
        path = nsr_dir + 'NSR_' + curr_y + '.pdf'
        path_list.append(path)
        year+=1

    return path_list 

def to_dataFrame(start_y,max_y,path_list):
    df_dict = {}
    curr_y = start_y

    for p in path_list:
        df = tabula.read_pdf(p,pages='all',lattice=True)
        df_dict[curr_y] = df 
        curr_y+=1

    return df_dict 


def main():
    start_year = '2011'
    max_year = '2018'
    df_dict = to_dataFrame(start_year,max_year,create_paths())

    table = df_dict['2011'][0] 
    print(table)

if __name__ == '__main__':
    main()