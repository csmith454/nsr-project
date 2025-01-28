import os
import pdfplumber
import pandas as pd

# #------#
# |      | 
# |      |
# #------#
def create_paths(start_y,max_y):

    name_list = []
    curr_y = start_y

    while (curr_y <= max_y):
        file_name =  'NSR_' + str(curr_y) + '.pdf'
        name_list.append(file_name)
        curr_y+=1

    return name_list

# #------#
# |      | 
# |      |
# #------#
def to_pdf_dict(start_y,name_list):
    
    pdf_dict = {}
    curr_y = start_y
    nsr_dir = '/home/csmith/desktop/nsr-project/NSRData_PDF/'

    for n in name_list:
        full_path = os.path.join(nsr_dir,n)
        pdf = pdfplumber.open(full_path)
        pdf_dict[curr_y] = pdf
        curr_y+=1

    return pdf_dict 

# #------#
# |      | 
# |      |
# #------#
def extract_pages(start_y,pdf_dict):
    
    # .extract_table() takes JSON style table settings if needed
    
    curr_y = start_y
    table_dict = {}
    
    for item in pdf_dict.items():                              # enter into each pdf_dict entry
        table_list = []
        for n in range(len(pdf_dict[curr_y].pages)):           # enter into each page of a particular pdf
            table_to_add = pdf_dict[curr_y].pages[n].extract_table() 
            table_list.append(table_to_add)
        table_dict[curr_y] = table_list 
        curr_y+=1 
        
    return table_dict

# #------#
# |      | 
# |      |
# #------#
def to_dataframe(start_y,table_dict):
    
    curr_y = start_y
    df_dict = {}
    
    
    for item in table_dict.items():
        for n in range(len(table_dict[curr_y])):
            data = table_dict[curr_y][:] 
        df_dict[curr_y] = pd.DataFrame(data) 
        curr_y+=1
        
    return df_dict
    
# #------#
# |      | 
# |      |
# #------#
def main():
    
    start_year = 2011
    max_year = 2018
    
    pdf_dict = to_pdf_dict(start_year,create_paths(start_year,max_year))

    table_dict = extract_pages(start_year, pdf_dict)
    
    df_dict = to_dataframe(start_year,table_dict)
    
    print('Beginning CSV conversion...')
    print('Converting ' + str(len(df_dict.keys())) + ' DataFrames to CSV')
    path = '/home/csmith/desktop/nsr-project/NSRData_CSV/'
    
    for year, df in df_dict.items():
        file_name = 'nsr_' + str(year) + '.csv'
        full_path = os.path.join(path, file_name)
        df.to_csv(full_path)
        
    print('CSV conversion done!')

if __name__ == '__main__':
    main()
