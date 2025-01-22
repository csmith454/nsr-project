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
def to_dataframe(start_y,name_list):
    
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
    
    # .extract_table() takes JSON table settings if needed
    
    curr_y = start_y
    table_dict = {}
    
    for x in range(len(pdf_dict.items())):      # enter into each pdf_dict entry
        table_list = []
        for page in pdf_dict[curr_y]:           # enter into each page of a particular pdf
            table_to_add = page.extract_table() 
            table_list.append(table_to_add)
        table_dict[curr_y] = table_list 
        curr_y+=1 
        
    return table_dict

# #------#
# |      | 
# |      |
# #------#
# def debug_output(pdf):
    
    
    
# #------#
# |      | 
# |      |
# #------#
def main():
    
    start_year = 2011
    max_year = 2018
    pdf_dict = to_dataframe(start_year,create_paths(start_year,max_year))

    table_dict = extract_pages(start_year, pdf_dict)
    

if __name__ == '__main__':
    main()
