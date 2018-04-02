from GetData import *
from FormFile import *
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt


def edgar_data(ciklist, form, year):
    """This function is the main function.  Calls functions to created the list
    containing the file name with the meta data of the actually location of the detail file"""

    q = ['/QTR1/', '/QTR2/', '/QTR3/', '/QTR4/']
    root_url = 'https://www.sec.gov/Archives/edgar/daily-index/'
    url_detail_file = 'https://www.sec.gov/Archives/'
    url = []
    # below for loops concatenates year list and q (quarter) list into one list
    for x in year:
        for y in q:
            url.append(root_url + x + y)
    # local file
    # df = pd.read_csv\
    #    ('C:\\Users\\ralphd60\\Downloads\\master.20180116.idx',sep='|',parse_dates=True,skiprows = 7,header=None)

    # initializing this dataframe as empty it is used to only once to create the dataframe
    # after it is initially populated, we use the append method the for loop below retrieves the list
    # of daily-index files it then filters out just the 'master file"
    df_cik = None

    for link in url:
        master_file_list = get_file_list(link)
        for xfile in master_file_list:
            # loops through the list to extract out relevant files based on the paramneters
            # master file is indexed by the cik code
            print(xfile)
            try:
                df = pd.read_csv(link + xfile, sep='|', parse_dates=True, skiprows=7, header=None)
                df.columns = ['CIK', 'Company Name', 'Form Type', 'Date Filed', 'File Name']
                for cik in ciklist:
                    if df_cik is not None:
                        df_cik = df_cik.append(df.loc[np.logical_and(df['CIK'] == cik, df['Form Type'] == form)],
                                               ignore_index=True)
                    else:
                        df_cik = df.loc[np.logical_and(df['CIK'] == cik, df['Form Type'] == form)]
            except Exception as e:
                print("type error: " + str(e) + ": " + xfile)
    # count this is intialized here.  It is only used really once to see if a header is needed
    # when writing out the  the final results to a file
    count = 0
    for filename in df_cik['File Name']:
        print(filename)
        count1 = get_details(url_detail_file, filename, count)
        count = count1


if __name__ == '__main__':
    cik_code = []
    n = int(input('How many CIKs do you want to enter? '))
    for i in range(n):
        cik_code.append(int((input('CIK code - '))))
        print(cik_code)
    edgar_data(cik_code, '4', ['2016', '2017', '2018'])
# 70858 bac
# 1506307 kmi
# 1130310  cnp
# 1368265 clne
