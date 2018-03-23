from GetData import *
from FormFile import *
import pandas as pd
import numpy as np


root_url ='https://www.sec.gov/Archives/edgar/daily-index/'

year = ['2016','2017']
q = ['/QTR1/','/QTR2/','/QTR3/','/QTR4/']
url = []
for x in year:
    for y in q:
        url.append(root_url+x+y)

#url = [root_url + '2017/QTR3/', root_url + '2017/QTR4/', root_url + '2018/QTR1/']
url_detail_file = 'https://www.sec.gov/Archives/'
# import matplotlib.pyplot as plt

def edgar_data(cik, form):
    # local file
    # df = pd.read_csv\
    #    ('C:\\Users\\ralphd60\\Downloads\\master.20180116.idx',sep='|',parse_dates=True,skiprows = 7,header=None)

    df_cik = None
    for link in url:
        master_file_list = get_file_list(link)
        for xfile in master_file_list:
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

        count = 0
    for filename in df_cik['File Name']:
        print(filename)
        get_details(url_detail_file, filename,count)
        count = count + 1

edgar_data(1506307, '4')
