from GetData import *
from FormFile import *
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt


def edgar_data(cik, form, year):
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

    # initializing this dataframe as empty
    # it is used to only once to start the dataframe
    # after it is initially populated, we use the append method
    df_cik = None
    for link in url:
        master_file_list = get_file_list(link)
        for xfile in master_file_list:
            # loops through the list to extract out the "master" file
            # master file is indexed by the cik code
            if xfile.startswith('master'):
                print(xfile)
                try:
                    df = pd.read_csv(link + xfile, sep='|', parse_dates=True, skiprows=7, header=None)
                    df.columns = ['CIK', 'Company Name', 'Form Type', 'Date Filed', 'File Name']

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
        get_details(url_detail_file, filename, count)
        count = count + 1


edgar_data(1506307, '4', ['2016', '2017'])
