c#https://www.geeksforgeeks.org/working-with-excel-files-using-pandas/
#https://stackoverflow.com/questions/63950775/how-can-i-insert-an-excel-formula-using-pandas-when-i-save-it-as-an-excel-file
#https://stackoverflow.com/questions/7225900/how-can-i-install-packages-using-pip-according-to-the-requirements-txt-file-fromi
#https://dev.to/blkkkbvsik/my-essential-toolkit-2023-daily-apps-and-software-hardware-for-flutter-development-nbk#:~:text=For%20Flutter%20development%2C%20my%20primary,room%20for%20any%20extra%20program.
#https://www.apple.com/shop/product/G1AK0LL/A/refurbished-16-inch-macbook-pro-apple-m3-pro-chip-with-12%E2%80%91core-cpu-and-18%E2%80%91core-gpu-silver?fnode=e937f3eaae1b1e85df1609a154592446e0e51ea957ebe2637e86bc7915a455004ee12a36fa6dadb6ec29a515f1747955cc15a934ae3b6d4086ecc82cebe1b9a1cf8f70c7798c89de399828f868ee3c17


''' import pandas as pd



file = 'pyExv1.xlsx'
sheet1 = pd.read_excel(file,
                      sheet_name = 1,
                      index_col = 0)

sheet2 = pd.read_excel(file,
                      sheet_name = 0,
                      index_col = 0)

newData = pd.concat([sheet1,sheet2])

print (newData) '''

import pandas as pd

file = 'pyExv1.xlsx'

sheet1 = pd.read_excel(file,
                       sheet_name = 0,
                       index_col = 0)
sheet2 = pd.read_excel(file,
                       sheet_name = 1,
                       index_col = 0)

newData = pd.concat([sheet1, sheet2])

'''
print(newData.head())
#To view 5 columns from the top and from the bottom of the data frame.
print(newData.tail())
'''


#Export the data back to an Excel file using the method to_excel.

newData.to_excel('firstExpo.xlsx')